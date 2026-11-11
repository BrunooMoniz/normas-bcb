---
titulo: "COMUNICADO N. 007431"
orgao: "Banco Central do Brasil"
tipo: "Comunicado"
numero: "7431"
data: 2000-04-07
ementa: "RDE _ Registro Declaratorio Eletronico _ Modulo ROF _ Registro de Operacoes Financeiras - Informa os procedimentos para regularizacao das operacoes de refinanciamento registradas provisoriamente."
revogada: false
responsavel: "FIRCE"
versao_texto: "texto do portal do BCB"
fonte: "https://www.bcb.gov.br/estabilidadefinanceira/exibeoutrasnormas?tipo=Comunicado&numero=7431"
baixado_em: 2026-11-10
---
# COMUNICADO N. 007431

```
                        COMUNICADO N. 007431
                        --------------------

                                 RDE    _    Registro    Declaratorio
                                 Eletronico _  Modulo ROF  _ Registro
                                 de  Operacoes Financeiras  - Informa
                                 os procedimentos  para regularizacao
                                 das  operacoes   de  refinanciamento
                                 registradas provisoriamente.

              Tendo  em vista o disposto  na Carta-Circular n. 2.901,
de 16 de  marco de 2000,  esclarecemos que, para  a regularizacao das
operacoes de refinanciamento  registradas provisoriamente  no Sistema
RDE, Modulo ROF,  pendentes de  inclusao do  esquema de  pagamento de
principal e  de  juros,  os interessados  devem  adotar  os seguintes
procedimentos:

    I - Operacoes sem alteracao do devedor:

    a) quanto ao registro original (modalidade 31xx ou 35xx):
    1) registrar evento(s) 8100 (baixa _ refinanciamento);
    2)  registrar evento(s)  4128 (refinanciamento  _ manifestacao do
credor);

    b) quanto ao registro do refinanciamento (destino):
    1) registrar modalidade 3116 ou 3516;
    2)  excluir periodo de juros relativos  a operacao original (taxa
igual a zero);
    3)  registrar evento(s)  6229 (refinanciamento)  e vincular ao(s)
ROF(s) original(is);
    4) registrar esquema(s) de pagamento de principal e de juros;

    II - Operacoes com alteracao do devedor:

    a) quanto ao registro original (modalidade 31xx ou 35xx):
    1) registrar evento(s) 8102 (assuncao de obrigacao);
    2) registrar evento(s) 4125 (assuncao _ manifestacao do credor);

    b) quanto ao registro da assuncao (destino):
    1) registrar modalidade 3117 ou 3517;
    2)  excluir periodo de juros relativos  a operacao original (taxa
igual a zero);
    3)  registrar evento(s) 6241  (assuncao de  obrigacao) e vincular
ao(s) ROF(s) original(is);
    4) registrar esquema(s) de pagamento de principal e de juros.

2.            Eventuais   duvidas  com   relacao   aos  procedimentos
descritos acima  devem  ser  esclarecidas  por  meio  de  consulta as
gerencias tecnicas  do  FIRCE  em Sao  Paulo,  Rio  de  Janeiro, Belo
Horizonte, Curitiba,  Porto  Alegre, Recife,  ou  ao  FIRCE/CONAC, em
Brasilia.

3.            Este Comunicado revoga o de n. 7.358, de 16 de marco de
2000.

                   Brasilia, 7 de abril de 2000

                   Departamento de Capitais Estrangeiros

                   Fernando Antonio Gomes
                   Chefe
```
