---
titulo: "COMUNICADO N. 004637"
orgao: "Banco Central do Brasil"
tipo: "Comunicado"
numero: "4637"
data: 1995-06-21
ementa: ""
revogada: false
responsavel: "DEPIN"
versao_texto: "texto do portal do BCB"
fonte: "https://www.bcb.gov.br/estabilidadefinanceira/exibeoutrasnormas?tipo=Comunicado&numero=4637"
baixado_em: 2026-11-10
---
# COMUNICADO N. 004637

```
                        COMUNICADO N. 004637
                        --------------------

AS INSTITUICOES AUTORIZADAS A OPERAR EM CAMBIO

                                 INSTITUI  SISTEMATICA  DE LEILAO  DE
                                 COMPRA  E/OU VENDA DE MOEDA  ESTRAN-
                                 GEIRA  (LEILAO DE "SPREAD") E ALTERA
                                 O  NUMERO DE "DEALERS"  CREDENCIADOS
                                 PELO BANCO CENTRAL DO BRASIL.

               LEVAMOS AO SEU CONHECIMENTO QUE:

               I - ADICIONALMENTE A ATUAL SISTEMATICA DE LEILOES ELE-
TRONICOS  DE COMPRA OU DE VENDA DE MOEDA ESTRANGEIRA, O BANCO CENTRAL
DO  BRASIL PODERA REALIZAR LEILAO EM QUE SOLICITARA COTACOES SIMULTA-
NEAS  TANTO  PARA  COMPRA  COMO  PARA VENDA  DE  DIVISAS  (LEILAO  DE
"SPREAD").

               II - NESSA MODALIDADE DE LEILAO, TODAS AS INSTITUICOES
CREDENCIADAS  COMO "DEALERS" PARTICIPARAO OFERECENDO, OBRIGATORIAMEN-
TE, COTACOES DE COMPRA E DE VENDA DA MOEDA ESTRANGEIRA.

               III - O BANCO CENTRAL DO BRASIL PASSARA, A PARTIR DES-
TA  DATA,  A ATUAR NOS MERCADOS DE CAMBIO DE TAXAS LIVRES E DE  TAXAS
FLUTUANTES  COM  O NUMERO DE 60 (SESSENTA)  INSTITUICOES  FINANCEIRAS
CREDENCIADAS COMO "DEALERS".

               IV - ENCONTRA-SE ANEXO ROTEIRO DESCRITIVO DOS PROCEDI-
MENTOS  OPERACIONAIS A SEREM ADOTADOS QUANDO DA REALIZACAO DE LEILOES
PELO BANCO CENTRAL DO BRASIL.

                             BRASILIA (DF), 21 DE JUNHO DE 1995

                             DEPARTAMENTO DE OPERACOES DAS
                             RESERVAS INTERNACIONAIS

                             JOUBERT FURTADO
                             CHEFE

               ANEXO AO COMUNICADO DEPIN DE 21.06.95

               I  - A realizacao dos "leiloes eletronicos de  cambio"
se da atraves das seguintes transacoes, integrantes do SISBACEN:

               a) Para uso exclusivo dos "dealers":

                  -PLEI650 - Registro de Propostas do Leilao - Insti-
                             tuicoes Financeiras.

               b) Para uso de todas as instituicoes financeiras auto-
                  rizadas a operar em cambio:

                  -PLEI655 - Consulta a Leiloes - Instituicoes Finan-
                             ceiras.

               II  -  A Instituicao Financeira devera credenciar  sua
matriz  para operar na Transacao PLEI650, observado que, na  hipotese
de  eventual impedimento da mesma para participar de qualquer leilao,
devera a Instituicao faze-lo por intermedio de qualquer outra de suas
dependencias. Nessa hipotese, as operacoes serao sempre registradas e
liquidadas, no SISBACEN, em nome da matriz.

               III - As mensagens correspondentes as varias etapas da
realizacao dos leiloes eletronicos serao exibidas nas duas linhas su-
periores  da tela da Transacao PCOT700 - Taxas Praticadas no  Mercado
Interbancario, aparecendo na parte superior esquerda quando se trata-
rem  de leiloes no segmento de taxas livres (comercial) e/ou na parte
superior direita quando no segmento de taxas flutuantes, a saber:

               a) Aviso de leilao:

               Mensagem: AV.BACEN.LEILAO  DE MOEDAS XXX          onde
                         XXX  =  COM, se no segmento de taxas  livres
                         (comercial),  ou XXX = FLU se no segmento de
                         taxas flutuantes.

               b) Caracteristicas do leilao:

               Mensagem: X Y N hh:mm:ss/HH:MM:SS
                         onde:  X  =  C  (compra),  V  (venda)  ou  S
                         ("spread");  Y = C (comercial) ou F (flutan-
                         te); N = numero de propostas (de 1 a 5); hh:
                         mm:ss  =  hora inicio do leilao; HH:MM:SS  =
                         hora fim do leilao. Tal mensagem ficara dis-
                         ponivel  ate a hora fim, quando sera substi-
                         tuida pela seguinte mensagem:
                         XXX-AA/NNNN EM APURACAO
                         onde XXX = COM ou FLU, AA/NNNN = ano e nume-
                         ro do leilao.

               c) Resultado do leilao de compra ou de venda:

               Mensagem: X YYY AA/NNNN TT.TTTT/PPP
                         onde:  X  =  C  (compra),  V  (venda)  ou  S
                         ("spread");  YYY  = COM (comercial)  ou  FLU
                         (flutuante);  AA/NNNN = ano e numero do lei-
                         lao; TT.TTTT/PPP = taxa de compra ou de ven-
                         da e percentual de corte.

               d) Resultado do leilao de "spread":

               Mensagem: NNNN TTT.TTTT/PPP ttt.tttt/ppp
                         onde: NNNN  = numero do leilao; TTT.TTTT/PPP
                         = taxa de compra e percentual de corte; ttt.
                         tttt//ppp  =  taxa de venda e percentual  de
                         corte.

               IV  - As propostas deverao ser registradas pelos "dea-
lers" levando-se em conta o ponto de vista do Banco Central, ou seja,
as taxas de compra e/ou de venda do Banco Central correspondem as ta-
xas de venda e/ou de compra do "Dealer", respectivamente.

                V - Ao receber a mensagem das caracteristicas do lei-
lao (alinea "B" do item III deste roteiro), o "dealer" devera acessar
a  transacao PLEI650 (opcao 1) para proceder a inclusao de suas  pro-
postas, atentando especialmente para o fato de que:

               a)  no leilao de "spread" o Banco Central informara  a
diferenca maxima aceitavel entre as taxas de compra e de venda,

               b)  o valor em moeda estrangeira do lote minimo encon-
tra-se expresso em milhares de unidades;

               c)  o campo relativo a quantidade de moeda estrangeira
devera ser preenchido em milhares de unidades;

               d) as propostas, ate atingirem o numero maximo estabe-
lecido  para o leilao, observada a hora de termino do evento, poderao
ser incluidas individualmente ou em grupo;

               e) o total em moeda nacional, de preenchimento obriga-
torio, constitui fator de seguranca para que o "dealer" possa confir-
mar  o valor de suas propostas em moeda estrangeira. Estando corretos
os valores, o sistema solicitara, automaticamente, mediante mensagens
na tela, dois niveis de confirmacao das propostas apresentadas;

               f)  nao obstante o disposto na alinea anterior, podera
o  "dealer", apos o primeiro nivel de confirmacao, cancelar integral-
mente  as suas propostas, mediante o retorno a tela inicial para,  se
do seu interesse, reiniciar a operacao de preenchimento de dados;

               g)  caso  o "dealer" ingresse na tela com o numero  de
propostas superior ao fixado pelo Banco Central para o leilao, o sis-
tema emitira mensagem de erro que permitira a eliminacao de quaisquer
das  propostas oferecidas e ainda nao confirmadas,  independentemente
da posicao do cursor no momento da mensagem de rejeicao;

               h)  uma  vez confirmada a inclusao das propostas  pelo
"dealer"  e, portanto, registradas em carater definitivo no  sistema,
serao as mesmas consideradas definitivas e irretrataveis; e

               i) o campo "instrucoes de pagamento" devera ser preen-
chido  pelo "dealer" somente nos casos de leiloes de venda ou de lei-
loes  de "spread" em que ocorra venda, pelo Banco Central,  hipoteses
em que devera ser informado o codigo indicativo das instrucoes de pa-
gamento.

               VI - A nao apresentacao de propostas ou a tentativa de
confirmacao das mesmas apos a hora do termino do leilao ficara regis-
trada no sistema com a correspondente mensagem estampada na tela.

               VII  - Na hipotese de nao apresentacao de proposta por
parte  de qualquer "dealer" em leilao onde o Banco Central tenha efe-
tivamente  comprado  e/ou vendido, sera considerada sua  participacao
pelo  lote minimo do leilao, aplicada a taxa menos favoravel ao "dea-
ler",  ou  seja, a menor taxa nos leiloes de compra e a maior nos  de
venda.

               VIII  - Alem da opcao relativa a inclusao de propostas
no  sistema, dispoe a transacao PLEI650 de duas outras opcoes de con-
sulta  a dados relativos a proposta do proprio "dealer" e a dados ge-
nericos dos leiloes promovidos pelo Banco Central.

               IX  - Uma vez aceitas as propostas pelo Banco Central,
os contratos de cambio pertinentes serao gerados automaticamente pelo
SISBACEN na data da contratacao.

               X - Os valores em moeda nacional correspondentes a li-
quidacao das operacoes mencionadas no item anterior serao automatica-
mente  debitados/creditados na conta "Reservas Bancarias" das  insti-
tuicoes contratantes, observadas as normas em vigor.

               XI  - Eventuais duvidas que a utilizacao do sistema de
"leilao  eletronico  de cambio" possa suscitar poderao ser  dirimidas
junto a Mesa de Cambio do DEPIN, pelo telefone (061) 321-7477.
```
