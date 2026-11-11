---
titulo: "COMUNICADO N. 008522"
orgao: "Banco Central do Brasil"
tipo: "Comunicado"
numero: "8522"
data: 2001-06-08
ementa: "Define procedimento alternativo a ser observado pelos participantes, relativamente ao envio/recepção de mensagens ao SELIC, durante o perío do de realização dos testes integra dos para o Sistema de Pagamentos Brasileiro e altera cronograma de testes."
revogada: false
responsavel: "SECRE"
versao_texto: "texto do portal do BCB"
fonte: "https://www.bcb.gov.br/estabilidadefinanceira/exibeoutrasnormas?tipo=Comunicado&numero=8522"
baixado_em: 2026-11-11
---
# COMUNICADO N. 008522

```
                        COMUNICADO N. 008522
                        --------------------

                                  Define procedimento alternativo   a
                                  ser observado  pelos participantes,
                                  relativamente ao envio/recepção  de
                                  mensagens ao SELIC, durante o perío
                                  do de realização dos testes integra
                                  dos para o  Sistema  de  Pagamentos
                                  Brasileiro e altera cronograma   de
                                  testes.

        O SELIC  tornará  disponível,  temporariamente, a  partir  de
11.6.2001, a alternativa de envio/recepção de mensagens via Internet,
sem  prejuízo  do acesso por intermédio da RSFN, para a realização de
testes integrados do Sistema de Pagamentos Brasileiro.

2.      As  mensagens  para  testes das aplicações devem ser enviadas
para a fila de REQUISIÇÕES do Selic. As respostas (R1, R2 ou de ERRO)
serão  recebidas  pelo  participante  na  fila  de  RESPOSTAS.  Essas
mensagens  devem estar no padrão definido para o SPB, ou seja, conter
o  header  de  segurança  com  indicativo  de  tamanho igual ao valor
hexadecimal H'014C' seguido de 330 bytes contendo zeros binários (sem
criptografia)  e  a  mensagem XML completa em código UNICODE UTF-16 -
BE, sem BOM (bytes significativos alinhados à direita).

3.      Informamos  que  o  cadastramento  dos  objetos  MQ  no SELIC
deve ser feito com a opção 7 da transação PRED300 do Sisbacen.

4.      Com relação aos testes via Internet, observar o que segue:

        a) endereço definido para o Selic na Internet: 200.252.35.115
           Porta 1414 (apenas  para  as Instituições ainda não conec-
           tadas à rede RSFN);
        b) nome do servidor MQ de Homologação do Selic na rede SPB:
           mqs02.selic.rsfn.net.br
        c) nomes dos objetos MQ do Selic:
            queue manager: QM.00038121.01
           filas locais (no Selic):
                QL.REQ.nnnnnnnn.00038121.01
                QL.RSP.nnnnnnnn.00038121.01
                QL.REP.nnnnnnnn.00038121.01
                QL.SUP.nnnnnnnn.00038121.01

            canais (no Selic):
            SENDER   : C00038121.nnnnnnnn.1
            RECEIVER : Cnnnnnnnn.00038121.1

        O conteúdo de  nnnnnnnn deverá ser o número da instituição no
        Sistema de Pagamentos Brasileiro com 8 algarismos (ISPBIF).

        d) data de referência do movimento a ser testado: 1.6.2001;
        e) posição de custódia de referência: 1.6.2001 (o arquivo
           encontra-se disponível no site do Selic: www.demab.rtm);
        f) telefones para contato e eventuais dúvidas:
           (21) 3805-5570 e 3805-5540.

5.      Em função  da  alternativa de acesso proposta, informamos que
as mensagens definidas  no  Comunicado 8.476, de 24.5.2001, previstas
para a semana de 1 a 8.6.2001 permanecerão disponíveis para testes no
período de 11 a 15.6.2001,  impondo,  em  conseqüência, alteração  no
calendário de testes, conforme anexo.

            Brasília (DF), 8 de junho de 2001

Roberto Ozu                    Sérgio Goldenstein
Chefe do                       Chefe do Departamento de Operações
Departamento de Informática    do Mercado Aberto
[
ANEXO

CRONOGRAMA DE TESTES PARA JUNHO DE 2001

MENSAGENS DO SELIC

1.6  a 15.6.2001 - SEL1003 - Desvinculação de Títulos
                 - SEL1013 - Vinculação de Títulos
                 - SEL1062 - Transferência de  Títulos sem Financeiro

18.6 a 22.6.2001 - SEL1052 - Operação Definitiva
                 - SEL1066 - Repasse de Impostos
                 - SEL3052 - Operação a Termo

25.6 a 29.6.2001 - SEL1073 - Desmembramento em Cupom de Juros
                 - SEL1074 - Remembramento de Cupom de Juros
                 - SEL1080 - Consulta de Operação
                 - Período alternativo para teste das mensagens do
                   mês.
```
