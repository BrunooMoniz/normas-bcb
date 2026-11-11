---
titulo: "COMUNICADO N. 008498"
orgao: "Banco Central do Brasil"
tipo: "Comunicado"
numero: "8498"
data: 2001-05-31
ementa: "Sistema de Pagamentos Brasileiro- Testes - MQSeries"
revogada: false
responsavel: "DEINF"
versao_texto: "texto do portal do BCB"
fonte: "https://www.bcb.gov.br/estabilidadefinanceira/exibeoutrasnormas?tipo=Comunicado&numero=8498"
baixado_em: 2026-11-11
---
# COMUNICADO N. 008498

```
                        COMUNICADO N. 008498
                        --------------------

                                    Sistema de Pagamentos Brasileiro-
                                    Testes - MQSeries

      Comunicamos que  os testes do Sistema de Pagamentos Brasileiro,
que  se iniciarão no próximo dia 01.06.2001, serão efetuados usando a
conexão de MQSeries via Internet, conforme disponibilizado pelo Banco
Central na comunicação 101068217, de 16.04.2001, Anexo II a este  Co-
municado.

2.    Adicionalmente, informamos que:

a)    a  partir  do  dia  31.05.2001  as  mensagens  para  teste   de
conectividade  MQ devem ser enviadas para a  fila de SUPORTE no Banco
Central. A resposta será retornada na fila de Suporte do participante
do SPB;

b)    as mensagens para testes das aplicações devem ser enviadas para
a  fila  de  REQUISIÇÕES do Banco Central. As respostas (R1, R2 ou de
ERRO) serão  recebidas  pelo participante na fila de RESPOSTAS. Essas
mensagens devem estar no  padrão definido para o SPB, ou seja, conter
o  header  de  segurança  com  indicativo  de  tamanho igual ao valor
hexadecimal H'014C' seguido de 330 bytes contendo zeros binários (sem
criptografia)  e  a mensagem XML completa em código UNICODE UTF-16.

3.    O Anexo  I  descreve  os  procedimentos  a serem efetuados para
possibilitar a conexão para os testes.

Reinaldo Doná Sol
Chefe do Deinf, em exercício

Anexo I

Procedimentos  de conectividade

· Solicitar  ao  master  Sisbacen  da  instituição o cadastramento na
transação PRED300 -  Testes  SPB  -  Conectividade  de  MQSeries,  no
ambiente de HOMOLOGAÇÃO do Banco Central; para acessar esse ambiente,
digitar  HOMOLOGA  no  campo  TRANSAÇÃO  da tela de logon do SISBACEN
(vide Comunicado Geral 100209388, de 03.11.2000);

· Definir  as  filas  locais no MQSeries da instituição;  caso deseje
adotar o padrão  SPB   para   nomenclatura  de   objetos,   no   link
http://www.bcb.gov.br/htms/spb/relatoriosMQSeries/objetos.txt   há  a
definição de todos os objetos necessários ao ambiente da instituição;

· Acessar  a PRED300 acionando a opção 1 - Definição de objetos MQ no
BC - e informar  os nomes das filas definidas no item anterior e o IP
e porta para o BC  conectar  o  MQ da instituição (o endereço IP deve
ser um endereço da instituição válido  na internet e a porta deve ser
1414);

· Definir as filas remotas no MQSeries da instituição correspondentes
'as filas do BC,  de  acordo  com  as  informações  obtidas durante o
cadastramento na PRED300;

· Definir  a  fila  de transmissão para o BC, de acordo com o nome do
queue manager do BC, exibido na PRED300;

· Definir  os canais, de acordo com os nomes fornecidos pela PRED300,
conectando com  o endereço IP do Banco Central, 200.252.35.114, porta
1414.  Esse  endereço  é  apenas  para  testes  via  internet  e  não
corresponde ao da rede SPB;

· Os  mecanismos  de  segurança  de  rede da instituição (firewall ou
equivalente)  devem ser ajustados para permitir as conexões ao  Banco
Central e deste  ao endereço IP da instituição, na referida porta TCP
1414;

· Definir  o  Queue  Manager  Alias  Name  no MQSeries da instituição
correspondente ao Queue Manager da IF exibido na PRED300;

· Acionar a opção 3 da PRED300  - Ativação de canal;

· Acionar opção 4 da PRED300 - Consulta status do canal - se desejar;

· Enviar  mensagens  para  a  fila  de SUPORTE no BC; essas mensagens
podem conter qualquer texto e não  devem  estar  no padrão SPB porque
serão convertidas para o CCSID local;

· As  respostas serão devolvidas na fila de SUPORTE informada durante
o cadastramento  na PRED300; essas mensagens não são tratadas, apenas
devolvidas pelo BC;

· Destacamos que eventuais dúvidas podem ser dirimidas por intermédio
da central de atendimento à rede do Banco Central, telefone (61)
414-2156.

Anexo II  -   Comunicação 101068217, de 16.04.2001

                 Testes de conectividade de MQSeries

Comunicamos  que  os  testes  opcionais de conectividade de MQSeries,
no Sistema de Pagamentos Brasileiros (SPB), com o Banco Central podem
ser  realizados a partir do dia 16 de abril, devendo serem observados
os  procedimentos a seguir descritos:

I.   Definir as filas locais no MQSeries de sua instituicao;

II.  Solicitar ao master Sisbacen de sua instituicao autorizacao para
     a transacao PRED300  (Testes SPB - Conectividade de MQSeries);

III. Acessar a PRED300 e solicitar opcao 1 - Definicao de objetos MQ
     no BC - e informar os nomes das filas definidas no item I;

IV.  Definir as filas remotas no MQSeries de sua instituicao corres-
     pondentes as filas do BC, de acordo com as informacoes obtidas
     durante o cadastramento na PRED300;

V.   Definir a fila de transmissao para o BC, de acordo com o nome do
     queue manager do BC exibido na PRED300;

VI.  Definir  os  canais,  de  acordo  com  os nomes fornecidos  pela
     PRED300,  conectando  com  o  endereco  IP  do  Banco   Central,
     200.252.35.114, porta 1414. Esse endereco e' apenas para testes
     via internet e nao corresponde ao da rede SPB;

VII. Definir o Queue Manager Alias Name no MQSeries de sua institui-
     cao correspondente ao Queue Manager da IF exibido na PRED300;

VIII.Solicitar opcao 3 - Ativacao de canal;

IX.  Solicitar opcao 4 - Consulta status do canal - se desejar;

X.   Enviar mensagens para a fila de REQUISICAO no BC;

XI.  As respostas serao devolvidas na fila de RESPOSTA informada du-
     rante o cadastramento na PRED300;

As mensagens  nao  serao  tratadas nesta fase. O Banco Central apenas
devolve o que recebeu.

Destacamos  que  eventuais duvidas podem ser dirimidas por intermedio
da central  de  atendimento  a  rede  do Banco Central, telefone (61)
414-2156.

      Roberto Ozu                  Jose Antonio Eirado Neto
      Chefe do DEINF               Chefe Adjunto do DEINF
```
