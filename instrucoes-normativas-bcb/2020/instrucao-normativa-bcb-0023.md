---
titulo: "Instrução Normativa BCB N° 23"
orgao: "Banco Central do Brasil"
tipo: "Instrução Normativa BCB"
numero: "23"
data: 2020-10-06
ementa: "Divulga procedimentos a serem observados nas operações da linha de redesconto às instituições financeiras participantes diretas do Sistema de Pagamentos Instantâneos (SPI), de que trata a Resolução BCB nº 20, de 1º de outubro de 2020."
revogada: true
responsavel: "DEBAN"
versao_texto: "texto do portal do BCB"
versao_normativo: "2"
publicacao: "Publicada no DOU de 8/10/2020, Seção 1, p. 38."
atualizacoes: ["Instrução Normativa BCB nº 234/2022 - Revogação total, a partir de 1º/3/2022."]
normas_vinculadas: ["INSTRUÇÃO NORMATIVA BCB 234/2022", "RESOLUÇÃO BCB 20/2020"]
referencias: ["Portaria nº 84.287/2015, Anexo (Regimento Interno do BCB), art. 23, inciso I, “a”; art. 111, inciso V, “d”; art. 112, inciso I, “c”; e art. 114, inciso IV.", "Resolução BCB nº 20/2020."]
fonte: "https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Instru%C3%A7%C3%A3o%20Normativa%20BCB&numero=23"
baixado_em: 2026-11-10
---
# Instrução Normativa BCB N° 23

INSTRUÇÃO NORMATIVA BCB Nº 23, DE 6 DE OUTUBRO DE 2020

[Documento normativo revogado, a partir
de 1º/3/2022, pela Instrução Normativa BCB nº 234, de 15/2/2022.](https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Instru%C3%A7%C3%A3o%20Normativa%20BCB&numero=234)

Divulga procedimentos a serem
observados nas operações da linha de redesconto às instituições financeiras
participantes diretas do Sistema de Pagamentos Instantâneos (SPI), de que trata
a Resolução BCB nº 20, de 1º de outubro de 2020.

O Chefe do Departamento de Operações
Bancárias e de Sistema de Pagamentos (Deban) e o Chefe do Departamento de
Operações do Mercado Aberto (Demab), no uso das atribuições que lhes conferem o
art. 111, inciso V, alínea “d”, o art. 112, inciso I, alínea “c”, o art. 114,
inciso IV, e o art. 23, inciso I, alínea “a”, do Regimento Interno do Banco
Central do Brasil, anexo à Portaria nº 84.287, de 27 de fevereiro de 2015, e
tendo em conta o disposto na Resolução BCB nº 20, de 1º de outubro de 2020,

R E S O L V E M :

Art. 1º  Esta Instrução Normativa
divulga procedimentos operacionais a serem observados nas operações da linha de
redesconto, de que trata a Resolução BCB nº 20, de 1º de outubro de 2020,
concedida pelo Banco Central do Brasil às instituições financeiras
participantes diretas do Sistema de Pagamentos Instantâneos (SPI), titulares de
Conta Pagamentos Instantâneos (Conta PI) no Banco Central do Brasil.

Art. 2º  O preço de compra pelo Banco
Central do Brasil, de que trata o art. 2º, § 2º, inciso I, da Resolução BCB nº
20, de 2020, é o divulgado diariamente por meio do arquivo ASEL006 - Preço de
lastro de títulos (preço unitário da 550) na página do Banco Central do Brasil
na internet.

Parágrafo único.  Os títulos públicos
federais que são aceitos nas referidas operações de redesconto são aqueles
constantes do arquivo ASEL006, de que trata o **caput**, exceto os títulos
que possuam pagamento de eventos (resgate, juros ou amortização) coincidente
com o vencimento da operação.

Art. 3º  O registro da solicitação de
operação, de que trata o art. 3º da Resolução BCB nº 20, de 2020, é realizado
por meio da mensagem SEL1009 (IF requisita liquidez em Conta PI) do Grupo de
Serviços SEL, do Catálogo de Serviços do SFN, enviada pela instituição
financeira ao Selic.

Parágrafo único.  Enquanto permanecer
retido no Selic, o registro de solicitação poderá ser cancelado pela
instituição financeira, por meio do envio ao Selic da mensagem SEL1400
(Participante requisita Cancelamento de registro de operação) do Grupo de
Serviços SEL, do Catálogo de Serviços do SFN, durante o horário regular de
operações no STR.

Art. 4º  A operação de recompra pela
instituição financeira, de que trata o art. 5º da Resolução BCB nº 20, de 2020,
é solicitada por meio do envio da mensagem SEL1016 (IF requisita pagamento de
liquidez em Conta PI) do Grupo de Serviços SEL, do Catálogo de Serviços do SFN,
pela instituição financeira ao Selic.

Art. 5º  O preço de revenda e o valor
financeiro das operações são calculados observada a metodologia descrita no
Anexo I desta Instrução Normativa.

Art. 6º  Esta Instrução Normativa
entra em vigor em 3 de novembro de 2020.

Flávio Túlio
Vilela                                                André de Oliveira Amante
                        Chefe do
Departamento de                              Chefe do Departamento de Operações
                        Operações Bancárias
e de Sistema                 do Mercado Aberto
                        de
Pagamentos

ANEXO I À INSTRUÇÃO NORMATIVA Nº 23,
DE 6 DE OUTUBRO DE 2020.

METODOLOGIA DE CÁLCULO

I - Valor financeiro da compra pelo
Banco Central do Brasil

Vcompra =
Quantidade títulos compra x PUcompra

Em que:

- Vcompra
corresponde ao valor financeiro da compra pelo Banco Central do Brasil expresso
com duas casas decimais, abandonando-se da terceira em diante;

- Quantidade títulos
compra  corresponde à quantidade de títulos (número inteiro) da operação que
está sendo contratada; e

- PUcompra corresponde
ao preço unitário de compra do título pelo Banco Central do Brasil para a data
da contratação da operação, de que trata o art. 2º desta Instrução Normativa,
com 8 casas decimais.

II – Preço de revenda

PUrevenda =
PUCompra  x  ( 1 + (((1 + TaxaSelic)^(1/252) - 1) x percentual))

Em que:

- PUrevenda
corresponde ao preço unitário de revenda pelo Banco Central do Brasil de que
trata o art. 2º, §2º, inciso II, da Resolução BCB nº 20, de 2020, com 8 casas
decimais arredondado matematicamente;

- PUcompra
corresponde ao preço unitário de compra do título pelo Banco Central do Brasil
para a data da contratação da operação, de que trata o art. 2º desta Instrução
Normativa, com 8 casas decimais;

- TaxaSelic corresponde
à Taxa Selic (% a.a.) apurada para o dia da contratação da operação, divulgada
diariamente na página do Banco Central do Brasil na internet; e

- percentual
corresponde ao percentual da Taxa Selic, fixado no art. 2º, § 2º, inciso II, da
Resolução BCB nº 20, de 2020, válido na data da contratação da operação.

Observação: O termo
"(1+ TaxaSelic)^(1/252)" corresponde ao fator diário da Taxa Selic,
arredondado em oito casas decimais, conforme divulgação diária na página do
Banco Central do Brasil na internet.

III – Valor financeiro da recompra
pela instituição financeira

Vrecompra =
Quantidade títulos recompra x PUrevenda

Em que:

- Vrecompra
corresponde ao valor financeiro da recompra pela instituição financeira
expresso com duas casas decimais, abandonando-se da terceira em diante;

- Quantidade títulos
recompra corresponde à quantidade de títulos (número inteiro) que estão sendo
recomprados pela instituição financeira;

- PUrevenda
corresponde ao preço unitário de revenda calculado na forma do item II deste
Anexo.

Observação: em função
das características de formação dos valores financeiros das operações, pode
haver resíduo financeiro no caso de liquidação parcelada, pois a soma das
parcelas financeiras decorrentes das relações PU x Quantidade, decorrente da
truncagem dos valores, poderá não corresponder ao produto PU x Quantidade
Total, devendo eventual resíduo ser ajustado quando do pagamento da última
parcela. Dessa forma, quando o compromisso de recompra for honrado em parcelas,
o valor financeiro da recompra da última parcela será o saldo financeiro da
operação antes do pagamento desta última parcela, podendo não corresponder ao
produto da quantidade de títulos pelo preço unitário de revenda.

IV – Saldo financeiro da operação

Saldo = Vcompra
+ Encargos – (Vrecompra1 + Vrecompra2 + Vrecompra3...)

Em que:

- Saldo corresponde ao
saldo financeiro da operação;

- Vcompra
corresponde ao valor financeiro da compra pelo Banco Central do Brasil
calculado na forma do item I deste Anexo;

- Encargos corresponde
a ((Quantidade títulos compra x PUrevenda) - Vcompra);

- (Vrecompra1
+ Vrecompra2 + Vrecompra3...) corresponde ao somatório
dos valores financeiros das recompras parciais pela instituição financeira,
calculados na forma do item III deste Anexo, efetivadas para a operação.

Observação: o produto
Quantidade títulos compra x PUrevenda utilizado na apuração dos
encargos é expresso com duas casas decimais, abandonando-se da terceira em
diante.
