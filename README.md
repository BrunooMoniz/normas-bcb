# Normas do Banco Central e do CMN em Markdown

Todos os normativos da [busca de normas do Banco Central](https://www.bcb.gov.br/estabilidadefinanceira/buscanormas),
convertidos para Markdown com cabeçalho estruturado e link para a origem de cada texto: resoluções do
Conselho Monetário Nacional e do BCB, resoluções conjuntas, circulares, cartas circulares, instruções
normativas, atos do presidente e de diretor, comunicados e as demais séries, de 1965 até hoje.

Inspirado no [ctresb/leis](https://github.com/ctresb/leis), que reúne a legislação brasileira no mesmo
formato. O Banco Central não edita leis: as leis do Sistema Financeiro Nacional (Lei 4.595/1964,
Lei 9.069/1995, Lei Complementar 105/2001 e as demais) já estão lá, em `federal/`; aqui ficam só os atos
do BCB e do CMN. As normas da CVM estão em [normas-cvm](https://github.com/BrunooMoniz/normas-cvm).

As contagens por pasta, com o que ficou de fora, estão em **[COBERTURA.md](COBERTURA.md)**.

> [!IMPORTANT]
> Os textos têm caráter informativo e **não substituem a publicação no Diário Oficial da União** nem o
> portal do BCB. São conversões automáticas (e OCR, nos documentos escaneados). Confira sempre a fonte
> indicada no cabeçalho antes de citar.

## Estrutura

```
resolucoes-cmn/AAAA/resolucao-cmn-NNNN.md        Resoluções do CMN, nº 1 (1965) em diante, numa série só
resolucoes-bcb/AAAA/resolucao-bcb-NNNN.md        Resoluções BCB (2020 em diante)
resolucoes-conjuntas/                            Resoluções conjuntas
circulares/  cartas-circulares/                  Circulares e Cartas Circulares
instrucoes-normativas-bcb/                       Instruções Normativas BCB
atos-do-presidente/  atos-de-diretor/            Atos do Presidente e de Diretor
comunicados/  comunicados-conjuntos/             Comunicados (inclui os avisos e resultados de leilão)
decisoes-conjuntas/  portarias-conjuntas/  atos-normativos-conjuntos/  instrucoes-normativas-conjuntas/
resolucoes-coseg/  resolucoes-coremec/
scripts/bcb.py                                   o código que baixa, converte e mede
COBERTURA.md                                     números por pasta e lacunas
_falhas.jsonl                                    o que não entrou, linha por linha, e por quê
```

`AAAA` é o ano da norma. As resoluções do CMN anteriores a julho de 2020 se chamam "Resolução" no portal
(nº 1 a 4.838); daí em diante, "Resolução CMN" (4.839 em diante). Como a numeração é contínua, as duas
ficam na mesma pasta. Fora do versionamento, porque o script os reproduz: `_fonte/` (o JSON de cada norma
e os PDFs) e `_indice/`.

## Formato dos arquivos

```markdown
---
titulo: "Resolução CMN N° 4.839"
orgao: "Conselho Monetário Nacional"
tipo: "Resolução CMN"
numero: "4839"
data: 2020-07-30
ementa: "Altera o preço de referência para as operações de Financiamento Especial para Estocagem ..."
revogada: true
responsavel: "SECRE"
versao_texto: "texto do portal do BCB"
versao_normativo: "2"
publicacao: "Publicada no DOU de 3/8/2020, Seção 1, p. 53."
atualizacoes: ["Resolução CMN nº 4.903/2021 - Revogação total, a partir de 1º/5/2021."]
normas_vinculadas: ["RESOLUÇÃO CMN 4903/2021"]
referencias: ["Lei nº 4.595/1964, arts. 4º, inciso VI, e 9º.", "..."]
fonte: "https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20CMN&numero=4839"
baixado_em: 2026-11-10
---
# Resolução CMN N° 4.839

RESOLUÇÃO CMN Nº 4.839, DE 30 DE JULHO DE 2020
...
```

`titulo`, `orgao`, `tipo`, `numero`, `data`, `revogada`, `versao_texto`, `fonte` e `baixado_em` existem em
todos os arquivos; os demais aparecem quando o portal os informa. O texto é o que o portal do BCB publica
(a versão vigente, quando a norma foi alterada; `versao_normativo` diz qual). Quando o portal não traz o
texto, ele vem do PDF oficial (`arquivo` e `sha256_arquivo`), com `ocr: true` se foi lido por OCR. Normas
antigas, datilografadas, saem em bloco de código para preservar o alinhamento original.

## Reproduzir e atualizar

Precisa de [uv](https://docs.astral.sh/uv/), do `pdftotext` (poppler) e do `tesseract` com português.

```
uv run scripts/bcb.py                              # índice + tudo (retoma de onde parou)
uv run scripts/bcb.py --reindexar                  # pega normas novas
uv run scripts/bcb.py --tipos "Resolução CMN" --forcar   # baixa de novo uma série
uv run scripts/test_bcb.py                         # testes
```

O portal do BCB bloqueia por alguns minutos o IP que faz muitas requisições seguidas. O script vai devagar
(1,5 s entre pedidos), espera quando é bloqueado e retoma de onde parou; a coleta completa leva cerca de
um dia.

## Licença

Código sob MIT. Os textos normativos são atos oficiais e não têm proteção de direito autoral
(Lei 9.610/1998, art. 8º, IV).
