---
titulo: "COMUNICADO N. 004755"
orgao: "Banco Central do Brasil"
tipo: "Comunicado"
numero: "4755"
data: 1995-09-01
ementa: "Estabelece instrucoes adicionais para o registro de dados no Sistema de Regis- tro de Operacoes de Credito com o Setor Publico (CADIP)"
revogada: false
responsavel: "DEDIP"
versao_texto: "texto do portal do BCB"
fonte: "https://www.bcb.gov.br/estabilidadefinanceira/exibeoutrasnormas?tipo=Comunicado&numero=4755"
baixado_em: 2026-11-10
---
# COMUNICADO N. 004755

```
                        COMUNICADO N. 004755
                        --------------------

                              Estabelece instrucoes adicionais para o
                              registro  de dados no Sistema de Regis-
                              tro de Operacoes de Credito com o Setor
                              Publico (CADIP)

               Tendo  em  vista  o disposto no Art. 7.,  da  Circular
2.367, de 23.09.93, informamos que foi incluido o campo "Pt" no modu-
lo  de  Cadastramento do Sistema de Registro de Operacoes de  Credito
com  o Setor Publico (CADIP), de forma a permitir o acompanhamento  e
controle  das operacoes contratadas ou garantidas pela  administracao
direta  de Estados, do Distrito Federal, de  Municipios e respectivas
autarquias.  O  preenchimento deste campo deve observar as  seguintes
instrucoes:

               a) o campo e composto de 10 caracteres numericos e de-
ve ser preenchido com o numero de protocolo sob o qual o processo re-
lativo  a  operacao de credito tramitou no Banco Central do Brasil  e
pode  ser encontrado no correio eletronico contendo a manifestacao do
Departamento  da  Divida Publica - DEDIP ou das Delegacias  Regionais
sobre a operacao;

               b)  na opcao de registro "on line" (transacao PDIP500)
basta preencher o campo "Pt" que consta da tela de Cadastramento;

               c) na opcao de registro em "batch" o campo "Pt" utili-
za-se  das  posicoes 217 a 226, da nova versao do  leiaute  LDIP0002,
disponivel por meio da transacao PDIC600, Documento 1010;

               d)  para as operacoes contratadas com entidades publi-
cas que nao sejam as administracoes diretas dos Estados, dos Distrito
Federal,  dos Municipios ou respectivas autarquias o campo "Pt"  deve
ser preenchido com zeros, na rotina "batch" e nao preenchido na roti-
na "on line".

2.             Informamos, ainda, que a denominacao do campo "INDEXA-
DA?(S/N)"  foi  alterada para "PREFIXADA?(S/N)". Este campo deve  ser
preenchido observadas as seguintes instrucoes:

               a) se a taxa for prefixada, o campo deve ser preenchi-
do com "S" na rotina "on line" e com "1" na rotina em "batch" e, nes-
ses casos, nao deve ser preenchido o campo "Indice Atualizacao";

               b)  se a taxa for pos-fixada, o campo deve ser  preen-
chido  com "N" na rotina "on line" e com "2" na rotina em "batch"  e,
nesses casos, deve ser preenchido o campo "Indice Atualizacao";

3.             Em  razao da mudanca de que trata o item anterior, in-
formamos que as causas do codigo de erro B22, quando do processamento
dos arquivos em "batch" sao as seguintes:

   Causa  1: nao foi informado o indice de atualizacao quando o campo
   "PREFIXADA" foi preenchido com 2 (nao);

   Causa  2: foi informado indice de atualizacao quando o campo "PRE-
   FIXADA" foi preenchido com 1 (sim).

4.             As  instrucoes contidas neste comunicado devem ser ob-
servadas a partir desta data.

                    Brasilia, 01 de setembro de 1995.

                    DEPARTAMENTO DA DIVIDA PUBLICA - DEDIP

                    Jairo da Cruz Ferreira
                    Chefe
```
