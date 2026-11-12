# Cobertura

Gerado por `scripts/bcb.py --relatorio`. Índice = itens na busca de normas do BCB.

| Pasta | Tipos | Índice | Arquivos .md | Só metadados | Falhas |
| --- | --- | ---: | ---: | ---: | ---: |
| `comunicados/` | Comunicado | 43.936 | 43.936 | 1 | 0 |
| `resolucoes-cmn/` | Resolução, Resolução CMN | 5.344 | 5.344 | 8 | 0 |
| `cartas-circulares/` | Carta Circular | 4.076 | 4.076 | 16 | 0 |
| `circulares/` | Circular | 4.038 | 4.038 | 11 | 0 |
| `atos-do-presidente/` | Ato do Presidente | 1.391 | 1.391 | 0 | 0 |
| `instrucoes-normativas-bcb/` | Instrução Normativa BCB | 786 | 786 | 0 | 0 |
| `atos-de-diretor/` | Ato de Diretor | 706 | 706 | 0 | 0 |
| `resolucoes-bcb/` | Resolução BCB | 604 | 604 | 0 | 0 |
| `atos-normativos-conjuntos/` | Ato Normativo Conjunto | 31 | 31 | 0 | 0 |
| `resolucoes-conjuntas/` | Resolução Conjunta | 21 | 21 | 0 | 0 |
| `comunicados-conjuntos/` | Comunicado Conjunto | 20 | 20 | 0 | 0 |
| `decisoes-conjuntas/` | Decisão Conjunta | 20 | 20 | 0 | 0 |
| `portarias-conjuntas/` | Portaria Conjunta | 8 | 8 | 0 | 0 |
| `instrucoes-normativas-conjuntas/` | Instrução Normativa Conjunta | 4 | 4 | 0 | 0 |
| `resolucoes-coseg/` | Resolução Coseg | 4 | 4 | 0 | 0 |
| `resolucoes-coremec/` | Resolução Coremec | 1 | 1 | 0 | 0 |
| **Total** | | **60.990** | **60.990** | **36** | **0** |

## Grafo de relações

Gerado por `scripts/grafo.py` a partir dos cabeçalhos, sem IA. Fica em `grafo/`: `arestas.jsonl` (uma relação por linha), `estado.jsonl` (situação de cada norma), `externos.jsonl` (normas do outro acervo e leis do ctresb/leis) e `nao_resolvidos.jsonl`.

| Relação | Arestas | Não resolvidas |
| --- | ---: | ---: |
| revoga | 14.441 | 1.054 |
| revoga_parcial | 2.028 | 43 |
| altera | 5.724 | 33 |
| cita | 28.226 | 2.129 |
| regulamenta | 18.899 | 106 |
| conjunta | 14 | 0 |
| **Total** | **69.332** | **3.365** (4,9%) |

Não resolvida = aresta que aponta para uma norma sem arquivo neste acervo, no outro ou no ctresb/leis (1.723 normas distintas). Trechos dos cabeçalhos sem norma reconhecida: 3.691. Situação calculada: 47.403 vigentes, 529 alteradas e 13.058 revogadas.
