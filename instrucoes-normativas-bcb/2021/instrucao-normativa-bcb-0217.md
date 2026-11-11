---
titulo: "Instrução Normativa BCB N° 217"
orgao: "Banco Central do Brasil"
tipo: "Instrução Normativa BCB"
numero: "217"
data: 2021-12-23
ementa: "Divulga a versão 1.8 do Manual das Interfaces de Comunicação, que compõe o Regulamento do Pix."
revogada: true
responsavel: "DECEM"
versao_texto: "texto do portal do BCB"
versao_normativo: "2"
publicacao: "Publicada no DOU de 24/12/2021, Seção 1, p. 126."
atualizacoes: ["Instrução Normativa BCB nº 302/2022 - Revogação total a partir de 1º/10/2022, produzindo efeitos a partir de 1º/2/2023."]
normas_vinculadas: ["INSTRUÇÃO NORMATIVA BCB 302/2022", "RESOLUÇÃO BCB 1/2020"]
referencias: ["Portaria BCB nº 84.287/2015, Anexo (Regimento Interno do BCB), arts. 23, inciso I, “a”; e 97-A.", "Resolução BCB nº 1/2020, Regulamento anexo, art. 2º, inciso VIII."]
fonte: "https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Instru%C3%A7%C3%A3o%20Normativa%20BCB&numero=217"
baixado_em: 2026-11-10
---
# Instrução Normativa BCB N° 217

INSTRUÇÃO NORMATIVA BCB Nº 217, DE 23 DE DEZEMBRO DE 2021

[Documento
normativo revogado, a partir de 1º/10/2022, pela Instrução Normativa BCB nº
302, de 9/9/2022, produzindo efeitos a partir de 1º/2/2023.](https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Instru%C3%A7%C3%A3o%20Normativa%20BCB&numero=302)

Divulga a
versão 1.8 do Manual das Interfaces de Comunicação,
que compõe o Regulamento do Pix.

O Chefe do Departamento de Competição e de Estrutura do Mercado Financeiro (Decem), no uso das atribuições que lhe conferem os arts. 23, inciso I, alínea “a”, e 97-A do Regimento Interno do Banco Central do Brasil, anexo à Portaria nº 84.287, de 27 de fevereiro de 2015, tendo em vista o disposto no art. 2º, inciso VIII, do Regulamento anexo à Resolução BCB nº 1, de 12 de agosto de 2020,

R E S O L V E :

Art. 1º  Esta Instrução Normativa divulga a versão 1.8 do Manual das Interfaces de Comunicação, que compõe o Regulamento do Pix, conforme art. 2º do Regulamento anexo à Resolução BCB nº 1, de 12 de agosto de 2020.

Parágrafo único.  O Manual das Interfaces de Comunicação está disponível no endereço eletrônico do Banco Central do Brasil na internet, na página destinada aos manuais que compõem o Regulamento do Pix: <https://www.bcb.gov.br/content/estabilidadefinanceira/cedsfn/Manual%20das%20Interfaces%20de%20Comunicacao-1.8.pdf>

Art. 2º  Esta Instrução Normativa entra em vigor na data da sua publicação.

Carlos Eduardo de Andrade Brandt Silva
Chefe do Departamento de Competição e de Estrutura do Mercado Financeiro, substituto

ANEXO À INSTRUÇÃO NORMATIVA BCB Nº 217, DE 23 DE DEZEMBRO DE 2021
Manual das Interfaces de Comunicação Versão 1.8

Histórico de revisão

|  |  |  |
| --- | --- | --- |
| Data | Versão | Descrição das alterações |
| 14/11/2019 | 1.0 | Versão inicial. |
| 17/01/2020 | 1.1 | Conectividade:  - Inclusão de referência ao Manual de Redes da RSFN;  - Atualização do link para o Manual de Segurança RSFN;  - Detalhamento do comportamento do DNS.  Endpoints:  - Mudança da URL base de produção e inclusão da URL de homologação;  Endpoint Entrada:  - Esclarecimento sobre idem potência no envio de mensagens duplicadas.  Endpoint Saída:  - Esclarecimento sobre interrupção.  Diversos:  - Cabeçalhos SPI-ResourceId e SPI-PullNext alterados para PI-ResourceId e PI-PullNext. |
| 17/02/2020 | 1.2 | Incluída a interface do DICT.  Renomeado o arquivo de “Manual da Interface de Comunicação” para “Manual das Interfaces de Comunicação”. |
| 28/07/2020 | 1.3 | Retiradas referências ao documento de especificações e alterado o título e nome do arquivo.  DICT: Modificada a sessão do DICT para referenciar assinatura de mensagens.  ICOM:  - Remoção de “Transfer-Encoding: gzip, chunked” para envio compactado. Recomendação de uso de “ContentEncoding” para essa finalidade;  - Admitidos novos cabeçalhos;  - Adoção de envio e recebimento de múltiplas mensagens em uma mesma requisição (multipart);  - Incluído o endpoint Catálogo: versões das mensagens aceitas e enviadas pela API;  - Remoção da seção “Pendências”.  ARQ: incluída documentação sobre o serviço de transferência de arquivos. |
| 12/08/2020 | 1.4 | Alterado padrão visual.  Adicionada seção com dicas para melhoria de desempenho na leitura de mensagens em situação de carga.  Alteração nas portas HTTPS para os serviços ICOM e ARQ. |
| 19/08/2020 | 1.5 | Correção na documentação de PI-ResourceId nos casos de requisições multipart no endpoint de saída. |
| 06/10/2020 | 1.6 | API ARQ: informação sobre uso de cabeçalhos ETag, “ETag”, “Last-Modified”, “If-None-Match” e “If-ModifiedSince”.  Cabeçalho Host deverá ser enviado sem a porta (ICOM, DICT e ARQ). |
| 14/10/2020 | 1.7 | Criação da seção 2.2.1.5 - Limitação da Quantidade Máxima de Transações Agendadas por Unidade de Tempo.  Ajuste pontual na definição do PI-Resource-ID, na seção 2.2.1.3. |
| 30/04/2021 | 1.8 | Criação da seção 2.2.1.6 – Limitação de Tráfego de Mensagens e Operações. |

NOTA

O Decreto nº 10.411, de 30 de junho de 2020, prevê a obrigatoriedade da realização de análise de impacto regulatório (AIR) para a edição de atos normativos de interesse geral produzidos pelos órgãos e entidades da administração pública federal direta e indireta.

Todavia, consoante se definiu no parágrafo 8 do Voto 280/2021–BCB, de 10 de novembro de 2021, o Regulamento do Pix, inclusive os demais documentos que o integram ou que o detalham e complementam, não se caracterizam como ato regulatório de força cogente, ostentando, em verdade, natureza eminentemente contratual; assim, modificações promovidas no referido regulamento e nos demais documentos que o integram ou que o detalham e complementam não se sujeitam à produção prévia de análise de impacto regulatório (AIR).

Dessa forma, fica a presente Instrução Normativa dispensada da prévia produção de AIR.

Carlos Eduardo de Andrade Brandt Silva
Chefe do Departamento de Competição e de Estrutura do Mercado Financeiro, substituto
