# /// script
# requires-python = ">=3.11"
# dependencies = ["beautifulsoup4>=4.12", "markdownify>=0.13"]
# ///
"""Testes do conversor do BCB. Rodar: uv run scripts/test_bcb.py"""
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import bcb  # noqa: E402
import grafo  # noqa: E402

FIX = Path(__file__).parent / "fixtures"


class Basicos(unittest.TestCase):
    def test_fatias_cobrem_tudo_uma_vez(self):
        linhas = [{"tipo": t, "numero": str(n)} for t in ("Comunicado", "Circular", "Resolução") for n in range(1, 400)]
        for n in (1, 2, 12):
            vistas = [l for k in range(n) for l in linhas if bcb.fatia_de(l, n) == k]
            self.assertEqual(sorted(map(str, vistas)), sorted(map(str, linhas)))

    def test_tipo_do_titulo(self):
        self.assertEqual(bcb.tipo_do_titulo("Resolução CMN N° 4.966"), "Resolução CMN")
        self.assertEqual(bcb.tipo_do_titulo("Circular Nº 1"), "Circular")
        # 'Normativa' não pode ser confundido com 'No'
        self.assertEqual(bcb.tipo_do_titulo("Instrução Normativa BCB N° 12"), "Instrução Normativa BCB")
        self.assertEqual(bcb.tipo_do_titulo("COMUNICADO N. 002002"), "COMUNICADO")

    def test_tipo_api(self):
        self.assertEqual(bcb.tipo_api("COMUNICADO N. 002002", "Comunicado"), "Comunicado")
        self.assertEqual(bcb.tipo_api("Resolução BCB N° 366", "Resolução"), "Resolução BCB")
        self.assertEqual(bcb.tipo_api("Resolução Nº 1", "Resolução"), "Resolução")

    def test_campos_em_lista(self):
        self.assertEqual(bcb.vinculadas("CIRCULAR;@3913;@2018;#RESOLUÇÃO BCB;@594;@2026;#"),
                         ["CIRCULAR 3913/2018", "RESOLUÇÃO BCB 594/2026"])
        self.assertEqual(bcb.lista("a;#b;#"), ["a", "b"])

    def test_pdf(self):
        self.assertEqual(bcb.pdfs_em_ordem("X_0001_v1_O.pdf;1#;X_0001_v2_L.pdf;2#;X_0001_v10_L.pdf;3#;"),
                         ["X_0001_v10_L.pdf", "X_0001_v2_L.pdf", "X_0001_v1_O.pdf"])
        self.assertEqual(bcb.pdfs_em_ordem("C_Circ_0073_v1_O.pdf;56#;"), ["C_Circ_0073_v1_O.pdf"])
        self.assertEqual(bcb.url_pdf("C_Circ_0073_v1_O.pdf", "1972"),
                         "https://www.bcb.gov.br/pre/normativos/c_circ/1972/pdf/c_circ_0073_v1_o.pdf")

    def test_serie_antiga_do_cmn_vai_junto_da_nova(self):
        self.assertEqual(bcb.pasta_do_tipo("Resolução"), bcb.pasta_do_tipo("Resolução CMN"))
        self.assertEqual(bcb.nome_arquivo("Resolução", "1"), "resolucao-cmn-0001.md")

    def test_ordem_comunicado_por_ultimo(self):
        l = [{"tipo": "Comunicado", "data": "1990"}, {"tipo": "Tipo Novo", "data": "1990"}, {"tipo": "Resolução CMN", "data": "2025"}]
        self.assertEqual([x["tipo"] for x in sorted(l, key=bcb.ordem)], ["Resolução CMN", "Tipo Novo", "Comunicado"])


class NormaReal(unittest.TestCase):
    def test_montar_resolucao_cmn(self):
        d = json.loads((FIX / "resolucao-cmn-4839.json").read_text(encoding="utf-8"))
        linha = {"titulo": "Resolução CMN N° 4.839", "tipo": "Resolução CMN", "numero": "4839", "data": "", "responsavel": "SECRE"}
        saida, md, versao = bcb.montar(linha, d, "2026-11-10")
        self.assertEqual(saida.relative_to(bcb.RAIZ).as_posix(), "resolucoes-cmn/2020/resolucao-cmn-4839.md")
        self.assertEqual(versao, "texto do portal do BCB")
        self.assertIn('orgao: "Conselho Monetário Nacional"', md)
        self.assertIn("data: 2020-07-30", md)
        self.assertIn("revogada: true", md)
        self.assertIn("RESOLUÇÃO CMN Nº 4.839", md)
        self.assertNotIn("&#58;", md)


class Grafo(unittest.TestCase):
    """Relações lidas dos cabeçalhos reais do acervo (scripts/grafo.py)."""

    @classmethod
    def setUpClass(cls):
        cls.g = grafo.montar(bcb.RAIZ, "bcb", hoje="2026-11-11")
        cls.arestas = {(a["de"], a["para"], a["relacao"]): a for a in cls.g["arestas"]}
        cls.estado = {e["id"]: e for e in cls.g["estado"]}
        cls.externos = {e["id"]: e["url"] for e in cls.g["externos"]}

    def ids(self, texto, acervo="bcb"):
        return [c[0] for c in grafo.citar(grafo.sem_datas(grafo.plano(texto)), acervo)]

    def test_id_igual_nas_variacoes_de_escrita(self):
        for texto in ("Resolução CMN nº 4.903/2021 - Revogação total, a partir de 1º/5/2021.", "RESOLUÇÃO CMN 4903/2021",
                      "RESOLUÇÃO CMN 4903/21 DOU 30/04/2021 PAG 82 - REVOGACAO TOTAL."):
            self.assertEqual(self.ids(texto), ["bcb:resolucao-cmn:4903"])
        self.assertEqual(self.ids("RESOLUÇÃO 3402/2006"), ["bcb:resolucao-cmn:3402"])  # série antiga do CMN, sem sigla
        self.assertEqual(self.ids("Revoga, a partir de 1º/3/2023, Circular BCB nº 3.336/2006."), ["bcb:circular:3336"])
        self.assertEqual(self.ids("CIRCULAR 3336/2006"), ["bcb:circular:3336"])
        self.assertEqual(self.ids("CARTA/CIRCULAR BCB 2823/98 - REVOGACAO TOTAL."), ["bcb:carta-circular:2823"])
        self.assertEqual(self.ids("Cita Resoluções CMN ns 1.339/1987; 1.409/1987 e 1.595/1989."),
                         ["bcb:resolucao-cmn:1339", "bcb:resolucao-cmn:1409", "bcb:resolucao-cmn:1595"])
        self.assertEqual(self.ids("Lei nº 4.595/1964, arts. 4º, inciso VI, e 9º."), ["lei:4595-1964"])  # artigo não é norma
        self.assertEqual(self.ids("LEI 4595/64 ART/9."), ["lei:4595-1964"])
        self.assertEqual(self.ids("Cita Instruções CVM ns. 209/1994, 472/2008."), ["cvm:instrucao:209", "cvm:instrucao:472"])
        self.assertEqual(self.ids("CARTA CIRCULAR BCB 53 DE 6/12/1971 - REVOGACAO TOTAL, A PARTIR DE 1/1/1972."),
                         ["bcb:carta-circular:53"])
        self.assertEqual(grafo.desde(grafo.plano("Revogação total, a partir de 1º/5/2021.")), "2021-05-01")

    def test_id_resolve_para_o_arquivo(self):
        for tipo, numero, ano in (("Resolução CMN", "4839", "2020"), ("Resolução", "1", "1965"), ("Circular", "3336", "2006")):
            caminho = f"{bcb.pasta_do_tipo(tipo)}/{ano}/{bcb.nome_arquivo(tipo, numero)}"
            self.assertTrue((bcb.RAIZ / caminho).exists(), caminho)
            self.assertEqual(self.estado[grafo.id_local(caminho, {}, "bcb")]["caminho"], caminho)
        self.assertEqual(grafo.id_local("resolucoes-cmn/1965/resolucao-cmn-0001.md", {}, "bcb"), "bcb:resolucao-cmn:1")

    def test_resolucao_cmn_4839_revogada_pela_4903(self):
        a = self.arestas[("bcb:resolucao-cmn:4903", "bcb:resolucao-cmn:4839", "revoga")]
        self.assertEqual(a["desde"], "2021-05-01")
        self.assertIn("atualizacoes", a["fonte"])
        e = self.estado["bcb:resolucao-cmn:4839"]
        self.assertEqual((e["caminho"], e["estado"], e["por"]),
                         ("resolucoes-cmn/2020/resolucao-cmn-4839.md", "revogada", ["bcb:resolucao-cmn:4903"]))

    def test_resolucao_bcb_283_revoga_circular_e_regulamenta_lei(self):
        self.assertEqual(self.arestas[("bcb:resolucao-bcb:283", "bcb:circular:3336", "revoga")]["desde"], "2023-03-01")
        self.assertEqual(self.estado["bcb:circular:3336"]["por"], ["bcb:resolucao-bcb:283"])
        self.assertIn(("bcb:resolucao-bcb:283", "lei:4595-1964", "regulamenta"), self.arestas)
        self.assertIn(("bcb:resolucao-bcb:283", "bcb:resolucao-cmn:5057", "cita"), self.arestas)
        self.assertEqual(self.externos["lei:4595-1964"],
                         "https://github.com/ctresb/leis/blob/main/federal/leis-ordinarias/1964/lei-4595-1964-12-31.md")
        self.assertEqual(self.estado["bcb:resolucao-bcb:283"]["estado"], "vigente")

    def test_norma_conjunta_liga_ao_acervo_da_cvm(self):
        par = "cvm:resolucao-conjunta-bcb:13-2024"
        self.assertIn(("bcb:resolucao-conjunta:13", par, "conjunta"), self.arestas)
        self.assertEqual(self.externos[par],
                         "https://github.com/BrunooMoniz/normas-cvm/blob/main/decisoes-conjuntas/2024/rcbccvm13.md")
        # a Decisão Conjunta 18 do BCB é de 2010; a 18/13 da CVM é outra norma: mesmo número não basta
        self.assertFalse([k for k in self.arestas if k[0] == "bcb:decisao-conjunta:18" and k[2] == "conjunta"])

    def test_citacao_de_norma_da_cvm_aponta_para_o_outro_acervo(self):
        self.assertIn(("bcb:circular:3261", "cvm:instrucao:409", "cita"), self.arestas)
        self.assertEqual(self.externos["cvm:instrucao:409"],
                         "https://github.com/BrunooMoniz/normas-cvm/blob/main/instrucoes/2004/inst409.md")

    def test_revogacao_parcial_e_prorrogacao_nao_revogam_a_norma(self):
        # 'Altera, a partir de 1º/5/2021, Resolução CMN nº 3.583/2008 - Revoga: art. 4º.'
        for r in ("altera", "revoga_parcial"):
            self.assertEqual(self.arestas[("bcb:resolucao-cmn:4903", "bcb:resolucao-cmn:3583", r)]["desde"], "2021-05-01")
        self.assertNotIn(("bcb:resolucao-cmn:4903", "bcb:resolucao-cmn:3583", "revoga"), self.arestas)
        # 'CIRCULAR BCB 827/1983 ... PRORROGA PARA 2/1/1984 A DATA DE REVOGACAO TOTAL DESTA CARTA CIRCULAR'
        self.assertIn(("bcb:circular:827", "bcb:carta-circular:391", "altera"), self.arestas)
        self.assertEqual(self.estado["bcb:carta-circular:391"]["por"], ["bcb:circular:813"])

    def test_nada_some_em_silencio(self):
        achaveis = set(self.estado) | set(self.externos) | {x["id"] for x in self.g["nao_resolvidos"]}
        self.assertFalse([a for a in self.g["arestas"] if a["de"] not in achaveis or a["para"] not in achaveis])
        soltos = {x["id"]: x for x in self.g["nao_resolvidos"]}
        self.assertGreater(soltos["ext:portaria-bcb:100288-2018"]["arestas"], 0)  # Portaria BCB não está no acervo
        self.assertFalse(set(soltos) & (set(self.estado) | set(self.externos)))
        self.assertEqual({a["relacao"] for a in self.g["arestas"]} - set(grafo.RELACOES), set())


if __name__ == "__main__":
    unittest.main()
