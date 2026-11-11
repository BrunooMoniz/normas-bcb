---
titulo: "COMUNICADO N. 004073"
orgao: "Banco Central do Brasil"
tipo: "Comunicado"
numero: "4073"
data: 1994-08-02
ementa: "Sistema de Registro de Operacoes de Credito com o Setor Publico - Transacao PDIP500 do SISBACEN - Instrucoes adicionais para o re- gistro de dados referentes a segunda etapa de implantacao do Sistema"
revogada: false
responsavel: "SECRE"
versao_texto: "texto do portal do BCB"
fonte: "https://www.bcb.gov.br/estabilidadefinanceira/exibeoutrasnormas?tipo=Comunicado&numero=4073"
baixado_em: 2026-11-10
---
# COMUNICADO N. 004073

```
                        COMUNICADO N. 004073
                        --------------------

                         Sistema  de Registro de Operacoes de Credito
                         com  o Setor Publico - Transacao PDIP500  do
                         SISBACEN  - Instrucoes adicionais para o re-
                         gistro  de dados referentes a segunda  etapa
                         de implantacao do Sistema

                    Com  base  no  art. 7. da Circular n.  2.367,  de
23.09.93, comunicamos que:

a) as  informacoes financeiras relativas as Opcoes "Movimento da Ope-
   racao"  e  "Informacoes Mensais" devem, obrigatoriamente, ser  ex-
   pressas na moeda nacional vigente a epoca da efetiva ocorrencia do
   evento;

b) o  campo  "Taxa" da tela de "Movimentacao de Pagamento"  deve  ser
   preenchido com a taxa de juros efetivamente cobrada, expressa sem-
   pre em percentagem ao mes;

c) as  "Informacoes Mensais" poderao ser prestadas a partir dos dados
   relativos ao mes de junho de 1.994;

d) o campo "Saldo Devedor Medio" que integra a Tela 11 - "Informacoes
   Mensais",  cujo preenchimento e exigido apenas para as modalidades
   01  -  "Adiantamentos a Depositantes, exceto os de cambio" e 36  -
   "Credito Rotativo", deve ser preenchido com o resultado da divisao
   do  somatorio  dos  saldos devedores diarios pelo numero  de  dias
   uteis do mes, considerando-se como zero os saldos credores ocorri-
   dos no mes, mediante a aplicacao da seguinte formula:

                         n
                         E  SD
                        i=1    i
               SDM = -------------
                            n

               onde:

                    SDM = Saldo Devedor Medio

                    E   = Simbolo de Somatorio

                    SD  = Saldo Devedor no  i-esimo dia util do  mes
                      i   que  deve ser tomado como zero para os sal-
                          dos  em conta corrente iguais ou superiores
                          a zero

                    n   = numero de dias uteis no mes

e) o  campo "Taxa Media Mensal" que integra a Tela 11 -  "Informacoes
   Mensais",  cujo preenchimento e exigido apenas para as modalidades
   01  -  "Adiantamentos a Depositantes, exceto os de cambio" e 36  -
   "Credito  Rotativo", deve ser preenchido com a media ponderada das
   taxas cobradas sobre cada saldo devedor diario, tendo como base de
   ponderacao  o proprio saldo devedor diario, devendo ser, obrigato-
   riamente, expressa em percentagem ao mes e calculada pela seguinte
   formula:

                         n
                         E   SD . t
                        i=1    i   i   n
               TMM =((----------------)  - 1)  * 100
                            n
                            E  SD
                           i=1    i

               onde:

                    TMM = Taxa Media Mensal

                    E   = Simbolo de Somatorio

                    SD  = Saldo Devedor no  i-esimo dia util do  mes
                      i   que  deve  tomado como zero  para os saldos
                          em  conta  corrente iguais ou superiores  a
                          zero

                    t   = Taxa de Juros ao dia praticada  no i-esimo
                     i    dia util do mes expressa em valores absolu-
                          tos acrescido da unidade

                    n   = numero de dias uteis no mes:

f) o  campo "Indexada (S/N)", da tela 02 - Cadastro da Operacao, deve
   ser preenchido, obedecendo o que  segue:

   I) com  "S"  (Sim) se, e somente se, a taxa de juros informada  no
      campo "Taxa", da mesma tela, "embutir" o componente de correcao
      monetaria,  o que caracteriza uma operacao com taxas  pre-fixa-
      das:

  II) com  "N"  (Nao) se, e somente se, a taxa de juros informada  no
      campo "Taxa", da mesma tela, "nao embutir" o componente de cor-
      recao  monetaria, o que caracteriza uma operacao com taxas pos-
      fixadas:

g) o  campo "Indice de Atualizacao", da tela 02 - Cadastro da  Opera-
   cao,  deve  ser preenchido somente naqueles casos em que  o  campo
   "Indexada (S/N)", da mesma tela, tiver sido preenchido com "N", de
   modo a permitir a identificacao do indexador utilizado;

2.                  Em virtude das consultas que vem sendo formuladas
pelas  Instituicoes  Financeiras acerca dos procedimentos para a  im-
plantacao  da  segunda etapa do SISDEDIP, esclarecemos que, antes  de
dar  inicio a entrada dos dados e informacoes requeridos nesta etapa,
e imprescindivel a consulta as instrucoes contidas nas telas de ajuda
disponiveis na transacao PDIP500.

3.                  O  primeiro conjunto de telas de ajuda contem in-
formacoes  gerais sobre os objetivos, funcionamento e as rotinas dis-
poniveis  no  SISDEDIP. O acesso  a esse grupo de telas e possivel  a
partir  da primeira tela do Sistema: "Menu de Opcoes", bastando acio-
nar  a  tecla  F1 e proceder sua impressao por  intermedio  de  "hard
copy".

4.                  As demais telas de ajuda sao especificas para ca-
da rotina do Sistema,  determinadas pelas combinacoes entre "Opcao" e
"Acao"  da  Tela 01 - Menu de Opcoes. Cada uma dessas telas de  ajuda
contem  informacoes sobre o objetivo daquela rotina e descreve o con-
teudo  e  operacionalizacao de cada um dos campos que compoem a  tela
destinada  a entrada de dados. Essas telas de ajuda podem ser aciona-
das  a partir das telas de entrada de dados de cada rotina,  bastando
acionar  a tecla F1 e proceder sua impressao por intermedio de  "hard
copy".

5.                  A fim de racionalizar e agilizar os procedimentos
requeridos  para a entrada dos dados relativos a segunda etapa de im-
plementacao  do Sistema, ate que seja emitido normativo alterando  os
prazos estabelecidos na Circular n. 2.367, de 23.09.93, para registro
das informacoes no Sistema, recomenda-se que seja observada a seguin-
te sequencia de rotinas:

a) "Cadastramento  da  Operacao", quando da contratacao de  uma  nova
   operacao;

b) "Movimento da Operacao", de acordo com as liberacoes ou pagamentos
   efetivamente ocorridos;

c) "Informacoes  Mensais", referente a cada mes de vigencia da opera-
   cao;

d) "Cessao  de Credito", "Aquisicao de Credito", "Renovacao", "Repac-
   tuacao"" e "Renegociacao", acompanhadas das respectivas movimenta-
   coes  que tenham efetivamente ocorrido e das informacoes  mensais,
   de cada uma das operacoes de credito resultante;

e) "Situacao da Operacao".

6.                  Para  a entrada dos dados relativos as rotinas de
"Movimento  da Operacao - Liberacao ou Pagamento" existem duas alter-
nativas:

a) as  informacoes das movimentacoes poderao ser prestadas individua-
   lizadamente por parcela de liberacao ou de pagamento, bastando que
   seja  indicado nos campos "Parcela Inicial" e "Parcela Final",  da
   "Tela  01 - Menu de Opcoes", o mesmo numero de parcela, ou seja, o
   numero especifico da parcela da qual se deseja registrar as infor-
   macoes de movimentacao;

b) as  informacoes das movimentacoes poderao ser prestadas de maneira
   agregada  por  grupo de parcelas, bastando que os campos  "Parcela
   Inicial"  e "Parcela Final", da "Tela 01 - Menu de Opcoes",  sejam
   preenchidos com os numeros das parcelas que delimitam o respectivo
   grupo de parcelas. Essa alternativa ficara disponivel apenas ate o
   dia  31.08.1994. A utilizacao dessa segunda alternativa implica na
   adocao de alguns cuidados especiais, explicitados a seguir;

c) a  adocao da alternativa "b" pressupoe que a movimentacao das par-
   celas  sejam integrais, ou seja, o sistema registra tal  condicao,
   nao  aceitando  movimentacoes parciais das parcelas  incluidas  no
   grupo de parcelas;

d) ao  selecionar-se a alternativa "b"  deve se ter o cuidado de  re-
   gistrar  corretamente os numeros das parcelas que delimitam o gru-
   po,  nos campos "Parcela Inicial" e "Parcela Final", da Tela 01  -
   Menu  de Opcoes, pois o grupo de parcelas, a partir de entao e to-
   mado como fixo. O sistema abrira apenas uma unica tela para regis-
   tro  dos dados de movimentacao, a qual somente podera ser alterada
   em  seus campos que contem valores financeiros, nao sendo possivel
   a  alteracao dos numeros que identificam as parcelas inicial e fi-
   nal;

f) caso  a identificacao dos numeros das "Parcela Inicial" e "Parcela
   Final" tenham sido registrados de maneira equivocada, deve ser so-
   licitado  ao Departamento da Divida Publica - DEDIP o cancelamento
   da referida Movimentacao, atraves de correspondencia informando:

               - NUMERO BACEN da Operacao de Credito
               - CGC DO CREDOR
               - CGC DO TOMADOR
               - NUMERO  DA PARCELA INICIAL, pertencente ao grupo  de
                 parcelas identificado de maneira equivocada
               - NUMERO  DA  PARCELA FINAL, pertencente ao  grupo  de
                 parcelas identificado de maneira equivocada.

7.                  O  acompanhamento  do registro de informacoes  no
SISDEDIP pode ser efetuado por intermedio da Transacao PDIP550 que se
encontra  disponivel as Instituicoes Financeiras e Sociedades de  Ar-
rendamento Mercantil desde o dia 26.04.94.

8.                  Por  fim, esclarecemos que as Instituicoes Finan-
ceiras  que nao mantinham operacoes de credito com Orgaos e Entidades
do  Setor Publico, em 23.09.93, e continuam nao operando com tais Or-
gaos e Entidades, devem informar uma unica vez ao DEDIP - Departamen-
to  da Divida Publica sobre tal situacao, de acordo com o  solicitado
no  Comunicado  3.567, de 28.10.93, nao sendo necessaria a  repeticao
mensal dessa informacao.

                    Brasilia (DF), 29 de julho de 1994

                    DEPARTAMENTO DA DIVIDA PUBLICA - DEDIP

                    Jairo da Cruz Ferreira
                    Chefe, em exercicio

Obs.: Republicado por ter havido incorrecao na data do Comunicado.
```
