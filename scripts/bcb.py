# /// script
# requires-python = ">=3.11"
# dependencies = ["beautifulsoup4>=4.12", "markdownify>=0.13"]
# ///
"""Baixa os normativos do Banco Central e do CMN (busca de normas do BCB) e grava cada um em Markdown.

Uso:
  uv run scripts/bcb.py --indice            # só (re)monta _indice/busca.jsonl
  uv run scripts/bcb.py                     # índice (se faltar) + todas as normas
  uv run scripts/bcb.py --tipos "Resolução CMN" Circular --limite 20
  uv run scripts/bcb.py --relatorio         # só regrava COBERTURA.md

Idempotente e retomável: o JSON de cada norma fica em _fonte/ e não é baixado de novo.
O WAF do BCB bloqueia o IP por um tempo quando as requisições vêm rápido; ao detectar o bloqueio,
o script espera e tenta de novo.
"""
import argparse
import datetime as dt
import hashlib
import json
import re
import subprocess
import sys
import tempfile
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
FONTE = RAIZ / "_fonte"
INDICE = RAIZ / "_indice" / "busca.jsonl"
FALHAS = RAIZ / "_falhas.jsonl"
SITE = "https://www.bcb.gov.br"
BUSCA = SITE + "/api/search/app/normativos/buscanormativos"
UA = "Mozilla/5.0 (normas-bcb; +https://github.com/BrunooMoniz/normas-bcb)"
PAUSA = 1.5        # segundos entre requisições
ESPERA_BLOQUEIO = 600
POR_PAGINA = 500

# ordem de coleta: o que mais importa primeiro; Comunicado (a maioria são avisos de leilão) por último
OUTRAS_NORMAS = {"Comunicado", "Comunicado Conjunto", "Ato do Presidente", "Ato de Diretor",
                 "Ato Normativo Conjunto", "Decisão Conjunta"}
PRIORIDADE = ["Resolução CMN", "Resolução BCB", "Resolução Conjunta", "Resolução", "Circular",
              "Instrução Normativa BCB", "Carta Circular", "Ato do Presidente", "Ato de Diretor",
              "Ato Normativo Conjunto", "Decisão Conjunta", "Portaria Conjunta", "Instrução Normativa Conjunta"]


class Bloqueado(Exception):
    pass


# ---------- rede ----------

def pedir(url, json_esperado=True, tentativas=6):
    for i in range(tentativas):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json, */*"})
            with urllib.request.urlopen(req, timeout=120) as r:
                dados = r.read()
            time.sleep(PAUSA)
            if json_esperado and not dados.lstrip().startswith(b"{"):
                raise Bloqueado(url)  # o WAF responde 200 com a página "Requisição Inválida!"
            return dados
        except Bloqueado:
            if i == tentativas - 1:
                raise
            print(f"  bloqueio do WAF; esperando {ESPERA_BLOQUEIO}s", flush=True)
            time.sleep(ESPERA_BLOQUEIO)
        except urllib.error.HTTPError as e:
            if e.code in (400, 403, 404) or i == tentativas - 1:
                raise
            time.sleep(10 * (i + 1))
        except (urllib.error.URLError, TimeoutError, ConnectionError):
            if i == tentativas - 1:
                raise
            time.sleep(10 * (i + 1))


# ---------- índice ----------

def tipo_do_titulo(titulo):
    """'Resolução CMN N° 4.966' -> 'Resolução CMN'; é o valor que a API de conteúdo aceita em p1."""
    return re.split(r"\s+N(?:\s*[º°]|[o.](?=\s*\d))", titulo, maxsplit=1)[0].strip()


def tipo_api(titulo, tipo_busca):
    """Tipo aceito pela API: o da busca, salvo 'Resolução', que o título separa em CMN, BCB, Conjunta..."""
    if tipo_busca and tipo_busca != "Resolução":
        return tipo_busca
    return tipo_do_titulo(titulo)


def linha_indice(r):
    return {
        "titulo": r["title"].strip(),
        "tipo": tipo_api(r["title"].strip(), (r.get("TipodoNormativoOWSCHCS") or "").strip()),
        "numero": str(int(float(r["NumeroOWSNMBR"]))) if r.get("NumeroOWSNMBR") else "",
        "data": r.get("data", ""),
        "id": r.get("listItemId", ""),
        "responsavel": r.get("ResponsavelOWSText") or "",
        "revogado": r.get("RevogadoOWSBOOL") == "1",
        "cancelado": r.get("CanceladoOWSBOOL") == "1",
    }


def indexar():
    q = urllib.parse.urlencode({"querytext": "ContentType:normativo AND contentSource:normativos",
                                "rowlimit": POR_PAGINA, "sortlist": "Data1OWSDATE:ascending",
                                "refinementfilters": ""}, quote_via=urllib.parse.quote)
    linhas, inicio, total = {}, 0, None
    while total is None or inicio < total:
        d = json.loads(pedir(f"{BUSCA}?{q}&startrow={inicio}"))
        total = d["TotalRows"]
        if not d["Rows"]:
            break
        for r in d["Rows"]:
            li = linha_indice(r)
            linhas[li["id"] or li["titulo"]] = li
        inicio += POR_PAGINA
        print(f"  índice: {min(inicio, total)}/{total}", flush=True)
    INDICE.parent.mkdir(exist_ok=True)
    INDICE.write_text("".join(json.dumps(l, ensure_ascii=False) + "\n" for l in linhas.values()), encoding="utf-8")
    return list(linhas.values()), total


def ler_indice():
    return [json.loads(l) for l in INDICE.read_text(encoding="utf-8").splitlines()] if INDICE.exists() else []


# ---------- conteúdo ----------

def baixar_norma(tipo, numero, forcar=False):
    """JSON da norma; tenta 'exibenormativo' e depois 'exibeoutrasnormas' (comunicados, atos)."""
    cache = FONTE / slugify(tipo) / f"{numero}.json"
    if cache.exists() and not forcar:
        return json.loads(cache.read_text(encoding="utf-8"))
    p = urllib.parse.urlencode({"p1": tipo, "p2": numero}, quote_via=urllib.parse.quote)
    vistas = ("exibeoutrasnormas", "exibenormativo") if tipo in OUTRAS_NORMAS else ("exibenormativo", "exibeoutrasnormas")
    for vista in vistas:
        d = json.loads(pedir(f"{SITE}/api/conteudo/app/normativos/{vista}?{p}"))
        if d.get("conteudo"):
            d["_vista"] = vista
            cache.parent.mkdir(parents=True, exist_ok=True)
            cache.write_text(json.dumps(d, ensure_ascii=False), encoding="utf-8")
            return d
    raise LookupError(f"API sem conteúdo para {tipo} {numero}")


def url_pdf(arquivo, ano):
    """'C_Circ_0073_v1_O.pdf' de 1972 -> /pre/normativos/c_circ/1972/pdf/c_circ_0073_v1_o.pdf"""
    m = re.match(r"(.+?)_\d+", arquivo)
    return f"{SITE}/pre/normativos/{m[1].lower()}/{ano}/pdf/{arquivo.lower()}" if m else ""


def pdfs_em_ordem(documentos):
    """Do campo 'Documentos' ('X_v1_O.pdf;56#;X_v2_L.pdf;57#;'): primeiro as versões '_L' da mais nova para a
    mais antiga, depois as demais. O portal às vezes só publica a original (v1_O), por isso a lista inteira."""
    nomes = re.findall(r"([^;#]+\.pdf)", documentos or "", re.I)

    def versao(n):
        m = re.search(r"_v(\d+)_", n)
        return int(m[1]) if m else 0
    livres = sorted((n for n in nomes if re.search(r"_L\.pdf$", n, re.I)), key=versao, reverse=True)
    return livres + [n for n in nomes if n not in livres]


def pdf_para_texto(dados):
    with tempfile.TemporaryDirectory() as tmp:
        pdf = Path(tmp) / "a.pdf"
        pdf.write_bytes(dados)
        texto = subprocess.run(["pdftotext", "-enc", "UTF-8", str(pdf), "-"],
                               capture_output=True, text=True, timeout=300).stdout
        if len(re.sub(r"\s", "", texto)) >= 200:
            return texto, False
        subprocess.run(["pdftoppm", "-r", "200", "-png", str(pdf), str(Path(tmp) / "p")],
                       check=True, capture_output=True, timeout=900)
        partes = [subprocess.run(["tesseract", str(img), "-", "-l", "por"], capture_output=True,
                                 text=True, timeout=300).stdout for img in sorted(Path(tmp).glob("p*.png"))]
        return "\n\n".join(partes), True


def limpar_md(md):
    md = md.replace("\xa0", " ").replace("​", "").replace("\r", "").replace("\f", "\n")
    md = re.sub(r"[ \t]+\n", "\n", md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip() + "\n"


def html_para_md(html):
    from bs4 import BeautifulSoup
    from markdownify import markdownify

    html = (html or "").replace("&#58;", ":")
    sopa = BeautifulSoup(html, "html.parser")
    for t in sopa(["script", "style"]):
        t.decompose()
    for pre in sopa("pre"):  # normas antigas vêm em <pre> de máquina de escrever: vira bloco de código
        pre.string = pre.get_text()
    return limpar_md(markdownify(str(sopa), heading_style="ATX", strip=["img"]))


def texto_simples(html):
    from bs4 import BeautifulSoup
    return " ".join(BeautifulSoup(html or "", "html.parser").get_text(" ").split())


def lista(campo):
    return [x.strip() for x in (campo or "").split(";#") if x.strip()]


def vinculadas(campo):
    """'CIRCULAR;@3913;@2018;#RESOLUÇÃO BCB;@594;@2026;#' -> ['CIRCULAR 3913/2018', 'RESOLUÇÃO BCB 594/2026']"""
    out = []
    for item in lista(campo):
        partes = [p.strip() for p in item.split(";@")]
        if len(partes) >= 3:
            out.append(f"{partes[0]} {partes[1]}/{partes[2]}")
        elif partes:
            out.append(" ".join(partes))
    return out


# ---------- saída ----------

def slugify(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


# 'Resolução' sem sigla é a série do CMN até a 4.838 (2020); a 4.839 em diante se chama 'Resolução CMN'
PASTAS = {
    "Resolução": "resolucoes-cmn", "Resolução CMN": "resolucoes-cmn", "Resolução BCB": "resolucoes-bcb",
    "Resolução Conjunta": "resolucoes-conjuntas", "Resolução Coseg": "resolucoes-coseg",
    "Resolução Coremec": "resolucoes-coremec", "Circular": "circulares", "Carta Circular": "cartas-circulares",
    "Comunicado": "comunicados", "Comunicado Conjunto": "comunicados-conjuntos",
    "Instrução Normativa BCB": "instrucoes-normativas-bcb", "Instrução Normativa Conjunta": "instrucoes-normativas-conjuntas",
    "Ato do Presidente": "atos-do-presidente", "Ato de Diretor": "atos-de-diretor",
    "Ato Normativo Conjunto": "atos-normativos-conjuntos", "Decisão Conjunta": "decisoes-conjuntas",
    "Portaria Conjunta": "portarias-conjuntas",
}


def pasta_do_tipo(tipo):
    return PASTAS.get(tipo) or slugify(tipo)


def nome_arquivo(tipo, numero):
    return f"{slugify('Resolução CMN' if tipo == 'Resolução' else tipo)}-{numero.zfill(4)}.md"


def data_local(c, linha):
    m = re.match(r"(\d{1,2})/(\d{1,2})/(\d{4})", c.get("DataTexto") or "")
    if m:
        return f"{m[3]}-{int(m[2]):02d}-{int(m[1]):02d}"
    return (c.get("Data") or linha.get("data") or "")[:10]


def yaml(v):
    return json.dumps(v, ensure_ascii=False)


def orgao_de(tipo):
    if tipo.startswith("Resolução CMN") or tipo == "Resolução":
        return "Conselho Monetário Nacional"
    if tipo in ("Resolução Conjunta", "Portaria Conjunta"):
        return "Banco Central do Brasil e outros órgãos"
    return "Banco Central do Brasil"


def fatia_de(linha, n):
    """Fatia estável por chave (o índice muda de ordem quando entram normas novas)."""
    return int(hashlib.sha1(f"{linha['tipo']}:{linha['numero']}".encode()).hexdigest(), 16) % n


def tem_md(linha):
    return any((RAIZ / pasta_do_tipo(linha["tipo"])).glob(f"*/{nome_arquivo(linha['tipo'], linha['numero'])}"))


def montar(linha, d, hoje):
    c = d["conteudo"][0]
    tipo = c.get("Tipo") or linha["tipo"]
    numero = linha["numero"]
    data = data_local(c, linha)
    corpo, ocr, arquivo, sha = html_para_md(c.get("Texto")), False, "", ""
    versao = "texto do portal do BCB"
    if len(re.sub(r"\W", "", corpo)) < 200 and c.get("Documentos"):
        for nome in pdfs_em_ordem(c["Documentos"]):
            url = url_pdf(nome, data[:4])
            cache = FONTE / "pdf" / nome
            if not cache.exists():
                try:
                    dados = pedir(url, json_esperado=False)
                except urllib.error.HTTPError as e:
                    if e.code == 404:
                        continue  # versão não publicada nesse endereço: tenta a próxima
                    raise
                cache.parent.mkdir(parents=True, exist_ok=True)
                cache.write_bytes(dados)
            dados = cache.read_bytes()
            texto, ocr = pdf_para_texto(dados)
            if len(re.sub(r"\W", "", texto)) >= 40:
                corpo, arquivo, sha = limpar_md(texto), url, hashlib.sha256(dados).hexdigest()
                versao = "PDF do portal do BCB" + (" (OCR)" if ocr else "")
                break
    if len(re.sub(r"\W", "", corpo)) < 20:
        corpo = "> O portal do BCB não traz o texto desta norma; ficaram só os metadados.\n"
        versao = "metadados apenas"
    fonte = f"{SITE}/estabilidadefinanceira/{d.get('_vista', 'exibenormativo')}?" + urllib.parse.urlencode(
        {"tipo": tipo, "numero": numero}, quote_via=urllib.parse.quote)
    campos = [
        ("titulo", yaml(" ".join((c.get("Titulo") or linha["titulo"]).split()))),
        ("orgao", yaml(orgao_de(tipo))),
        ("tipo", yaml(tipo)),
        ("numero", yaml(numero)),
        ("data", data),
        ("ementa", yaml(texto_simples(c.get("Assunto")))),
        ("revogada", "true" if c.get("Revogado") else "false"),
        ("cancelada", "true" if c.get("Cancelado") else None),
        ("responsavel", yaml(linha["responsavel"]) if linha.get("responsavel") else None),
        ("versao_texto", yaml(versao)),
        ("versao_normativo", yaml(str(int(c["VersaoNormativo"]))) if c.get("VersaoNormativo") else None),
        ("publicacao", yaml(c["DOU"]) if c.get("DOU") else None),
        ("atualizacoes", yaml(lista(c.get("Atualizacoes")))) if c.get("Atualizacoes") else (None, None),
        ("normas_vinculadas", yaml(vinculadas(c.get("NormasVinculadas")))) if c.get("NormasVinculadas") else (None, None),
        ("referencias", yaml(lista(c.get("Referencias")))) if c.get("Referencias") else (None, None),
        ("fonte", yaml(fonte)),
        ("arquivo", yaml(arquivo) if arquivo else None),
        ("sha256_arquivo", sha or None),
        ("ocr", "true" if ocr else None),
        ("baixado_em", hoje),
    ]
    cab = "\n".join(f"{k}: {v}" for k, v in campos if k and v is not None)
    titulo = " ".join((c.get("Titulo") or linha["titulo"]).split())
    saida = RAIZ / pasta_do_tipo(linha["tipo"]) / (data[:4] or "sem-data") / nome_arquivo(linha["tipo"], numero)
    return saida, f"---\n{cab}\n---\n# {titulo}\n\n{corpo}", versao


def ordem(linha):
    t = linha["tipo"]
    return (PRIORIDADE.index(t) if t in PRIORIDADE else len(PRIORIDADE) + (t == "Comunicado"), linha["data"])


# ---------- relatório ----------

def relatorio():
    idx = ler_indice()
    falhas = [json.loads(l) for l in FALHAS.read_text(encoding="utf-8").splitlines()] if FALHAS.exists() else []
    por_pasta = {}  # pasta: [tipos, índice, md, só metadados, falhas]
    for l in idx:
        v = por_pasta.setdefault(pasta_do_tipo(l["tipo"]), [set(), 0, 0, 0, 0])
        v[0].add(l["tipo"])
        v[1] += 1
    for f in falhas:
        por_pasta.setdefault(pasta_do_tipo(f["tipo"]), [set(), 0, 0, 0, 0])[4] += 1
    for pasta, v in por_pasta.items():
        mds = list((RAIZ / pasta).rglob("*.md"))
        v[2] = len(mds)
        v[3] = sum(1 for p in mds if 'versao_texto: "metadados apenas"' in p.read_text(encoding="utf-8")[:20000])
    linhas = ["# Cobertura", "",
              "Gerado por `scripts/bcb.py --relatorio`. Índice = itens na busca de normas do BCB.", "",
              "| Pasta | Tipos | Índice | Arquivos .md | Só metadados | Falhas |",
              "| --- | --- | ---: | ---: | ---: | ---: |"]
    tot = [0, 0, 0, 0]
    for pasta, v in sorted(por_pasta.items(), key=lambda kv: -kv[1][1]):
        tot = [a + b for a, b in zip(tot, v[1:])]
        linhas.append(f"| `{pasta}/` | {', '.join(sorted(v[0]))} | " + " | ".join(f"{x:,}".replace(",", ".") for x in v[1:]) + " |")
    linhas.append("| **Total** | | " + " | ".join(f"**{x:,}**".replace(",", ".") for x in tot) + " |")
    (RAIZ / "COBERTURA.md").write_text("\n".join(linhas) + "\n", encoding="utf-8")
    import readme  # números do README e progresso.svg saem da mesma medição
    readme.main(readme.CONFIG)
    return tot


def gravar(linha, d, hoje):
    saida, md, _ = montar(linha, d, hoje)
    saida.parent.mkdir(parents=True, exist_ok=True)
    saida.write_text(md, encoding="utf-8")
    return saida


def atualizar_novos(dias, hoje):
    """Modo leve (job agendado): normas publicadas nos últimos `dias` que ainda não têm .md,
    mais as normas vinculadas a elas (revogadas ou alteradas), que são baixadas de novo."""
    idx = ler_indice()
    por_id = {l["id"]: l for l in idx}
    por_chave = {(l["tipo"], l["numero"]): l for l in idx}
    tipos = {slugify(l["tipo"]): l["tipo"] for l in idx}
    corte = (dt.date.today() - dt.timedelta(days=dias)).isoformat()
    q = urllib.parse.urlencode({"querytext": "ContentType:normativo AND contentSource:normativos", "rowlimit": 100,
                                "sortlist": "Data1OWSDATE:descending", "refinementfilters": ""},
                               quote_via=urllib.parse.quote)
    recentes, inicio = [], 0
    while True:
        rows = json.loads(pedir(f"{BUSCA}?{q}&startrow={inicio}"))["Rows"]
        novos = [linha_indice(r) for r in rows if (r.get("data") or "")[:10] >= corte]
        recentes += novos
        if len(novos) < len(rows) or not rows:
            break
        inicio += len(rows)
    for li in recentes:
        if li["id"] not in por_id:
            idx.append(li)
            por_id[li["id"]] = li
            por_chave[(li["tipo"], li["numero"])] = li
            tipos.setdefault(slugify(li["tipo"]), li["tipo"])
    INDICE.parent.mkdir(exist_ok=True)
    INDICE.write_text("".join(json.dumps(l, ensure_ascii=False) + "\n" for l in idx), encoding="utf-8")

    def existe(li):
        return any((RAIZ / pasta_do_tipo(li["tipo"])).rglob(nome_arquivo(li["tipo"], li["numero"])))

    falhas = {(f["tipo"], f["numero"]): f for f in
              (json.loads(l) for l in (FALHAS.read_text(encoding="utf-8").splitlines() if FALHAS.exists() else []))}
    n_novas = n_atual = 0
    for li in [l for l in recentes if not existe(l)]:
        try:
            d = baixar_norma(li["tipo"], li["numero"], forcar=True)
            print(f"nova: {gravar(li, d, hoje).relative_to(RAIZ)}", flush=True)
            falhas.pop((li["tipo"], li["numero"]), None)
            n_novas += 1
        except Exception as e:
            falhas[(li["tipo"], li["numero"])] = {"tipo": li["tipo"], "numero": li["numero"], "titulo": li["titulo"],
                                                  "erro": f"{type(e).__name__}: {e}"}
            continue
        for item in lista(d["conteudo"][0].get("NormasVinculadas")):
            partes = [x.strip() for x in item.split(";@")]
            ref = por_chave.get((tipos.get(slugify(partes[0]), ""), partes[1] if len(partes) > 1 else ""))
            if ref and existe(ref):  # só regrava o que já está no acervo; o resto a coleta completa traz
                try:
                    print(f"atualizada: {gravar(ref, baixar_norma(ref['tipo'], ref['numero'], forcar=True), hoje).relative_to(RAIZ)}", flush=True)
                    n_atual += 1
                except Exception as e:
                    print(f"  falha ao atualizar {ref['titulo']}: {e}", flush=True)
    FALHAS.write_text("".join(json.dumps(f, ensure_ascii=False) + "\n" for f in sorted(
        falhas.values(), key=lambda f: (f["tipo"], f["numero"]))), encoding="utf-8")
    print(f"{n_novas} novas, {n_atual} atualizadas; total [índice, md, só metadados, falhas]:", relatorio())


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--indice", action="store_true", help="só remonta o índice")
    ap.add_argument("--reindexar", action="store_true", help="remonta o índice antes de baixar")
    ap.add_argument("--tipos", nargs="*", help="só estes tipos (como aparecem no título, ex.: 'Resolução CMN')")
    ap.add_argument("--limite", type=int, help="só as N primeiras de cada tipo")
    ap.add_argument("--forcar", action="store_true", help="baixa de novo o que está em cache")
    ap.add_argument("--relatorio", action="store_true", help="só regrava COBERTURA.md")
    ap.add_argument("--fatia", metavar="K/N", help="só a fatia K de N (coleta em paralelo, uma por máquina)")
    ap.add_argument("--pular-existentes", action="store_true", help="pula normas que já têm .md no repositório")
    ap.add_argument("--novos", type=int, metavar="DIAS",
                    help="modo leve: só normas dos últimos DIAS sem .md, mais as vinculadas a elas (job agendado)")
    a = ap.parse_args()
    if a.novos:
        return atualizar_novos(a.novos, dt.date.today().isoformat())
    if a.relatorio:
        print(relatorio())
        return
    if a.indice or a.reindexar or not INDICE.exists():
        idx, total = indexar()
        print(f"índice: {len(idx)} normas únicas de {total} resultados", flush=True)
        if a.indice:
            return
    idx = sorted(ler_indice(), key=ordem)
    if a.tipos:
        idx = [l for l in idx if l["tipo"] in a.tipos]
    if a.fatia:
        k, n = map(int, a.fatia.split("/"))
        idx = [l for l in idx if fatia_de(l, n) == k]
    if a.pular_existentes:
        idx = [l for l in idx if not tem_md(l)]
        print(f"pendentes: {len(idx)}", flush=True)
    if a.limite:
        cont, sel = {}, []
        for l in idx:
            cont[l["tipo"]] = cont.get(l["tipo"], 0) + 1
            if cont[l["tipo"]] <= a.limite:
                sel.append(l)
        idx = sel
    hoje = dt.date.today().isoformat()
    falhas = {(f["tipo"], f["numero"]): f for f in
              (json.loads(l) for l in (FALHAS.read_text(encoding="utf-8").splitlines() if FALHAS.exists() else []))}
    for n, linha in enumerate(idx, 1):
        chave = (linha["tipo"], linha["numero"])
        try:
            d = baixar_norma(linha["tipo"], linha["numero"], a.forcar)
            saida, md, versao = montar(linha, d, hoje)
            saida.parent.mkdir(parents=True, exist_ok=True)
            saida.write_text(md, encoding="utf-8")
            falhas.pop(chave, None)
        except Bloqueado:
            print("bloqueio persistente do WAF; pare e retome mais tarde (o progresso fica salvo)", flush=True)
            break
        except Exception as e:
            falhas[chave] = {"tipo": linha["tipo"], "numero": linha["numero"], "titulo": linha["titulo"],
                             "erro": f"{type(e).__name__}: {e}"}
        if n % 100 == 0:
            print(f"  {n}/{len(idx)} ({linha['tipo']})", flush=True)
            FALHAS.write_text("".join(json.dumps(f, ensure_ascii=False) + "\n" for f in sorted(
                falhas.values(), key=lambda f: (f["tipo"], f["numero"]))), encoding="utf-8")
    FALHAS.write_text("".join(json.dumps(f, ensure_ascii=False) + "\n" for f in sorted(
        falhas.values(), key=lambda f: (f["tipo"], f["numero"]))), encoding="utf-8")
    print("total [índice, md, só metadados, falhas]:", relatorio())


if __name__ == "__main__":
    sys.exit(main())
