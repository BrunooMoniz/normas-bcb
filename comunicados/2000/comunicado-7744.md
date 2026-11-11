---
titulo: "COMUNICADO N. 007744"
orgao: "Banco Central do Brasil"
tipo: "Comunicado"
numero: "7744"
data: 2000-07-31
ementa: "Divulga a nova regra de codificacao dos titulos publicos a serem registrados no SELIC."
revogada: false
responsavel: "DEMAB"
versao_texto: "texto do portal do BCB"
fonte: "https://www.bcb.gov.br/estabilidadefinanceira/exibeoutrasnormas?tipo=Comunicado&numero=7744"
baixado_em: 2026-11-11
---
# COMUNICADO N. 007744

```
                        COMUNICADO N. 007744
                        --------------------

                            Divulga a nova  regra de codificacao dos
                            titulos publicos a  serem registrados no
                            SELIC.

        Comunicamos  que, a partir  desta data, os codigos dos titu-
los publicos a serem registrados no Sistema Especial de Liquidacao e
de Custodia - SELIC terao o formato "NNXXYY", onde:

        NN - identificador do tipo/serie do titulo;

        XX - a) para  titulos com  rentabilidade   prefixada  e  sem
                cupom de juros:

                XX = 00;

             b) para os demais titulos:

                XX = 01 a 90 - numero sequencial a ser usado, quando
                     necessario, para diferenciar titulos  de  mesmo
                     tipo/serie e mesmo vencimento;

        YY - a) para titulos sem possibilidade de desmembramento:

                YY = 00;

             b) para titulos com possibilidade de desmembramento:

                YY = identificador   da   totalidade   do titulo, do
                     principal ou do cupom de juros, sendo:

                     99      -  principal  com  todos os cupons   de
                     juros;
                     98      - principal, apos o desmembramento;
                     90 a 01 - numero  sequencial  do cupom de juros
                     desmembrado, em ordem temporal inversa.

2.      Os  codigos dos titulos ja registrados no  SELIC  permanecem
inalterados.

3.      Na  hipotese  de desmembramento  dos  titulos  referidos  no
paragrafo anterior,  sera observado o disposto neste Comunicado para
os  digitos  "YY"  e, em caso de remembramento, serao restaurados os
codigos originais.

4.      O  documento  numero 8  (MNI 6.3 - DOC-8)  que  instruira  o
registro da operacao de desmembramento no SELIC devera ser preenchi-
do da seguinte forma:

        campo 03 - codigo do titulo a ser desmembrado;
        campo 04 - 1073 (codigo da operacao de desmembramento);
        campo 05 - nome  da  instituicao   financeira  detentora  do
                   titulo;
        campo 06 - codigo  da  instituicao  financeira  detentora do
                   titulo;
        campo 12 - comando de debito (1) - autorizacao de debito  do
                   titulo a ser desmembrado;
        campo 15 - numero da operacao de desmembramento;
        campo 16 - data  do vencimento do titulo a ser desmembrado;
                   e
        campo 17 - quantidade de titulos a serem desmembrados.

5.      O  desmembramento somente sera  efetuado  quando a  conta da
instituicao financeira  detentora pertencer ao  Subsistema  de Livre
Movimentacao e nao  estiverem  os  titulos  vinculados  a  quaisquer
compromissos de revenda.

6.      Adicionalmente,   estara    disponivel  a  operacao  de  re-
membramento, ao principal, de todos os cupons de juros vincendos.  O
documento numero  8 (MNI 6.3 - DOC-8) que instruira o registro dessa
operacao no SELIC devera ser preenchido da seguinte forma:

        campo 03 - codigo do titulo resultante do remembramento;
        campo 04 - 1074 (codigo da operacao de remembramento);
        campo 07 - nome   da  instituicao  financeira  detentora  do
                   principal e de todos os cupons de juros vincendos
                   a serem remembrados;
        campo 08 - codigo   da   instituicao   financeira  detentora
                   do  principal  e  de  todos  os cupons  de  juros
                   vincendos a serem remembrados;
        campo 12 - comando de credito (2) - autorizacao de debito do
                   principal e de todos os cupons de juros vincendos
                   a serem remembrados;
        campo 15 - numero da operacao de remembramento;
        campo 16 - data  do  vencimento  do   titulo  resultante  do
                   remembramento; e
        campo 17 - quantidade de titulos a serem remembrados.

7.      O  remembramento  somente sera  efetuado quando  a  conta da
instituicao financeira detentora pertencer  ao  Subsistema  de Livre
Movimentacao e nao estiverem, tanto o principal quanto  os cupons de
juros vincendos, vinculados a quaisquer compromissos de revenda.

8.      Os  registros  de movimentacao  com os  codigos  de operacao
1073 e 1074 exigirao duplo lancamento no SELIC, sendo  que um desses
lancamentos  devera ser efetuado pelo Departamento  de  Operacoes do
Mercado Aberto - DEMAB.

9.      Quanto  aos  demais aspectos operacionais, devera ser obser-
vada a orientacao constante do Manual do Usuario do SELIC - MUS.

10.     Fica revogado o Comunicado n. 7.588, de 31 de maio de 2000.

                            Rio de Janeiro, 31 de julho de 2000

                            DEPARTAMENTO DE OPERACOES
                            DO MERCADO ABERTO - DEMAB

                            Paulo Roberto Zakarewicz
                            Chefe, em exercicio
```
