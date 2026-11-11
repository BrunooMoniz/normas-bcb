---
titulo: "COMUNICADO N. 007608"
orgao: "Banco Central do Brasil"
tipo: "Comunicado"
numero: "7608"
data: 2000-06-08
ementa: "Esclarece sobre a remessa, ao Ban- co Central do Brasil, das informa- coes de que trata o art 3. da Cir- cular n. 2.977, de 2000."
revogada: false
responsavel: "SECRE"
versao_texto: "texto do portal do BCB"
fonte: "https://www.bcb.gov.br/estabilidadefinanceira/exibeoutrasnormas?tipo=Comunicado&numero=7608"
baixado_em: 2026-11-11
---
# COMUNICADO N. 007608

```
                        COMUNICADO N. 007608
                        --------------------

                                   Esclarece sobre a remessa, ao Ban-
                                   co Central do Brasil, das informa-
                                   coes de que trata o art 3. da Cir-
                                   cular n. 2.977, de 2000.

   De  acordo com o disposto na  Circular n. 2.977, de  6 de abril de
2000, e na Carta-Circular n.  2.909, de 26 de  abril de 2000, fazemos
os seguintes esclarecimentos;

   I  _ Com relacao a transmissao e  ao processamento das informacoes
da Central de Risco de Credito:

   a) as instituicoes conectadas ao Sistema de Informacoes Banco Cen-
tral - SISBACEN na modalidade TCU-TCU  e usuarias do software CONNECT
DIRECT  devem  entrar  em  contato  com   o  Banco  Central  do  Bra-
sil/Departamento de Informatica  (DEINF/DITEC), telefones  (061) 414-
2130 e 414-2073, para definicao e  ajuste dos parametros de transmis-
sao;

   b)  as demais instituicoes devem obter junto  ao componente do De-
partamento de Informatica a que estiverem  jurisdicionadas ou por in-
termedio da  INTERNET,  endereco  http://www.bcb.gov.br,  o  programa
PSTAW10, executavel em ambiente Windows 95, NT ou superior, destinado
a cifragem dos dados e transmissao  atraves da Internet, para o Banco
Central do Brasil, e que inclui  as instrucoes de instalacao e utili-
zacao no arquivo LEIAME.TXT;

   c)  o leiaute do documento 3010 _  Devedores do Sistema Financeiro
Nacional encontra-se disponivel na transacao PDIC600, do SISBACEN;

   d)  o simples envio do documento nao  garante a aceitacao e o pro-
cessamento das informacoes nele  contidas, sendo a  geracao do numero
de protocolo apenas a confirmacao de  que o documento foi transmitido
com sucesso;

   e)  apos a transmissao dos dados da Central de Risco de Credito, a
instituicao deve consultar a transacao PSTA300  do SISBACEN para con-
firmar o recebimento do arquivo pelo  Banco Central do Brasil e iden-
tificar eventuais erros de identificacao  na sua abertura, observando
que, constatada a inexistencia de erro,  o documento sera submetido a
processamento, desde que a posicao relativa  a data-base anterior te-
nha sido processada sem erro;

   f)  por meio da transacao  PDEV300 do SISBACEN,  a instituicao tem
acesso ao resultado do processamento e  as informacoes de responsabi-
lidade dos clientes. A  consulta ao resultado do processamento permi-
te a identificacao de  erros relativos a dados  da instituicao finan-
ceira e dos clientes;

   g) apos a confirmacao do processamento sem erro dos dados enviados
relativos a uma determinada data-base, fica liberada para a institui-
cao remetente a consulta  ao banco de dados  do Sistema relativamente
aquela data-base;

   h) para o processamento de mais de um documento (diferentes datas-
base), devera ser remetido um por  dia, em ordem cronologica crescen-
te;

   II _ Com relacao ao preenchimento dos campos:

   a) Saldos zerados: para o fornecimento da informacao de saldos ze-
rados no documento 3010-Devedores do Sistema Financeiro Nacional, re-
ferentes a uma  data-base, deve ser  obedecido o  leiaute descrito no
anexo a Carta-Circular 2.909, de 2000, com as seguintes observacoes:

   1. registro de identificacao (codigo LDEV001);

   2. registro de dados (codigo LDEV0002):

   para o registro consolidado de CNPJs, utilizar o registro de dados
 com as seguintes particularidades:

   Campo CNPJ do cliente: preencher as 11 posicoes  com  9,  ou seja,
99999999999;

   Campo indicador CNPJ: preencher com o valor numerico 3;

   Todos os campos de valores (posicoes 13 a 182): preencher com  ze-
ros;

   Campo categoria de risco: preencher com zero;

   para  o registro consolidado de CPFs, utilizar o registro de dados
com as seguintes particularidades:

   Campo  CPF do cliente: preencher  as 11    posicoes   com    9, ou
seja, 99999999999;

   Campo indicador CPF: preencher com o valor numerico 4;

   Todos  os campos de valores (posicoes 13 a 182): preencher com ze-
ros;

   Campo categoria de risco: preencher com zero;

   3. registro de controle final (codigo LDEV003);

   b) a adocao da providencia ora tratada e obrigatoria enquanto per-
sistir a situacao  de saldos  zerados do documento  3010, ou  seja, e
obrigatorio o envio de dados com  saldos zerados, tanto para consoli-
dado de CNPJ quanto para CPF;

   c) a partir da data-base abril/2000, inclusive, os valores relati-
vos a dividas  vencidas, cujo atraso  seja inferior a  15 dias, devem
ser informados como dividas a vencer ate 180 dias;

   d)  a partir da data-base abril/2000, inclusive, sera aceita a du-
plicidade de CNPJs e  CPFs no documento  remetido, exclusivamente com
vistas a permitir a  identificacao dos diferentes niveis  de risco do
cliente, sendo vedada essa duplicidade para um mesmo nivel de risco;

   e) a prestacao de informacoes referentes aos consolidados de CNPJs
e CPFs e obrigatoria, devendo haver  a segregacao de tais informacoes
por nivel de risco do cliente, exceto no caso de informacao de saldos
zerados;

   f)  na existencia de operacoes com valores abaixo de R$ 20.000,00,
somente deve ser informado  o valor global consolidado  dos niveis de
risco relativos  aquelas operacoes.  Nesse caso,  os niveis  de risco
para os quais nao existam operacoes  nao devem ser informados com va-
lores zerados;

   III _ Com relacao a disponibilizacao dos dados:

   a)  as informacoes da Central de Risco  referentes a uma data-base
somente sao disponibilizadas quando 80%,  no minimo, das instituicoes
tiverem seus dados de clientes processados  e, adicionalmente, a con-
sulta e condicionada  a previa  remessa e regularidade  do mencionado
arquivo de clientes;

   b)  a base de dados disponivel para consulta contem informacoes da
data-base mais recente, podendo retroagir, no maximo, a um periodo de
doze meses;

   IV _ Com relacao a alteracao de informacoes ja processadas:

    a)  faz-se necessaria  a substituicao  do documento anteriormente
remetido. Para tanto, deve ser formalizado  pedido contendo as justi-
ficativas necessarias, por meio de correio eletronico dirigido ao De-
partamento de Cadastro  e Informacoes do  Sistema Financeiro (DECAD),
no caso de  instituicoes jurisdicionadas a  sede do  Banco Central do
Brasil ou, nos  demais casos, a  Gerencia Tecnica  que jurisdiciona a
instituicao. Citado pedido deve ser  firmado pelo Diretor responsavel
pelas informacoes da Central de Risco;

   b) apos autorizada a substituicao do documento, a instituicao deve
transmitir os dados  a partir  da mensagem substituicao  de documento
autorizada, a ser obtida na opcao  5 - Resultado do Processamento, da
transacao PDEV300 do SISBACEN, ate o  dia util seguinte ao do pedido,
obedecida a sistematica vigente;

   c)  quando constatada, pela  instituicao financeira  ou pelo Banco
Central do Brasil, a prestacao de quaisquer informacoes incorretas no
documento 3010, e  obrigatoria a substituicao  das informacoes envia-
das. Essa obrigatoriedade  abrange  apenas informacoes incorretas re-
ferentes ao periodo de doze meses  anteriores a ultima informacao re-
metida;

   d)  na existencia de ordem judicial determinando a exclusao de in-
formacoes da Central de Risco de  Credito, os saldos devedores desses
clientes devem ser incluidos entre aqueles  para os quais dispensa-se
a identificacao (para esses casos deve-se manter dossie para eventual
fiscalizacao por parte do Banco Central  do Brasil). Referida solucao
tem carater provisorio,  ate que seja  implantado tratamento adequado
para situacoes da especie no sistema Central de Risco de Credito;

   e)  havendo necessidade  de substituicao  de mais de  um documento
(diferentes datas-base) para uma mesma instituicao financeira, os do-
cumentos nao podem ser  remetidos todos em um  mesmo dia, devendo ser
enviados um por dia, sem obediencia a ordem cronologica;

   2.    Ficam revogados os Comunicados n.s. 5.715, de 18 de julho de
1997, 5.846, de  14 de  outubro de 1997,  6.315, de  17 de  agosto de
1998, 6.998, de  15 de  outubro de 1999,  e 7.035, de 04  de novembro
de 1999.

                        Brasilia, 8 de junho de 2000.

Departamento de Cadastro e Informacoes     Departamento de
do Sistema Financeiro                      Informatica

Lucio Ricardo Rodrigues Oliveira           Reinaldo Dona Sol
Chefe Substituto                           Chefe Substituto

Departamento de Fiscalizacao

Vanio Cesar Pickler Aguiar
Chefe Substituto
```
