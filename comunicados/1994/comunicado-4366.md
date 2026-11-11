---
titulo: "COMUNICADO N. 004366"
orgao: "Banco Central do Brasil"
tipo: "Comunicado"
numero: "4366"
data: 1994-12-30
ementa: "PROAGRO - Securitizacao - Remessa de Dados"
revogada: false
responsavel: "DEORF"
versao_texto: "texto do portal do BCB"
fonte: "https://www.bcb.gov.br/estabilidadefinanceira/exibeoutrasnormas?tipo=Comunicado&numero=4366"
baixado_em: 2026-11-10
---
# COMUNICADO N. 004366

```
                        COMUNICADO N. 004366
                        --------------------

                              PROAGRO  -  Securitizacao - Remessa  de
                              Dados

               COMUNICAMOS que o registro no sistema de processamento
de dados do PROAGRO, de que trata o item II, artigo 1. da Circular n.
2.530, de 28.12.94, devera ser feito mediante remessa, ao Departamen-
to de Organizacao do Sistema Financeiro (DEORF), das  informacoes re-
lativas as coberturas e demais despesas pendentes  de pagamento ou de
ressarcimento relativas as indenizacoes pagas pelos agentes e as par-
celas financiadas e nao liquidadas ate 31.07.94, agrupadas  em arqui-
vo  especifico, em disquete ou fita magnetica, na forma do leiaute em
anexo.

2.              A fita magnetica devera ser gravada sem utilizacao de
"label"  interno, com densidade de 1600 ou 6250 BPI e portar etiqueta
indicando:

          I - o nome da instituicao remetente;
         II - o nome do arquivo:  AGRO055;
        III - a densidade de gravacao, e
         IV - a blocagem utilizada.

3.             O disquete devera ter o formato IBM/PC e ser etiqueta-
do com as informacoes a que se referem os incisos I e II acima.

4.             Os disquetes e fitas magneticas ficarao em poder deste
Banco Central, para arquivamento e eventuais prestacoes de contas aos
orgaos envolvidos.

5.             As coberturas e demais despesas de que tratam os inci-
sos I e II do artigo 2. da referida Circular deverao ser registrados
atraves  da opcao 1 da transacao PGRO200 do SISBACEN, sob  informacao
de TIPO DE REMESSA 6 (seis).

6.              As custas periciais complementares de que trata o in-
ciso  III do artigo 2. da Circular n. 2.530, de 28.12.94, deverao ser
registradas  atraves da opcao 1 da transacao PGRO200 do SISBACEN, sob
informacao de TIPO DE REMESSA 7 (sete).

                    Brasilia(DF), 30 de dezembro de 1.994.

                    DEPARTAMENTO DE ORGANIZACAO DO SISTEMA FINANCEIRO
                    - DEORF

                    Carlos Henrique de Paula
                    CHEFE, EM EXERCICIO

                       ANEXO AO COMUNICADO N.

Leiaute dos registros que comporao o arquivo a ser  remetido ao BANCO
CENTRAL  DO BRASIL, contendo operacoes do PROAGRO a serem securitiza-
das

Registro identificador (HEADER): primeiro registro do arquivo

------------------------------------------------------------------
CAMPO             FORMATO TAMANHO  OBSERVACOES
------------------------------------------------------------------
 tipo de remessa    c         1    Preencher com o caracter "5"
 cgc do agente      c         8    cgc (parte basica) do remetente
                                   do arquivo
 numero da remessa  n         8    numero atribuido pelo agente a
                                   remessa
 data da remessa    n         8    data "AAAAMMDD" de geracao/envio
                                   do arquivo
 identificador      c         7    preencher com "AGRO055"
 Brancos            c        66    nao preencher / preencher com
                                  brancos
 numero do registro n         6    preencher com 000001
------------------------------------------------------------------

registro totalizador  (TRAILER): ultimo registro do arquivo

------------------------------------------------------------------
CAMPO             FORMATO TAMANHO  OBSERVACOES
------------------------------------------------------------------
 tipo de remessa    c         1    Preencher com o caracter "5"
 cgc do agente      c         8    cgc (parte basica) do remetente
                                  do arquivo
 numero da remessa  n         8    numero atribuido pelo agente a
                                  remessa
 noves              c         8    preencher com "99999999"
 quantidade de

 registros          n         6    informar o total de registros
                                   de DADOS no arquivo
 Brancos            c        67    nao preencher / preencher com
                                   brancos
 numero do registro n         6    preencher com o numero do re-
                                   gistro no arquivo
------------------------------------------------------------------

registros de dados (2. ao penultimo)

------------------------------------------------------------------
CAMPO             FORMATO TAMANHO  OBSERVACOES
------------------------------------------------------------------
 tipo de remessa    c         1    Preencher com o caracter "5"
 cgc do agente      c         8    cgc (parte basica) do remetente
                                   do arquivo
 numero da remessa  n         8    numero atribuido pelo agente a
                                   remessa

 cgc do emitente    c        14    preencher com o cgc completo da
                                   agencia emitente da cedula
 referencia BACEN   c         9    informar o numero de referencia
                                   BACEN da cedula
 empreend. RECOR    c         2    informar o numero de ordem do
                                   empreendimento na cedula
 evento             c         3    indicar o codigo do evento cau-
                                  sador das perdas
 cgc periciadora    c        11    indicar o cpf (11 digitos) ou o
                                   cgc (8 digitos) do responsavel
                                   pela pericia
 instancia          c         1    indicar o codigo de responsavel
                                   pelo deferimento
 data base calculo  c         8    informar a data do calculo da
                                   cobertura (AAAAMMDD)
 natureza           c         3    informar o codigo de natureza
                                   do valor deferido
 valor   deferido    n        15    informar   o  valor  apurado   na
                                   data   do  calculo  da  cobertura,
                                   sem pontos ou virgulas
 vlr. a securitizar n        15    informar o valor da cobertura
                                   atualizado ate 31.07.94

 numero do registro n         6    preencher com o numero sequen-
                                   cial do registro no arquivo
------------------------------------------------------------------

Notas: - todos os campos deverao estar em formato DISPLAY
       - os codigos de evento e de natureza (registros de dados)
         podem ser obtidos nas tabelas TGRO001 e TGRO002
```
