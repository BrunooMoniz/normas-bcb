---
titulo: "Instrução Normativa BCB N° 367"
orgao: "Banco Central do Brasil"
tipo: "Instrução Normativa BCB"
numero: "367"
data: 2023-03-31
ementa: "Divulga a versão 1.11 do Manual das Interfaces de Comunicação, que compõe o Regulamento do Pix."
revogada: true
responsavel: "DECEM"
versao_texto: "texto do portal do BCB"
versao_normativo: "2"
publicacao: "Publicada no DOU de 4/4/2023, Seção 1, p. 95."
atualizacoes: ["Instrução Normativa BCB nº 695/2025 - Revogação total."]
normas_vinculadas: ["INSTRUÇÃO NORMATIVA BCB 695/2025", "INSTRUÇÃO NORMATIVA BCB 225/2022", "RESOLUÇÃO BCB 1/2020"]
referencias: ["Portaria BCB nº 84.287/2015, Anexo (Regimento Interno do BCB), arts. 23, inciso I, \"a\"; e 97-A.", "Resolução BCB nº 1/2020, Regulamento anexo, art. 2º.", "Revoga, a partir de 29/10/2023, Instrução Normativa BCB nº 225/2022."]
fonte: "https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Instru%C3%A7%C3%A3o%20Normativa%20BCB&numero=367"
baixado_em: 2026-11-10
---
# Instrução Normativa BCB N° 367

INSTRUÇÃO NORMATIVA
BCB Nº 367, DE 31 DE MARÇO DE 2023

[Documento
normativo revogado pela Instrução Normativa BCB nº 695, de 23/12/2025.](https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Instru%C3%A7%C3%A3o%20Normativa%20BCB&numero=695)

Divulga a versão 1.11 do Manual das Interfaces de Comunicação, que
compõe o Regulamento do Pix.

O Chefe do Departamento
de Competição e de Estrutura do Mercado Financeiro (Decem), no uso das
atribuições que lhe conferem os arts. 23, inciso I, alínea “a”, e 97-A do
Regimento Interno do Banco Central do Brasil, anexo à Portaria nº 84.287, de 27
de fevereiro de 2015, tendo em vista o disposto no art. 2º, inciso VIII, do
Regulamento anexo à Resolução BCB nº 1, de 12 de agosto de 2020,

R E S O L V E :

Art. 1º  Esta Instrução Normativa
divulga a versão 1.11 do Manual das Interfaces de Comunicação, que compõe o
Regulamento do Pix, conforme art. 2º do Regulamento anexo à Resolução BCB nº 1,
de 12 de agosto de 2020.

Parágrafo único.  O Manual das
Interfaces de Comunicação está disponível no endereço eletrônico do Banco
Central do Brasil na internet: <https://www.bcb.gov.br/content/estabilidadefinanceira/cedsfn/Manual%20das%20Interfaces%20de%20Comunicacao-1.11.pdf>

Art. 2º  Fica revogada a Instrução
Normativa BCB nº 225, de 5 de janeiro de 2022.

Art. 3º  Esta Instrução Normativa
entra em vigor:

I - em 2 de maio de 2023, para as alterações referentes à seção 2.2.1.6.
do Manual das Interfaces de Comunicação, conforme descrição detalhada no Anexo
à esta Instrução Normativa;

II - em 29 de outubro de 2023, para as demais alterações.

Angelo José Mont Alverne Duarte

ANEXO À INSTRUÇÃO NORMATIVA BCB Nº 367, DE 31 DE
MARÇO DE 2023

Manual das Interfaces de Comunicação

Histórico
de revisão

|  |  |  |
| --- | --- | --- |
| Data | Versão | Descrição das alterações |
| 14/11/2019 | 1.0 | Versão inicial. |
| 17/01/2020 | 1.1 | Conectividade:  - Inclusão de referência ao Manual de Redes da RSFN;  - Atualização do link para o Manual de Segurança RSFN;  - Detalhamento do comportamento do DNS.  Endpoints:  - Mudança da URL base de produção e inclusão da URL de homologação;  Endpoint Entrada:  - Esclarecimento sobre idempotência no envio de mensagens duplicadas.  Endpoint Saída:  - Esclarecimento sobre interrupção.  Diversos:  - Cabeçalhos SPI-ResourceId e SPI-PullNext alterados para PI-ResourceId e PI-PullNext. |
| 17/02/2020 | 1.2 | Incluída a interface do DICT.  Renomeado o arquivo de “Manual da Interface de Comunicação” para “Manual das Interfaces de Comunicação”. |
| 28/07/2020 | 1.3 | Retiradas referências ao documento de especificações e alterado o título e nome do arquivo.  DICT: Modificada a sessão do DICT para referenciar assinatura de mensagens.  ICOM:  - Remoção de “Transfer-Encoding: gzip, chunked” para envio compactado. Recomendação de uso de “ContentEncoding” para essa finalidade;  - Admitidos novos cabeçalhos;  - Adoção de envio e recebimento de múltiplas mensagens em uma mesma requisição (multipart);  - Incluído o endpoint Catálogo: versões das mensagens aceitas e enviadas pela API;  - Remoção da seção “Pendências”.  ARQ: incluída documentação sobre o serviço de transferência de arquivos. |
| 12/08/2020 | 1.4 | Alterado padrão visual.  Adicionada seção com dicas para melhoria de desempenho na leitura de mensagens em situação de carga.  Alteração nas portas HTTPS para os serviços ICOM e ARQ. |
| 19/08/2020 | 1.5 | Correção na documentação de PI-ResourceId nos casos de requisições multipart no endpoint de saída. |
| 06/10/2020 | 1.6 | API ARQ: informação sobre uso de cabeçalhos ETag, “ETag”, “Last-Modified”, “If-None-Match” e “If-ModifiedSince”.  Cabeçalho Host deverá ser enviado sem a porta (ICOM, DICT e ARQ). |
| 14/10/2020 | 1.7 | Criação da seção 2.2.1.5 - Limitação da Quantidade Máxima de Transações Agendadas por Unidade de Tempo.  Ajuste pontual na definição do PI-Resource-ID, na seção 2.2.1.3. |
| 30/04/2021 | 1.8 | Criação da seção 2.2.1.6 – Limitação de Tráfego de Mensagens e Operações. |
| 04/01/2022 | 1.9 | Alteração nos valores da seção 2.2.1.5 – Limitação da quantidade máxima de transações agendadas por unidade de tempo. |
| 17/10/2022 | 1.10 | Inclusão do texto na seção 2.2.1.6. para alteração dos parâmetros de balde dos participantes, a critério do BACEN. |
| 31/03/2023 | 1.11 | - Alteração nos valores do bucket e do acréscimo de tokens na seção 2.2.1.6 – com validade a partir de 02/05/2023.  - Criação da seção 1.2 - Canais de transmissão de mensagens – com validade a partir de 29/10/2023.  - Alterações nos textos das seções 2.2, 2.2.1.5, 2.2.1.6, 2.2.2.10 para inclusão das especificações relativas ao canal secundário – com validade a partir de 29/10/2023. |

NOTA

O Decreto nº 10.411, de 30 de junho de 2020, prevê a obrigatoriedade da
realização de análise de impacto regulatório (AIR) para a edição de atos
normativos de interesse geral produzidos pelos órgãos e entidades da
administração pública federal direta e indireta.

Todavia, consoante se definiu no parágrafo 8 do Voto 280/2021–BCB, de 10
de novembro de 2021, o Regulamento do Pix, inclusive os demais documentos que o
integram ou que o detalham e o complementam, não se caracterizam como ato
regulatório de força cogente, ostentando, em verdade, natureza eminentemente
contratual. Assim, modificações promovidas no referido regulamento e nos demais
documentos que o integram ou que o detalham e o complementam não se sujeitam à
produção prévia de AIR.

O Decreto nº 10.139, de 28 de novembro de 2019, prevê que os atos
normativos devem entrar em vigor sempre no primeiro dia do mês ou em seu
primeiro dia útil. Este ato normativo dispõe que parte das alterações na versão
1.11 do Manual das Interfaces de Comunicação entrará em vigor no dia 29 de
outubro de 2023, que não é o primeiro dia do respectivo mês nem seu primeiro
dia útil. Isso se justifica por questões operacionais. Como o Pix é composto
por uma infraestrutura que funciona 24 horas por dia, em todos os dias do ano,
mudanças nessa infraestrutura devem ser realizadas em dias de menor
movimentação, para mitigar os riscos de essas mudanças afetarem o seu bom
desempenho. Os dias de menor movimentação do Pix são os domingos, razão pela
qual prevê-se que os ajustes entrem em vigor em um domingo.

Angelo José Mont Alverne Duarte
Chefe do Departamento de Competição e de Estrutura do Mercado
Financeiro
