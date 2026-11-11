---
titulo: "COMUNICADO N. 011594"
orgao: "Banco Central do Brasil"
tipo: "Comunicado"
numero: "11594"
data: 2003-11-13
ementa: "Divulga os novos dados que devem instruir os comandos para o registro e a liquidação das operações com in- termediação no Sistema Especial de Liquidação e de Custódia (Selic)."
revogada: false
responsavel: "DEMAB"
versao_texto: "texto do portal do BCB"
fonte: "https://www.bcb.gov.br/estabilidadefinanceira/exibeoutrasnormas?tipo=Comunicado&numero=11594"
baixado_em: 2026-11-11
---
# COMUNICADO N. 011594

```
                        COMUNICADO N. 011594
                        --------------------

                                 Divulga os  novos  dados  que  devem
                                 instruir os comandos para o registro
                                 e a liquidação das operações com in-
                                 termediação no Sistema  Especial  de
                                 Liquidação e de Custódia (Selic).

    Os  comandos  para o  registro e a liquidação das  operações  com
intermediação devem ser instruídos, observadas as disposições  gerais
contidas no Regulamento do Selic e no Manual do Usuário do Selic, com
os seguintes dados específicos:

    I - operação definitiva, código 1052, com a intermediação  de  um
corretor:

    a) duplo comando - instituição  vendedora e  instituição interme-
diária:

         1.  campos 5 e 6: nome da instituição vendedora e código  de
         sua conta de custódia de livre movimentação;

         2.  campos 8 e 9: nome da instituição intermediária e código
         de sua conta de corretagem;

         3.  campo  16:  número  da  faixa  numérica  da  instituição
         vendedora;

         4.  campo 19: preço unitário de venda dos títulos; e

         5.  campo  22, somente  no  comando  da  instituição  inter-
         mediária: conteúdo  do campo  16  mencionado  na  alínea "b"
         deste inciso;

    b) duplo comando - instituição compradora e  instituição interme-
diária:

         1.  campos 5 e 6: nome da instituição intermediária e código
         de sua conta de corretagem;

         2.  campos 8 e 9: nome da instituição compradora e código de
         sua conta de custódia de livre movimentação;

         3.  campo  16:  número  da  faixa  numérica  da  instituição
         intermediária;

         4.  campo  19: preço unitário de compra dos títulos; e

         5.  campo  22, somente  no  comando  da  instituição  inter-
         mediária: conteúdo  do  campo  16  mencionado  na alínea "a"
         deste inciso;

    II - operação definitiva, código  1052, com  a  intermediação  de
dois corretores:

    a) duplo comando - instituição  vendedora  e respectiva  interme-
diária:

         1.  campos 5 e 6: nome da instituição vendedora e código  de
         sua conta de custódia de livre movimentação;

         2.  campos 8 e 9: nome da instituição intermediária e código
         de sua conta de corretagem;

         3.  campo  16:  número  da  faixa  numérica  da  instituição
         vendedora;

         4.  campo 19: preço unitário de venda dos títulos; e

         5.  campo  22, somente  no   comando  da  instituição inter-
         mediária:  conteúdo do  campo 16  mencionado  na  alínea "b"
         deste inciso;

    b) duplo comando - instituições intermediárias:

         1.  campos  5  e  6:  nome da intermediária  da  instituição
         vendedora e código de sua conta de corretagem;

         2.  campos  8  e  9:  nome da intermediária  da  instituição
         compradora e código de sua conta de corretagem;

         3.  campo  16: número da faixa numérica da intermediária  da
         instituição vendedora;

         4.  campo  19: preço unitário de venda dos títulos acrescido
         do   preço  unitário  de  corretagem  da  intermediária   da
         instituição vendedora;

         5.  campo 22, comando da intermediária  da  instituição ven-
         dedora: conteúdo  do  campo  16  mencionado  na  alínea  "a"
         deste inciso; e

         6.  campo 22, comando  da  intermediária da instituição com-
         pradora: conteúdo  do  campo  16  mencionado na  alínea  "c"
         deste inciso;

    c) duplo comando - instituição  compradora  e  respectiva  inter-
mediária:

         1.  campos 5 e 6: nome da instituição intermediária e código
         de sua conta de corretagem;

         2.  campos 8 e 9: nome da instituição compradora e código de
         sua conta de custódia de livre movimentação;

         3.  campo  16:  número  da  faixa  numérica  da  instituição
         intermediária;

         4.  campo 19: preço unitário de compra dos títulos; e

         5.  campo  22, somente  no  comando  da   instituição inter-
         mediária: conteúdo  do  campo 16  mencionado  na  alínea "b"
         deste inciso;

    III - operação compromissada, código 1054, com a intermediação de
um corretor:

    a) duplo comando - instituição   vendedora  e  instituição inter-
mediária:

         1.  campos  5,  6,  8,  9,  16, 19 e  22:  os  mesmos  dados
         previstos na alínea "a" do inciso I; e

         2.  campo 20: preço unitário de recompra dos títulos;

    b) duplo comando - instituição compradora  e  instituição  inter-
mediária:

         1.  campos  5,  6,  8,  9,  16, 19 e  22:  os  mesmos  dados
         previstos na alínea "b" do inciso I; e

         2. campo 20: preço unitário de revenda dos títulos;

    IV - operação compromissada, código 1054, com a intermediação  de
dois corretores:

    a) duplo comando - instituição   vendedora  e  respectiva  inter-
mediária:

         1.  campos  5,  6,  8,  9,  16, 19 e  22:  os  mesmos  dados
         previstos na alínea "a" do inciso II; e

         2.  campo 20: preço unitário de recompra dos títulos;

    b) duplo comando - instituições intermediárias:

         1.  campos  5,  6,  8,  9,  16, 19 e  22:  os  mesmos  dados
         previstos na alínea "b" do inciso II; e

         2.  campo  20: preço  unitário   de  revenda   dos   títulos
         acrescido,  se  for o caso, do preço unitário da  corretagem
         da intermediária da instituição revendedora;

    c) duplo comando - instituição  compradora  e  respectiva  inter-
mediária:

         1.  campos  5,  6,  8,  9,  16, 19 e  22:  os  mesmos  dados
         previstos na alínea "c" do inciso II; e

         2.  campo 20: preço unitário de revenda dos títulos;

    V - operação compromissada, código 1056, com a  intermediação  de
um ou dois corretores: os comandos a serem transmitidos restringem-se
aos das instituições compradora e vendedora da operação original.

2.  Os  novos  dados previstos  neste comunicado deverão instruir  os
comandos  a  serem  transmitidos a partir de 19 de novembro de  2003,
quando ficará revogado o Comunicado 8.804, de 31 de agosto de 2001.

                        Rio de Janeiro, 13 de novembro de 2003.

                        Departamento de Operações
                        do Mercado Aberto - Demab

                        Ivan Luís Gonçalves de Oliveira Lima
                        Chefe, em exercício
```
