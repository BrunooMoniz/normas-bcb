---
titulo: "Carta Circular Nº 3.254"
orgao: "Banco Central do Brasil"
tipo: "Carta Circular"
numero: "3254"
data: 2006-12-08
ementa: "Divulga leiaute das informações de que trata a Circular 3.290, de 2005."
revogada: true
responsavel: "DECIC"
versao_texto: "texto do portal do BCB"
atualizacoes: ["Carta Circular BCB nº 3.454/2010 - Revogação total."]
normas_vinculadas: ["CARTA CIRCULAR 3454/2010", "CARTA CIRCULAR 3341/2008", "CARTA CIRCULAR 3260/2006", "CIRCULAR 3290/2005"]
referencias: ["Circular BCB nº 3.290/2005, art. 5º, parágrafo único."]
fonte: "https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Carta%20Circular&numero=3254"
baixado_em: 2026-11-10
---
# Carta Circular Nº 3.254

```
                      CARTA-CIRCULAR N. 003254
                      ------------------------
                                    Divulga  leiaute das  informações
                                    de  que  trata a Circular  3.290,
                                    de 2005.

                  Em conformidade com o contido no parágrafo único do
artigo  5º da Circular 3.290, de 5.9.2005, divulgamos leiaute  a  ser
adotado para prestação das informações ali previstas:

Seq   Campo    Tipo Tamanho  Decimais   DESCRIÇÃO       OBSERVAÇÕES
=====================================================================
 1  Nome do     A     30                             Sem  acentuações
    cliente                                          e cedilha.
---------------------------------------------------------------------
 2  Tipo        A      1              Tipo do  paga-
                                      dor ou recebe-
                                      dor:
                                      Pessoa  Física
                                      (1)  ou Pessoa
                                      Jurídica (2)
---------------------------------------------------------------------
 3  CPF/CNPJ    A     14              CPF  ou   CNPJ CNPJ  ou CPF  se
    do                                do cliente.    ponto, traço  ou
    cliente                                          barra, com  ali-
                                                     nhamento  à  di-
                                                     reita.
---------------------------------------------------------------------
 4  Código      A      5              Código         Código com dígi-
    Sisbacen                          Sisbacen da    tos,  se  ponto,
                                      instituição    barra ou  depen-
                                      do  cliente    dência.
---------------------------------------------------------------------
 5  Agência     A     10              Código      da Código sem traço
    (se for o                         agência deten- e   sem   dígito
    caso)                             tora da conta, verificador ali-
                                      quando se tra- nhado à direita.
                                      tar de cliente
---------------------------------------------------------------------
 6  Conta  (se  A     20              Número      da Número  completo
    for      o                        conta   quando da    conta   de
    caso)                             se  tratar  de relacionamento,
                                      cliente.       com dígito veri-
                                                     ficador,sem pon-
                                                     tos  ou  traços,
                                                     alinhado  à  di-
                                                     ta.
---------------------------------------------------------------------
 7  Data        D      8              Data       da  DDMMAAAA.
                                      movimentação
                                      dos recursos.
---------------------------------------------------------------------
 8  D/C         A      1              Informar se o  D  =   Pagamento
                                      evento  é  de  (Débito)
                                      débito         C  = Recebimento
                                      (pagamento)    (Crédito)
                                      ou     crédito
                                      (recebimento).
---------------------------------------------------------------------
 9  Histórico   A     30              Descrição   do
                                      débito  ou  do
                                      crédito.
---------------------------------------------------------------------
10  Documento   A     10              Número      do
    (se for o                         documento   do
    caso)                             débito  ou  do
                                      crédito.
---------------------------------------------------------------------
11  Valor       N     15        2     Valor       do Duas       casas
                                      débito  ou  do decimais
                                      crédito.       incluídas     no
                                                     tamanho       do
                                                     campo, sem ponto
                                                     ou      vírgula,
                                                     alinhado       à
                                                     direita.
---------------------------------------------------------------------
12  Nome do    A      30              Nome        do Sem  acentuações
    pagador                           destinatário   e cedilha.
    ou                                ou   recebedor
    recebedor                         dos   recursos
                                      (no  caso   de
                                      débito), ou do
                                      depositante
                                      ou   remetente
                                      dos   recursos
                                      (no  caso   de
                                      crédito).
---------------------------------------------------------------------
13  Tipo        A      1              Tipo        do
                                      pagador     ou
                                      recebedor:
                                      Pessoa  Física
                                      (1),    Pessoa
                                      Jurídica   (2)
                                      ou        Não-
                                      residente (3)
---------------------------------------------------------------------
14  CPF/CNPJ/   A     14              CPF,  CNPJ  ou CNPJ ou CPF  sem
    Passaporte                        número      do ponto, traço  ou
    do   paga-                        passaporte  do barra, com  ali-
    dor ou re-                        destinatário   nhamento  à  di-
    cebedor                           ou   recebedor reita.
                                      dos   recursos
                                      (no  caso   de
                                      débito),    ou
                                      dodepositante
                                      ou   remetente
                                      dos   recursos
                                      (no  caso   de
                                      crédito).
---------------------------------------------------------------------
15  Código      A      5              Código         Código com dígi-
    Sisbacen                          Sisbacen    da tos, sem  ponto,
                                      instituição    barra ou  depen-
                                      do  destinatá- dência.
                                      rio ou recebe-
                                      dor dos recur-
                                      sos  (no  caso
                                      de débito), ou
                                      do depositante
                                      ou   remetente
                                      dos   recursos
                                      (no  caso   de
                                      crédito).
---------------------------------------------------------------------
16  Agência     A     10              Código      da Código sem traço
    da                                agência desti- e   sem   dígito
    instituiç                         natária ou re- verificador,
    ão                                cebedora   dos alinhado à   di-
    depositár                         recursos    no reita.
    ia      ou                        caso  de   dé-
    remetente                         bito,  ou   da
    (se for  o                        agência  depo-
    caso)                             sitante ou re-
                                      metente    dos
                                      recursos    no
                                      caso de   cré-
                                      dito.
---------------------------------------------------------------------
17  Conta   na  A         20          Número      da Número  completo
    instituiç                         conta       de da    conta   de
    ão                                relacionamento  relacionamento,
    depositár                         destinatária / com       dígito
    ia      ou                        recebedora dos verificador, sem
    remetente                         recebedora dos pontos        ou
    (se for  o                        recursos   (no traços, alinhado
    caso)                             caso de  débi- à direita.
                                      to),  ou    da
                                      conta de rela-
                                      cionamento  do
                                      depositante  /
                                      remetente  dos
                                      recursos   (no
                                      caso        de
                                      crédito).
---------------------------------------------------------------------

2.                Os arquivos devem ser preparados em formato -texto-
(extensão .txt), com registros de tamanho fixo, padrão -ASCII-,  para
utilização  em  microcomputadores  do  tipo  -PC-,  ser  gerados  sem
cabeçalho e sem -filler-, e os campos numéricos devem ser no  formato
decimal externo ("display", -descompactado- ou -zonado-). No caso  de
ausência  de  informação, preencher com -brancos- os campos  do  tipo
-alfa- (A) e com zeros à esquerda os campos do tipo -numérico- (N).

3.                Havendo  débito e/ou crédito composto por  dois  ou
mais  valores  (por exemplo, depósito constituído por vários  cheques
e/ou  parte  em  espécie,  ou um débito autorizado  para  emissão  de
cheques   administrativos  ou  DOC's),  o   lançamento   deverá   ser
desmembrado  em  tantas  linhas quantas forem  as  parcelas,  devendo
constar    em    cada    linha    a   identificação    completa    do
depositante/remetente ou do destinatário/recebedor.

                                   BRASÍLIA, 08 de dezembro DE 2006.

                       Departamento    de    Combate    a    Ilícitos
                       Financeiros e Supervisão de Câmbio e  Capitais
                       Internacionais

                       Ricardo Liáo
                       Chefe
```
