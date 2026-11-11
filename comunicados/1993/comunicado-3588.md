---
titulo: "COMUNICADO N. 003588"
orgao: "Banco Central do Brasil"
tipo: "Comunicado"
numero: "3588"
data: 1993-11-12
ementa: "Sistema de Registro de Operacoes de Credito com o Setor Publico - Circular 2.367, de 23.09.93 - transacao PDIP500 do SISBACEN - Alteracoes das normas para o fornecimento das informacoes"
revogada: false
responsavel: "DEDIP"
versao_texto: "texto do portal do BCB"
fonte: "https://www.bcb.gov.br/estabilidadefinanceira/exibeoutrasnormas?tipo=Comunicado&numero=3588"
baixado_em: 2026-11-10
---
# COMUNICADO N. 003588

```
                        COMUNICADO N. 003588
                        --------------------
                         Sistema  de Registro de Operacoes de Credito
                         com  o  Setor Publico - Circular  2.367,  de
                         23.09.93  - transacao PDIP500 do SISBACEN  -
                         Alteracoes  das  normas para o  fornecimento
                         das informacoes

                    Comunicamos  que  foram efetuadas  alteracoes  na
transacao PDIP500, do SISBACEN, envolvendo os seguintes campos:

a) "MOEDA"  - Este campo foi alterado para cinco posicoes  numericas,
   onde  deve ser informada a moeda utilizada na realizacao da opera-
   cao de credito.

a.1) Para  o cadastramento de operacao contratada em moeda  nacional,
     ate  24.09.93, deve ser informada a respectiva moeda da epoca da
     contratacao ou,

a.2) Alternativamente, podera ser informada a moeda nacional mais re-
     cente, desde que o principal seja devidamente atualizado em seus
     valores  monetarios,  devendo nestes casos ser  obrigatoriamente
     informado no campo "MES REF", o mes, ate o qual foram corrigidos
     os  montantes  de  principal informados  nos  campos  "VLR.OPR",
     "PRINC A LIB", "PRINC A PAG";

a.3) No  calculo dos montantes atualizados, discriminados no item an-
     terior,  deve ser utilizado o indexador pactuado no contrato  ou
     aquele que o tenha substituido;

a.4) Deve  ser observado, ainda, que a moeda aqui informada sera uti-
     lizada para as demais informacoes financeiras da opcao de cadas-
     tramento, envolvendo, portanto, os Cronogramas de Liberacao e de
     Pagamento;

a.5) As  demais informacoes financeiras a serem prestadas, referentes
     as Opcoes de Movimentacao e de Outras Informacoes Mensais, devem
     ser  expressas na moeda corrente da data do evento objeto da in-
     formacao;

b) "UPF"  - Este campo foi incluido para identificar apenas as infor-
   macoes financeiras das operacoes de credito atualmente baseadas em
   Unidades de Padrao de Financiamento - UPF, e que podem ser expres-
   sas  em UPF-Mensal ou UPF-Trimestral. Este campo e mutuamente  ex-
   clusivo com o campo "MOEDA". Possui cinco posicoes numericas e de-
   ve ser preenchido com os codigos 20050 para UPF-Mensal e 40050 pa-
   ra a UPF-Trimestral;

c) "MES  REF" (Mes de Referencia) - Trata-se de um campo data de seis
   posicoes (ddmmaa), a ser preenchido com o ultimo dia do mes utili-
   zado  como base para atualizacao dos valores financeiros registra-
   dos  na opcao de cadastramento da operacao. Esse campo e de preen-
   chimento  obrigatorio apenas quando as informacoes financeiras fo-
   rem  atualizadas na forma facultada pelo item a.2 retro, caso con-
   trario deve ser deixado em branco.;

d) "PRINC  A LIB" (Principal a Liberar) - consiste apenas na  substi-
   tuicao  da  denominacao do campo "SLD.LIB" - Saldo a Liberar.  Sua
   operacionalizacao  continua a mesma, ou seja, este campo deve  ser
   preenchido  exclusivamente  com o montante de principal ainda  por
   liberar aos tomadores, expressos na moeda informada em um dos cam-
   pos  "MOEDA" ou "UPF". Observar que esse campo deve ser preenchido
   apenas para as operacoes existentes ate 24.09.93;

e) "PRINC  A PAG" (Principal a Pagar) - consiste apenas na substitui-
   cao  da denominacao do campo "SLD.PAG" - Saldo a Pagar. Sua opera-
   cionalizacao continua a mesma, ou seja, este campo deve ser preen-
   chido  exclusivamente com o montante de principal ainda por  pagar
   pelos  tomadores,  expressos na moeda informada em um  dos  campos
   "MOEDA" ou "UPF". Observar que esse campo deve ser preenchido ape-
   nas para as operacoes existentes ate 24.09.93;

f) "TAXA"  - Consiste apenas na substituicao da denominacao "TAXA EN-
   CARGO". Sua operacionalizacao continua a mesma, ou seja, este cam-
   po  deve ser preenchido com a taxa de encargos pactuada quando  da
   contratacao  da operacao de credito,  expressa em percentagem  com
   oito digitos, sendo os quatro primeiros digitos destinados aos in-
   teiros  e  os quatro seguintes para as decimais. Nao deve ser  in-
   cluida  na TAXA, a parcela correspondente a atualizacao monetaria,
   desde  que  essa seja explicitada na operacao e indicada no  campo
   "INDICE  DE ATUALIZACAO". Tambem, nao deve ser incluida na TAXA, a
   parcela de custos referente a Seguro;

g) "PERIODO"  -  Campo novo, incluido para captar a periodicidade  da
   TAXA  da operacao de credito de referencia. Tem apenas uma posicao
   e  deve  ser preenchido, de acordo com tabela especifica que  pode
   ser acionada a partir do proprio campo  (1 = Ao Dia, 2 = Ao Mes, 3
   =  Ao Bimestre, 4 = Ao Trimestre, 5 = Ao Quadrimestre, 6 = Ao  Se-
   mestre, 7 = Ao Ano);

h) "TIPO"  - Campo novo, incluido para identificar se os encargos de-
   correntes  da "TAXA" sao cobrados antecipada ou  postecipadamente.
   Tem apenas uma posicao e deve ser preenchido, de acordo com tabela
   especifica  que  pode ser acionada a partir do proprio campo (1  =
   antecipado; e 2 = Postecipado)

i) "CAPITALIZACAO"  - Campo novo, incluido para identificar se os en-
   cargos cobrados, decorrentes da "TAXA", obedecem ao regime capita-
   lizacao  Simples  ou Composta. Tem apenas uma posicao e  deve  ser
   preenchido de acordo com tabela especifica que pode ser acionada a
   partir do proprio campo (1 = Simples; e 2 = Composta).

j) "INDEXADA"  -  Campo  novo, de apenas uma posicao,  incluido  para
   identificar se a operacao de credito tem o principal corrigido por
   algum  indexador explicito e que portanto, nao deve estar embutido
   na  "TAXA".  Este campo  dever ser  preenchido com "S" = SIM  para
   as  operacoes indexadas ou, "N" = NAO para  as operacoes nao inde-
   xadas, ao ser utilizada a transacao PDIP500 e, com "1" = SIM e "2"
   =  NAO, quando as informacoes forem enviadas por meio de fita mag-
   netica;

k) "INDICE DE ATUALIZACAO" - Este continua sendo um campo nao numeri-
   co  de seis posicoes e deve ser preenchido sempre que o campo "IN-
   DEXADA"  tenha como resposta "SIM". Deve ser utilizado para infor-
   mar  o indexador utilizado para atualizacao do principal da opera-
   cao  de  credito pactuado quando de sua realizacao. Ex: TR,  IGPM,
   IGPDI,  CAMBIO, entre outras. Caso a Instituicao Financeira utili-
   ze-se  de um indexador proprio, este campo pode ser preenchido com
   o mnemonico "PROPRI";

l) "COND.OPERACAO"  - Este campo continua com a mesma denominacao  do
   anterior, mantendo suas sessenta posicoes nao numericas. Tem a fi-
   nalidade  de identificar o metodo de amortizacao, a  periodicidade
   de pagamento do principal e dos encargos, alem da identificacao do
   periodo  de carencia. Ex.; Amortizacao pela Tabela Price com  dois
   anos  de carencia.; Amortizacao pelo Sistema Hamburgues e sem  ca-
   rencia;  Pgtos. Mensais de Juros e Resg. Anual do Princ., sem  ca-
   rencia; entre outros.

TRATAMENTO  DAS OPERACOES DE CREDITO CADASTRADAS ANTES DESTAS ALTERA-
COES

2.             As  Instituicoes  Financeiras que ate 09.11.93  tenham
cadastrado  operacoes  de credito atraves da transacao PDIP500 ate  o
numero  9300004242 inclusive, deverao complementar as respectivas in-
formacoes  cadastrais, identificadas pelos campos que se encontram em
branco, ate o dia 30.11.93, na tela de "Cadastramento da Operacao" da
transacao PDIP500.

3.             Para  prestar as informacoes complementares basta uti-
lizar-se do seguinte procedimento:

a) No Menu de Opcoes, escolher a "Acao 1" (Cadastrar) combinada com a
   "Opcao 2" (Alterar), fornecendo o Numero BACEN da operacao de cre-
   dito considerada;

b) Complementar  os campos que se encontram em branco, na tela de Ca-
   dastro da Operacao.

TRATAMENTO DAS OPERACOES DE CREDITO A SEREM CADASTRADAS APOS AS ALTE-
RACOES

4.             O  procedimento para novos cadastramentos de operacoes
continua  inalterado. Basta selecionar a "Opcao 1" (Cadastramento)  e
"Acao  1" (Inclusao), na tela de Menu de Opcoes e, em seguida  preen-
cher  os  campos  da tela Cadastramento de Operacoes,  com  seu  novo
leiaute e os respectivos Cronogramas de Liberacao e/ou de Pagamento.

5.             As  consultas  sobre eventuais duvidas a respeito  dos
dados  a serem incluidos ou alterados na transacao PDIP500 devem  ser
formalmente dirigidas ao Departamento da Divida Publica (DEDIP).

               Brasilia, 12 de novembro de 1993

               DEPARTAMENTO DA DIVIDA PUBLICA

               Carlos Augusto Dias de Carvalho
               CHEFE
```
