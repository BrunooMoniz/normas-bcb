---
titulo: "COMUNICADO N. 005885"
orgao: "Banco Central do Brasil"
tipo: "Comunicado"
numero: "5885"
data: 1997-11-04
ementa: "Remessa ao Banco Central de informacoes em meio magnetico e por teleprocessamento - Mudanca em funcao da virada do milenio."
revogada: false
responsavel: "DEINF"
versao_texto: "texto do portal do BCB"
fonte: "https://www.bcb.gov.br/estabilidadefinanceira/exibeoutrasnormas?tipo=Comunicado&numero=5885"
baixado_em: 2026-11-10
---
# COMUNICADO N. 005885

```
                        COMUNICADO N. 005885
                        --------------------

                              Remessa ao Banco Central de informacoes
                              em     meio     magnetico     e     por
                              teleprocessamento -  Mudanca  em funcao
                              da virada do milenio.

          Tendo em  vista  a necessidade  de  adequacao  dos sistemas
eletronicos de  informacao a  virada  do milenio,  comunicamos  que a
partir de 30  de abril de  1998 as informacoes  encaminhadas ao Banco
Central,   atraves   de   meio    magnetico   ou   transmitidas   por
teleprocessamento, somente serao aceitas se estiverem em conformidade
com os modelos anexos, ja contendo o ano  com 4 digitos nos campos de
data.

2.       A  fim de minimizar o impacto  na implementacao da alteracao
informamos que, para o periodo de  transicao compreendido entre 05 de
novembro e a data limite acima, estaremos aceitando os arquivos tanto
nos antigos como nos  novos leiautes, sendo que  os arquivos com novo
leiaute deverao ter seus  meios magneticos identificados externamente
com a expressao .

3.       Adicionalmente,   informamos   que   se   encontram   tambem
disponiveis no SISBACEN  - Sistema  de Informacoes Banco  Central, na
transacao PDIC600 - Dados Recebidos em  Meio Magnetico pelo BACEN, os
novos leiautes dos arquivos.

                        Brasilia, 04 de novembro de 1997.

                        DEPARTAMENTO DE INFORMATICA

                        Roberto Ozu
                        Chefe

Anexos:

DOCUMENTO:  COR   585

     LEIAUTE:  LCOR0001
      IDENTIFICACAO DO
      REGISTRO                1    1 X     1 "Ý" LOW VALUE (VALOR HE-
                                             XADECIMAL "23" EM ASCII
                                             E "7B" EM EBCDIC);
      NOME DO ARQUIVO         2    8 X     7 "ACOR011"
      FILLER                  9  210 X   202 BRANCOS
      CGC DA INSTITUICAO    211  218 9     8 CGC COM 8 POSICOES
      DATA DA REMESSA       219  226 9     8 "AAAAMMDD"

     LEIAUTE:  LCOR0002
      TIPO DE REGISTRO
      (DADOS DO TIPO A)       1    1 X     1 "A" (LETRA A)
      NUMERO DE REF. BACEN    2   10 9     9
      CGC DA INSTITUICAO     11   24 9    14 CGC COM 14 POSICOES
      CONTINUACAO            25   26 9     2 "00"
      DATA DA EMISSAO        27   34 9     8 "AAAAMMDD"
      DATA DE VENCIMENTO     35   42 9     8 "AAAAMMDD"
      NUMERO DA CEDULA       43   59 X    17 CODIF. PROPRIA DO BANCO,
                                             EXCETO CASO CEDULA FILHA
                                             (OP. DE REPASSE), QUANDO
                                             DEVERA CONTER: POS.39/46
                                             = CGC BASICO DA CED.MAE
                                             POS.47/55 = NUM. DE REF.
                                             BACEN DA CEDULA MAE
      VALOR DA CEDULA        60   77 9    18 COM CENTAVOS
      CATEGORIA DO BENEFI-
      CIARIO                 78   81 9     4
      FILLER                 82   83 X     2 BRANCOS
      CGC/CPF                84   94 X    11 PARA PESSOAS JURIDICAS:
      CGC/CPF                95  105 X    11   3 PRIM.POS. = BRANCOS;
      CGC/CPF               106  116 X    11   8 POS.RESTANTES =  CGC
      CGC/CPF               117  127 X    11   BASICO C/ 8 ALGARISMOS
      CGC/CPF               128  138 X    11 PARA PESSOAS FISICAS:
      CGC/CPF               139  149 X    11   CPF COMPLETO COM 11
      CGC/CPF               150  160 X    11 __ALGARISMOS.
      CGC/CPF               161  171 X    11
      CGC/CPF               172  182 X    11
      CGC/CPF               183  193 X    11
      FILLER                194  210 X    17 BRANCOS
      CGC DA INSTITUICAO    211  218 9     8 CGC COM 8 POSICOES
      DATA DA REMESSA       219  226 9     8 "AAAAMMDD"

      TIPO DE REGISTRO
      (DADOS DO TIPO B)       1    1 X     1 "B" (LETRA B)
      NUMERO DE REF. BACEN    2   10 9     9
      CGC DA INSTITUICAO     11   24 9    14
      NUMERO DE ORDEM        25   26 9     2 01 A 50
      FILLER                 27   29 X     3 BRANCOS
      CODIGO DE PROGRAMA/
      FONTE DE RECURSOS      30   33 9     4
      FILLER                 34   40 X     7 BRANCOS
      CODIGO MUNICIPIO       41   46 9     6
      CODIGO EMPREENDIMEN-
      TO                     47   54 9     8
      FILLER                 55   58 X     4 BRANCOS
      PARCELA DO CREDITO     59   76 9    18 COM CENTAVOS
      PARCELA RECURSOS
      PROPRIOS               77   94 9    18 COM CENTAVOS
      PROAGRO ALIQUOTA       95   98 9     4 COM 2 CASAS DECIMAIS
      FILLER                 99  100 X     2 BRANCOS
      JUROS                 101  105 9     5 COM 2 CASAS DECIMAIS
      FILLER                106  109 X     4 BRANCOS
      AREA EM HECTARES      110  118 9     9 COM 2 CASAS DECIMAIS
      QUANTIDADE/UNIDADE    119  129 9    11 COM 2 CASAS DECIMAIS
      PREVISAO DE PRODUCAO  130  140 9    11 COM 2 CASAS DECIMAIS
      FILLER                141  144 X     4 BRANCOS
      SAFRA                 145  152 9     8 "AAAAAAAA". EX: 19971998
      CGC/CPF PROPRIET. 1   153  163 X    11 PARA PESSOAS JURIDICAS:
      CGC/CPF PROPRIET. 2   164  174 X    11   3 PRIM. POS. = BRANCOS
                                               8 POS. RESTANTES = CGC
                                                BASICO C/8 ALGARISMOS
                                             PARA PESSOAS FISICAS:
                                                CPF  COMPLETO  COM 11
                                                ALGARISMOS.
      FILLER                175  210 X    36 BRANCOS
      CGC DA INSTITUICAO    211  218 9     8 CGC COM 8 POSICOES
      DATA DA REMESSA       219  226 9     8 "AAAAMMDD"

      TIPO DE REGISTRO
      (DADOS DO TIPO C)       1    1 X     1 "C" (LETRA C)
      NUMERO DE REF. BACEN    2   10 9     9
      CGC DA INSTITUICAO     11   24 9    14 CGC COM 14 POSICOES
      CONTINUACAO            25   26 9     2 "00" P/ALT. QUADRO "A";
                                             "01" A "50" P/ALTERACAO
                                             DO QUADRO "B"
      NUMERO DO CAMPO A      27   28 9     2 NUMERO  DO CAMPO A ALTE-
      ALTERAR                                RAR, CONFORME ABAIXO:
                                             04-AGENCIA
                                             05-DATA EMISSAO,FORMATO:
                                              "AAAAMMDD"
                                             06-DATA VENCIMENTO,
                                              FORMATO : "AAAAMMDD"
                                             07-NUMERO DA CEDULA
                                             08-VALOR DA CEDULA
                                             09-CATEGORIA DO EMITENTE
                                             10-CGC/CPF DO(S) EMITEN-
                                                TE(S)
                                             14-CODIGO DO PROGRAMA
                                             17-CODIGO DO MUNICIPIO
                                             20-CODIGO EMPREEDIMENTO
                                             21-PARCELA DO CREDITO
                                             22-PARCELA REC. PROPRIOS
                                             23-ALIQUOTA PROAGRO
                                             24-JUROS
                                             26-AREA EM HECTARES
                                             27-QUANTIDADE/UNIDADE
                                             28-PREV.PRODUCAO/UNIDADE
                                             29-SAFRA. "AAAAAAAA"
                                               EX: 19971998
                                             30-CGC/CPF PROPRIET. 1
                                             31-CGC/CPF PROPRIET. 2
      DADOS ALTERACAO        29  138 X   110 NOVO DADO (INICIAR DA
                                             POSICAO 1 ATE O NECESSA-
                                             RIO DE ACORDO COM O TA-
                                             MANHO DO DADO A SER AL-
                                             TERADO)
      FILLER                139  210 X    72 BRANCOS
      CGC DA INSTITUICAO    211  218 9     8 CGC DA INSTITUICAO
      DATA DA REMESSA       219  226 9     8 "AAAAMMDD"
      "ADICAO DE QUADRO B"
      TIPO DE REGISTRO
      (DADOS DO TIPO D)       1    1 X     1 "D" (LETRA D)
                              2  220         PREENCHER  COM  A  MESMA
                                             ESTRUTURA  DE  DADOS  DO
                                             TIPO "B"

     LEIAUTE:  LCOR0003
      IDENTIFICACAO DO
      REGISTRO                1    1 X     1 "Ð" HIGH-VALUE (VALOR
                                             HEXADECIMAL "40" EM
                                             ASCII OU "7C" EM EBCDIC)
      NOME DO ARQUIVO         2    8 X     7 "ACOR011"
      NUMERO DE REGISTROS
      GRAVADOS                9   14 9     6 TOTAL DE REGISTROS
                                             GRAVADOS NO ARQUIVO,
                                             INCLUSIVE OS DE CONTROLE
      FILLER                 15  210 X   196 BRANCOS
      CGC DA INSTITUICAO    211  218 9     8 CGC COM 8 POSICOES
      DATA DA REMESSA       219  226 9     8 "AAAAMMDD"

DOCUMENTO:  COS  4010

     LEIAUTE:  LCOS0004
      IDENTIF. DO REGISTRO    1    1 X     1 "Ý" (VALOR  HEXADECIMAL
                                             "23" EM ASCII,E "7B" EM
                                             EBCDIC
                              2    2 X     1 "A" (LETRA A)
                              3    3 9     1 1 (ALGARISMO 1)
      CODIGO DO DOCUMENTO     4    7 9     4
      CGC DA INSTITUICAO      8   21 9    14 CGC COM 14 POSICOES
      FILLER                 22   29 X     8
      DATA DO MOVIMENTO      30   35 9     6 MES E ANO-FORMATO MMAAAA
      FLAG                   36   36 X     1 - CONTERA' O CARATER "*"
                                               NO CASO DO UNICO  OU
                                               ULTIMO ARQUIVO DO  VO-
                                               LUME DE FITA MAGNETICA
                                             - CONTERA' O CARATER "F"
                                               NO CASO DE ARQUIVO  EM
                                               FITA MAGNETICA QUE NAO
                                               FOR  UNICO OU O ULTIMO
                                               DO VOLUME
                                             - CONTERA' O CARATER "D"
                                               NO CASO DE ARQUIVO  EM
                                               DISQUETE
      FILLER                 37   71 X    35

     LEIAUTE:  LCOS0005
      CONTA                   1   10 9    10 CODIGO E DIGITO  VERIFI
                                             CADOR
      FILLER                 11   14 X     4
      VALOR DA COLUNA TO-
      TAL(EM FITA MAGNETI-
      CA)                    15   32 S9   18 VALOR DA COLUNA COM  SI-
                                             NAL
      VALOR DA COLUNA  TO-
      TAL (EM DISQUETE)      15   32 9    18 VALOR ABSOLUTO DA COLUNA
      SINAL (1)              33   33 X     1 - NO CASO DE ARQUIVO  EM
                                               FITA,  PREENCHIDO  COM
                                               BRANCO
                                             - NO CASO  DE ARQUIVO EM
                                               DISQUETE,   PREENCHIDO
                                               COM  O  CARATER "+" OU
                                               BRANCO,   PARA INDICAR
                                               VALOR POSITIVO, OU   O
                                               CARATER "-", PARA  IN-
                                               DICAR VALOR NEGATIVO
      VALOR DA COLUNA REA-
      LIZAVEL/EXIGIVEL ATE
      90 DIAS(EM FITA MAG-
      NETICA)                34   51 S9   18 VALOR DA COLUNA COM  SI-
                                             NAL
      VALOR DA COLUNA REA-
      LIZAVEL/EXIGIVEL ATE
      90 DIAS(EM DISQUETE)   34   51 9    18 VALOR ABSOLUTO DA COLUNA
      SINAL (2)              52   52 X     1 - NO CASO DE ARQUIVO  EM
                                               FITA,  PREENCHIDO  COM
                                               BRANCO
                                             - NO CASO  DE ARQUIVO EM
                                               DISQUETE,   PREENCHIDO
                                               COM  O  CARATER "+" OU
                                               BRANCO,   PARA INDICAR
                                               VALOR POSITIVO, OU   O
                                               CARATER "-", PARA  IN-
                                               DICAR VALOR NEGATIVO
      VALOR DA COLUNA REA-
      LIZAVEL/EXIGIVEL  A
      POS 90 DIAS (EM FI-
      TA MAGNETICA)          53   70 S9   18 VALOR DA COLUNA COM  SI-
                                             NAL
      VALOR DA COLUNA REA-
      LIZAVEL/EXIGIVEL  A
      POS 90 DIAS (EM DIS-
      QUETE)                 53   70 9    18 VALOR ABSOLUTO DA COLUNA
      SINAL (3)              71   71 X     1 - NO CASO DE ARQUIVO  EM
                                               FITA,  PREENCHIDO  COM
                                               BRANCO
                                             - NO CASO  DE ARQUIVO EM
                                               DISQUETE,   PREENCHIDO
                                               COM  O  CARATER "+" OU
                                               BRANCO,   PARA INDICAR
                                               VALOR POSITIVO, OU   O
                                               CARATER "-", PARA  IN-
                                               DICAR VALOR NEGATIVO

     LEIAUTE:  LCOS0006
      IDENTIF. DO REGISTRO    1    1 X     1 "Ð"  (VALOR  HEXADECIMAL
                                             "40" EM ASCII. E "7C" EM
                                             EBCDIC
                              2    2 9     1 1 (ALGARISMO 1)
      NUM. DE REG.GRAVADOS    3    8 9     6 TOTAL DE  REGISTROS GRA-
                                             VADOS NO ARQUIVO, INCLU
                                             SIVE OS DE CONTROLE
      FILLER                  9   71 X    63

DOCUMENTO:  COS  4016

     LEIAUTE:  LCOS0004
      IDENTIF. DO REGISTRO    1    1 X     1 "Ý" (VALOR  HEXADECIMAL
                                             "23" EM ASCII,E "7B" EM
                                             EBCDIC
                              2    2 X     1 "A" (LETRA A)
                              3    3 9     1 1 (ALGARISMO 1)
      CODIGO DO DOCUMENTO     4    7 9     4
      CGC DA INSTITUICAO      8   21 9    14 CGC COM 14 POSICOES
      FILLER                 22   29 X     8
      DATA DO MOVIMENTO      30   35 9     6 MES E ANO-FORMATO MMAAAA
      FLAG                   36   36 X     1 - CONTERA' O CARATER "*"
                                               NO CASO DO UNICO  OU
                                               ULTIMO ARQUIVO DO  VO-
                                               LUME DE FITA MAGNETICA
                                             - CONTERA' O CARATER "F"
                                               NO CASO DE ARQUIVO  EM
                                               FITA MAGNETICA QUE NAO
                                               FOR  UNICO OU O ULTIMO
                                               DO VOLUME
                                             - CONTERA' O CARATER "D"
                                               NO CASO DE ARQUIVO  EM
                                               DISQUETE
      FILLER                 37   71 X    35

     LEIAUTE:  LCOS0005
      CONTA                   1   10 9    10 CODIGO E DIGITO  VERIFI
                                             CADOR
      FILLER                 11   14 X     4
      VALOR DA COLUNA TO-
      TAL(EM FITA MAGNETI-
      CA)                    15   32 S9   18 VALOR DA COLUNA COM  SI-
                                             NAL
      VALOR DA COLUNA  TO-
      TAL (EM DISQUETE)      15   32 9    18 VALOR ABSOLUTO DA COLUNA
      SINAL (1)              33   33 X     1 - NO CASO DE ARQUIVO  EM
                                               FITA,  PREENCHIDO  COM
                                               BRANCO
                                             - NO CASO  DE ARQUIVO EM
                                               DISQUETE,   PREENCHIDO
                                               COM  O  CARATER "+" OU
                                               BRANCO,   PARA INDICAR
                                               VALOR POSITIVO, OU   O
                                               CARATER "-", PARA  IN-
                                               DICAR VALOR NEGATIVO
      VALOR DA COLUNA REA-
      LIZAVEL/EXIGIVEL ATE
      90 DIAS(EM FITA MAG-
      NETICA)                34   51 S9   18 VALOR DA COLUNA COM  SI-
                                             NAL
      VALOR DA COLUNA REA-
      LIZAVEL/EXIGIVEL ATE
      90 DIAS(EM DISQUETE)   34   51 9    18 VALOR ABSOLUTO DA COLUNA
      SINAL (2)              52   52 X     1 - NO CASO DE ARQUIVO  EM
                                               FITA,  PREENCHIDO  COM
                                               BRANCO
                                             - NO CASO  DE ARQUIVO EM
                                               DISQUETE,   PREENCHIDO
                                               COM  O  CARATER "+" OU
                                               BRANCO,   PARA INDICAR
                                               VALOR POSITIVO, OU   O
                                               CARATER "-", PARA  IN-
                                               DICAR VALOR NEGATIVO
      VALOR DA COLUNA REA-
      LIZAVEL/EXIGIVEL  A
      POS 90 DIAS (EM FI-
      TA MAGNETICA)          53   70 S9   18 VALOR DA COLUNA COM  SI-
                                             NAL
      VALOR DA COLUNA REA-
      LIZAVEL/EXIGIVEL  A
      POS 90 DIAS (EM DIS-
      QUETE)                 53   70 9    18 VALOR ABSOLUTO DA COLUNA
      SINAL (3)              71   71 X     1 - NO CASO DE ARQUIVO  EM
                                               FITA,  PREENCHIDO  COM
                                               BRANCO
                                             - NO CASO  DE ARQUIVO EM
                                               DISQUETE,   PREENCHIDO
                                               COM  O  CARATER "+" OU
                                               BRANCO,   PARA INDICAR
                                               VALOR POSITIVO, OU   O
                                               CARATER "-", PARA  IN-
                                               DICAR VALOR NEGATIVO

     LEIAUTE:  LCOS0006
      IDENTIF. DO REGISTRO    1    1 X     1 "Ð"  (VALOR  HEXADECIMAL
                                             "40" EM ASCII. E "7C" EM
                                             EBCDIC
                              2    2 9     1 1 (ALGARISMO 1)
      NUM. DE REG.GRAVADOS    3    8 9     6 TOTAL DE  REGISTROS GRA-
                                             VADOS NO ARQUIVO, INCLU
                                             SIVE OS DE CONTROLE
      FILLER                  9   71 X    63

DOCUMENTO:  COS  4040

     LEIAUTE:  LCOS0007
      IDENTIF. DO REGISTRO    1    1 X     1 "Ý" (VALOR  HEXADECIMAL
                                             "23" EM ASCII,E "7B" EM
                                             EBCDIC
                              2    2 X     1 "A" (LETRA A)
                              3    3 9     1 1 (ALGARISMO 1)
      CODIGO DO DOCUMENTO     4    7 9     4
      CODIGO DO CONGLOME-
      RADO FINANCEIRO         8   15 9     8 COD.DO CONGLOM.C/ 8 POS.
      CGC DA INST. LIDER     16   29 9    14 CGC COM 14 POSICOES
      DATA DO MOVIMENTO      30   35 9     6 MES E ANO-FORMATO MMAAAA
      FLAG                   36   36 X     1 - CONTERA' O CARATER "*"
                                               NO CASO DO UNICO  OU
                                               ULTIMO ARQUIVO DO  VO-
                                               LUME DE FITA MAGNETICA
                                             - CONTERA' O CARATER "F"
                                               NO CASO DE ARQUIVO  EM
                                               FITA MAGNETICA QUE NAO
                                               FOR  UNICO OU O ULTIMO
                                               DO VOLUME
                                             - CONTERA' O CARATER "D"
                                               NO CASO DE ARQUIVO  EM
                                               DISQUETE
      FILLER                 37   71 X    35

     LEIAUTE:  LCOS0008
      CONTA                   1   10 9    10 CODIGO E DIGITO  VERIFI-
                                             CADOR
      FILLER                 11   14 X     4
      VALOR DA COLUNA  A-
      GLUTINADO  (EM  FITA
      MAGNETICA)             15   32 S9   18 VALOR DA COLUNA COM  SI-
                                             NAL
      VALOR DA COLUNA AGLU
      TINADO (EM DISQUETE)   15   32 9    18 VALOR ABSOLUTO DA COLUNA
      SINAL (1)              33   33 X     1 - NO CASO DE ARQUIVO  EM
                                               FITA,  PREENCHIDO  COM
                                               BRANCO
                                             - NO CASO  DE ARQUIVO EM
                                               DISQUETE,   PREENCHIDO
                                               COM  O  CARATER "+" OU
                                               BRANCO,   PARA INDICAR
                                               VALOR POSITIVO, OU   O
                                               CARATER "-", PARA  IN
                                               DICAR VALOR NEGATIVO
      VALOR DA COLUNA ELI-
      MINACOES   (EM  FITA
      MAGNETICA)             34   51 S9   18 VALOR DA COLUNA COM  SI-
                                             NAL
      VALOR DA COLUNA ELI-
      MINACOES (EM DISQUE-
      TE)                    34   51 9    18 VALOR ABSOLUTO DA COLUNA
      SINAL (2)              52   52 X     1 - NO CASO DE ARQUIVO  EM
                                               FITA,  PREENCHIDO  COM
                                               BRANCO
                                             - NO CASO  DE ARQUIVO EM
                                               DISQUETE,   PREENCHIDO
                                               COM  O  CARATER "+" OU
                                               BRANCO,   PARA INDICAR
                                               VALOR POSITIVO, OU   O
                                               CARATER "-", PARA  IN
                                               DICAR VALOR NEGATIVO
      VALOR DA COLUNA CON-
      SOLIDADO  (EM  FITA
      MAGNETICA)             53   70 S9   18 VALOR DA COLUNA COM  SI-
                                             NAL
      VALOR DA COLUNA CON-
      SOLIDADO (EM DISQUE-
      TE)                    53   70 9    18 VALOR ABSOLUTO DA COLUNA
      SINAL (3)              71   71 X     1 - NO CASO DE ARQUIVO  EM
                                               FITA,  PREENCHIDO  COM
                                               BRANCO
                                             - NO CASO  DE ARQUIVO EM
                                               DISQUETE,   PREENCHIDO
                                               COM  O  CARATER "+" OU
                                               BRANCO,   PARA INDICAR
                                               VALOR POSITIVO, OU   O
                                               CARATER "-", PARA  IN-
                                               DICAR VALOR NEGATIVO

     LEIAUTE:  LCOS0009
      IDENTIF. DO REGISTRO    1    1 X     1 "Ð"  (VALOR  HEXADECIMAL
                                             "40" EM ASCII. E "7C" EM
                                             EBCDIC
                              2    2 9     1 1 (ALGARISMO 1)
      NUM. DE REG.GRAVADOS    3    8 9     6 TOTAL DE  REGISTROS GRA-
                                             VADOS NO ARQUIVO, INCLU-
                                             SIVE OS DE CONTROLE
      FILLER                  9   71 X    63

DOCUMENTO:  COS  4046

     LEIAUTE:  LCOS0007
      IDENTIF. DO REGISTRO    1    1 X     1 "Ý" (VALOR  HEXADECIMAL
                                             "23" EM ASCII,E "7B" EM
                                             EBCDIC
                              2    2 X     1 "A" (LETRA A)
                              3    3 9     1 1 (ALGARISMO 1)
      CODIGO DO DOCUMENTO     4    7 9     4
      CODIGO DO CONGLOME-
      RADO FINANCEIRO         8   15 9     8 COD.DO CONGLOM.C/ 8 POS.
      CGC DA INST. LIDER     16   29 9    14 CGC COM 14 POSICOES
      DATA DO MOVIMENTO      30   35 9     6 MES E ANO-FORMATO MMAAAA
      FLAG                   36   36 X     1 - CONTERA' O CARATER "*"
                                               NO CASO DO UNICO  OU
                                               ULTIMO ARQUIVO DO  VO-
                                               LUME DE FITA MAGNETICA
                                             - CONTERA' O CARATER "F"
                                               NO CASO DE ARQUIVO  EM
                                               FITA MAGNETICA QUE NAO
                                               FOR  UNICO OU O ULTIMO
                                               DO VOLUME
                                             - CONTERA' O CARATER "D"
                                               NO CASO DE ARQUIVO  EM
                                               DISQUETE
      FILLER                 37   71 X    35

     LEIAUTE:  LCOS0008
      CONTA                   1   10 9    10 CODIGO E DIGITO  VERIFI-
                                             CADOR
      FILLER                 11   14 X     4
      VALOR DA COLUNA  A-
      GLUTINADO  (EM  FITA
      MAGNETICA)             15   32 S9   18 VALOR DA COLUNA COM  SI-
                                             NAL
      VALOR DA COLUNA AGLU
      TINADO (EM DISQUETE)   15   32 9    18 VALOR ABSOLUTO DA COLUNA
      SINAL (1)              33   33 X     1 - NO CASO DE ARQUIVO  EM
                                               FITA,  PREENCHIDO  COM
                                               BRANCO
                                             - NO CASO  DE ARQUIVO EM
                                               DISQUETE,   PREENCHIDO
                                               COM  O  CARATER "+" OU
                                               BRANCO,   PARA INDICAR
                                               VALOR POSITIVO, OU   O
                                               CARATER "-", PARA  IN
                                               DICAR VALOR NEGATIVO
      VALOR DA COLUNA ELI-
      MINACOES   (EM  FITA
      MAGNETICA)             34   51 S9   18 VALOR DA COLUNA COM  SI-
                                             NAL
      VALOR DA COLUNA ELI-
      MINACOES (EM DISQUE-
      TE)                    34   51 9    18 VALOR ABSOLUTO DA COLUNA
      SINAL (2)              52   52 X     1 - NO CASO DE ARQUIVO  EM
                                               FITA,  PREENCHIDO  COM
                                               BRANCO
                                             - NO CASO  DE ARQUIVO EM
                                               DISQUETE,   PREENCHIDO
                                               COM  O  CARATER "+" OU
                                               BRANCO,   PARA INDICAR
                                               VALOR POSITIVO, OU   O
                                               CARATER "-", PARA  IN
                                               DICAR VALOR NEGATIVO
      VALOR DA COLUNA CON-
      SOLIDADO  (EM  FITA
      MAGNETICA)             53   70 S9   18 VALOR DA COLUNA COM  SI-
                                             NAL
      VALOR DA COLUNA CON-
      SOLIDADO (EM DISQUE-
      TE)                    53   70 9    18 VALOR ABSOLUTO DA COLUNA
      SINAL (3)              71   71 X     1 - NO CASO DE ARQUIVO  EM
                                               FITA,  PREENCHIDO  COM
                                               BRANCO
                                             - NO CASO  DE ARQUIVO EM
                                               DISQUETE,   PREENCHIDO
                                               COM  O  CARATER "+" OU
                                               BRANCO,   PARA INDICAR
                                               VALOR POSITIVO, OU   O
                                               CARATER "-", PARA  IN-
                                               DICAR VALOR NEGATIVO

     LEIAUTE:  LCOS0009
      IDENTIF. DO REGISTRO    1    1 X     1 "Ð"  (VALOR  HEXADECIMAL
                                             "40" EM ASCII. E "7C" EM
                                             EBCDIC
                              2    2 9     1 1 (ALGARISMO 1)
      NUM. DE REG.GRAVADOS    3    8 9     6 TOTAL DE  REGISTROS GRA-
                                             VADOS NO ARQUIVO, INCLU-
                                             SIVE OS DE CONTROLE
      FILLER                  9   71 X    63

DOCUMENTO:  COS  4150

     LEIAUTE:  LCOS0001
      IDENTIF. DO REGISTRO    1    1 X     1 "Ý" (VALOR  HEXADECIMAL
                                             "23" EM ASCII,E "7B" EM
                                             EBCDIC
                              2    2 X     1 "A" (LETRA A)
                              3    3 9     1 1 (ALGARISMO 1)
      CODIGO DO DOCUMENTO     4    7 9     4
      CGC DA INSTITUICAO      8   21 9    14 CGC COM 14 POSICOES
      FILLER                 22   27 X     6
      DATA DO MOVIMENTO      28   33 9     6 MES E ANO-FORMATO MMAAAA
      FLAG                   34   34 X     1 - CONTERA' O CARATER "*"
                                               NO CASO DO UNICO  OU
                                               ULTIMO ARQUIVO DO  VO
                                               LUME DE FITA MAGNETICA
                                             - CONTERA' O CARATER "F"
                                               NO CASO DE ARQUIVO  EM
                                               FITA MAGNETICA QUE NAO
                                               FOR  UNICO OU O ULTIMO
                                               DO VOLUME
                                             - CONTERA' O CARATER "D"
                                               NO CASO DE ARQUIVO  EM
                                               DISQUETE

     LEIAUTE:  LCOS0002
      CONTA                   1   10 9    10 CODIGO E DIGITO  VERIFI
                                             CADOR
      FILLER                 11   14 X     4
      VALOR DA  CONTA  (EM
      FITA MAGNETICA)        15   32 S9   18 VALOR DA CONTA COM SINAL
      VALOR  DA CONTA  (EM
      DISQUETE)              15   32 9    18 VALOR ABSOLUTO DA CONTA
      SINAL DO VALOR         33   33 X     1 - NO CASO DE ARQUIVO  EM
                                               FITA,  PREENCHIDO  COM
                                               BRANCO
                                             - NO CASO DE ARQUIVO  EM
                                               DISQUETE,   PREENCHIDO
                                               COM O CARATER "+"   OU
                                               BRANCO,  PARA  INDICAR
                                               VALOR POSITIVO, OU   O
                                               CARATER "-" PARA INDI
                                               CAR VALOR NEGATIVO
      FILLER                 34   34 X     1

     LEIAUTE:  LCOS0003
      IDENTIF. DO REGISTRO    1    1 X     1 "Ð"  (VALOR  HEXADECIMAL
                                             "40" EM ASCII. E "7C" EM
                                             EBCDIC
                              2    2 9     1 1 (ALGARISMO 1)
      NUM. DE REG.GRAVADOS    3    8 9     6 TOTAL DE  REGISTROS GRA-
                                             VADOS NO ARQUIVO, INCLU-
                                             SIVE OS DE CONTROLE
      FILLER                  9   34 X    26

DOCUMENTO:  COS  4180

     LEIAUTE:  LCOS0010
      IDENTIF. DO REGISTRO    1    1 X     1 "Ý" (VALOR  HEXADECIMAL
                                             "23" EM ASCII,E "7B" EM
                                             EBCDIC
                              2    2 X     1 "A" (LETRA A)
                              3    3 9     1 1 (ALGARISMO 1)
      CODIGO DO DOCUMENTO     4    7 9     4
      CGC DA INSTITUICAO      8   21 9    14 CGC COM 14 POSICOES
      FILLER                 22   27 X     6
      DATA DO MOVIMENTO      28   33 9     6 MES E ANO-FORMATO MMAAAA
      FLAG                   34   34 X     1 - CONTERA' O CARATER "*"
                                               NO CASO DO UNICO  OU
                                               ULTIMO ARQUIVO DO  VO-
                                               LUME DE FITA MAGNETICA
                                             - CONTERA' O CARATER "F"
                                               NO CASO DE ARQUIVO  EM
                                               FITA MAGNETICA QUE NAO
                                               FOR  UNICO OU O ULTIMO
                                               DO VOLUME
                                             - CONTERA' O CARATER "D"
                                               NO CASO DE ARQUIVO  EM
                                               DISQUETE

     LEIAUTE:  LCOS0011
      CGC DA DEPENDENCIA                     PARA OS DOCUMENTOS 4510
                                             E 4780 PREENCHER COM  O
                                             VALOR "999999"
        SEQUENCIAL            1    4 9     4
        DV                    5    6 9     2
      CODIGO DO ITEM (PARA
      ESTAT. BANCARIA)        7    9 9     3
      FILLER (PARA ESTAT.
      BANCARIA               10   14 X     5
      COD-DA-CONTA   (PARA
      BALANCETE PATRIM.)      7   14 9     8
      VALOR  DA CONTA  (EM
      FITA MAGNETICA)        15   32 S9   18 VALOR DA CONTA COM SINAL
      VALOR DA  CONTA  (EM
      DISQUETE)              15   32 9    18 VALOR ABSOLUTO DA CONTA
      SINAL DO VALOR         33   33 X     1 - NO CASO DE ARQUIVO  EM
                                               FITA,  PREENCHIDO  COM
                                               BRANCO
                                             - NO CASO DE ARQUIVO  EM
                                               DISQUETE,   PREENCHIDO
                                               COM O CARATER "+"   OU
                                               BRANCO,  PARA  INDICAR
                                               VALOR POSITIVO, OU   O
                                               CARATER "-" PARA INDI-
                                               CAR VALOR NEGATIVO
      FILLER                 34   34 X     1

     LEIAUTE:  LCOS0012
      IDENTIF. DO REGISTRO    1    1 X     1 "Ð"  (VALOR  HEXADECIMAL
                                             "40" EM ASCII. E "7C" EM
                                             EBCDIC
                              2    2 9     1 1 (ALGARISMO 1)
      NUM. DE REG.GRAVADOS    3    8 9     6 TOTAL DE  REGISTROS GRA-
                                             VADOS NO ARQUIVO, INCLU-
                                             SIVE OS DE CONTROLE
      FILLER                  9   34 X    26

DOCUMENTO:  COS  4250

     LEIAUTE:  LCOS0001
      IDENTIF. DO REGISTRO    1    1 X     1 "Ý" (VALOR  HEXADECIMAL
                                             "23" EM ASCII,E "7B" EM
                                             EBCDIC
                              2    2 X     1 "A" (LETRA A)
                              3    3 9     1 1 (ALGARISMO 1)
      CODIGO DO DOCUMENTO     4    7 9     4
      CGC DA INSTITUICAO      8   21 9    14 CGC COM 14 POSICOES
      FILLER                 22   27 X     6
      DATA DO MOVIMENTO      28   33 9     6 MES E ANO-FORMATO MMAAAA
      FLAG                   34   34 X     1 - CONTERA' O CARATER "*"
                                               NO CASO DO UNICO  OU
                                               ULTIMO ARQUIVO DO  VO
                                               LUME DE FITA MAGNETICA
                                             - CONTERA' O CARATER "F"
                                               NO CASO DE ARQUIVO  EM
                                               FITA MAGNETICA QUE NAO
                                               FOR  UNICO OU O ULTIMO
                                               DO VOLUME
                                             - CONTERA' O CARATER "D"
                                               NO CASO DE ARQUIVO  EM
                                               DISQUETE

     LEIAUTE:  LCOS0002
      CONTA                   1   10 9    10 CODIGO E DIGITO  VERIFI
                                             CADOR
      FILLER                 11   14 X     4
      VALOR DA  CONTA  (EM
      FITA MAGNETICA)        15   32 S9   18 VALOR DA CONTA COM SINAL
      VALOR  DA CONTA  (EM
      DISQUETE)              15   32 9    18 VALOR ABSOLUTO DA CONTA
      SINAL DO VALOR         33   33 X     1 - NO CASO DE ARQUIVO  EM
                                               FITA,  PREENCHIDO  COM
                                               BRANCO
                                             - NO CASO DE ARQUIVO  EM
                                               DISQUETE,   PREENCHIDO
                                               COM O CARATER "+"   OU
                                               BRANCO,  PARA  INDICAR
                                               VALOR POSITIVO, OU   O
                                               CARATER "-" PARA INDI
                                               CAR VALOR NEGATIVO
      FILLER                 34   34 X     1

     LEIAUTE:  LCOS0003
      IDENTIF. DO REGISTRO    1    1 X     1 "Ð"  (VALOR  HEXADECIMAL
                                             "40" EM ASCII. E "7C" EM
                                             EBCDIC
                              2    2 9     1 1 (ALGARISMO 1)
      NUM. DE REG.GRAVADOS    3    8 9     6 TOTAL DE  REGISTROS GRA-
                                             VADOS NO ARQUIVO, INCLU-
                                             SIVE OS DE CONTROLE
      FILLER                  9   34 X    26

DOCUMENTO:  COS  4500

     LEIAUTE:  LCOS0010
      IDENTIF. DO REGISTRO    1    1 X     1 "Ý" (VALOR  HEXADECIMAL
                                             "23" EM ASCII,E "7B" EM
                                             EBCDIC
                              2    2 X     1 "A" (LETRA A)
                              3    3 9     1 1 (ALGARISMO 1)
      CODIGO DO DOCUMENTO     4    7 9     4
      CGC DA INSTITUICAO      8   21 9    14 CGC COM 14 POSICOES
      FILLER                 22   27 X     6
      DATA DO MOVIMENTO      28   33 9     6 MES E ANO-FORMATO MMAAAA
      FLAG                   34   34 X     1 - CONTERA' O CARATER "*"
                                               NO CASO DO UNICO  OU
                                               ULTIMO ARQUIVO DO  VO-
                                               LUME DE FITA MAGNETICA
                                             - CONTERA' O CARATER "F"
                                               NO CASO DE ARQUIVO  EM
                                               FITA MAGNETICA QUE NAO
                                               FOR  UNICO OU O ULTIMO
                                               DO VOLUME
                                             - CONTERA' O CARATER "D"
                                               NO CASO DE ARQUIVO  EM
                                               DISQUETE

     LEIAUTE:  LCOS0011
      CGC DA DEPENDENCIA                     PARA OS DOCUMENTOS 4510
                                             E 4780 PREENCHER COM  O
                                             VALOR "999999"
        SEQUENCIAL            1    4 9     4
        DV                    5    6 9     2
      CODIGO DO ITEM (PARA
      ESTAT. BANCARIA)        7    9 9     3
      FILLER (PARA ESTAT.
      BANCARIA               10   14 X     5
      COD-DA-CONTA   (PARA
      BALANCETE PATRIM.)      7   14 9     8
      VALOR  DA CONTA  (EM
      FITA MAGNETICA)        15   32 S9   18 VALOR DA CONTA COM SINAL
      VALOR DA  CONTA  (EM
      DISQUETE)              15   32 9    18 VALOR ABSOLUTO DA CONTA
      SINAL DO VALOR         33   33 X     1 - NO CASO DE ARQUIVO  EM
                                               FITA,  PREENCHIDO  COM
                                               BRANCO
                                             - NO CASO DE ARQUIVO  EM
                                               DISQUETE,   PREENCHIDO
                                               COM O CARATER "+"   OU
                                               BRANCO,  PARA  INDICAR
                                               VALOR POSITIVO, OU   O
                                               CARATER "-" PARA INDI-
                                               CAR VALOR NEGATIVO
      FILLER                 34   34 X     1

     LEIAUTE:  LCOS0012
      IDENTIF. DO REGISTRO    1    1 X     1 "Ð"  (VALOR  HEXADECIMAL
                                             "40" EM ASCII. E "7C" EM
                                             EBCDIC
                              2    2 9     1 1 (ALGARISMO 1)
      NUM. DE REG.GRAVADOS    3    8 9     6 TOTAL DE  REGISTROS GRA-
                                             VADOS NO ARQUIVO, INCLU-
                                             SIVE OS DE CONTROLE
      FILLER                  9   34 X    26
DOCUMENTO:  COS  4510

     LEIAUTE:  LCOS0010
      IDENTIF. DO REGISTRO    1    1 X     1 "Ý" (VALOR  HEXADECIMAL
                                             "23" EM ASCII,E "7B" EM
                                             EBCDIC
                              2    2 X     1 "A" (LETRA A)
                              3    3 9     1 1 (ALGARISMO 1)
      CODIGO DO DOCUMENTO     4    7 9     4
      CGC DA INSTITUICAO      8   21 9    14 CGC COM 14 POSICOES
      FILLER                 22   27 X     6
      DATA DO MOVIMENTO      28   33 9     6 MES E ANO-FORMATO MMAAAA
      FLAG                   34   34 X     1 - CONTERA' O CARATER "*"
                                               NO CASO DO UNICO  OU
                                               ULTIMO ARQUIVO DO  VO-
                                               LUME DE FITA MAGNETICA
                                             - CONTERA' O CARATER "F"
                                               NO CASO DE ARQUIVO  EM
                                               FITA MAGNETICA QUE NAO
                                               FOR  UNICO OU O ULTIMO
                                               DO VOLUME
                                             - CONTERA' O CARATER "D"
                                               NO CASO DE ARQUIVO  EM
                                               DISQUETE

     LEIAUTE:  LCOS0011
      CGC DA DEPENDENCIA                     PARA OS DOCUMENTOS 4510
                                             E 4780 PREENCHER COM  O
                                             VALOR "999999"
        SEQUENCIAL            1    4 9     4
        DV                    5    6 9     2
      CODIGO DO ITEM (PARA
      ESTAT. BANCARIA)        7    9 9     3
      FILLER (PARA ESTAT.
      BANCARIA               10   14 X     5
      COD-DA-CONTA   (PARA
      BALANCETE PATRIM.)      7   14 9     8
      VALOR  DA CONTA  (EM
      FITA MAGNETICA)        15   32 S9   18 VALOR DA CONTA COM SINAL
      VALOR DA  CONTA  (EM
      DISQUETE)              15   32 9    18 VALOR ABSOLUTO DA CONTA
      SINAL DO VALOR         33   33 X     1 - NO CASO DE ARQUIVO  EM
                                               FITA,  PREENCHIDO  COM
                                               BRANCO
                                             - NO CASO DE ARQUIVO  EM
                                               DISQUETE,   PREENCHIDO
                                               COM O CARATER "+"   OU
                                               BRANCO,  PARA  INDICAR
                                               VALOR POSITIVO, OU   O
                                               CARATER "-" PARA INDI-
                                               CAR VALOR NEGATIVO
      FILLER                 34   34 X     1

     LEIAUTE:  LCOS0012
      IDENTIF. DO REGISTRO    1    1 X     1 "Ð"  (VALOR  HEXADECIMAL
                                             "40" EM ASCII. E "7C" EM
                                             EBCDIC
                              2    2 9     1 1 (ALGARISMO 1)
      NUM. DE REG.GRAVADOS    3    8 9     6 TOTAL DE  REGISTROS GRA-
                                             VADOS NO ARQUIVO, INCLU-
                                             SIVE OS DE CONTROLE
      FILLER                  9   34 X    26

DOCUMENTO:  COS  4780

     LEIAUTE:  LCOS0010
      IDENTIF. DO REGISTRO    1    1 X     1 "Ý" (VALOR  HEXADECIMAL
                                             "23" EM ASCII,E "7B" EM
                                             EBCDIC
                              2    2 X     1 "A" (LETRA A)
                              3    3 9     1 1 (ALGARISMO 1)
      CODIGO DO DOCUMENTO     4    7 9     4
      CGC DA INSTITUICAO      8   21 9    14 CGC COM 14 POSICOES
      FILLER                 22   27 X     6
      DATA DO MOVIMENTO      28   33 9     6 MES E ANO-FORMATO MMAAAA
      FLAG                   34   34 X     1 - CONTERA' O CARATER "*"
                                               NO CASO DO UNICO  OU
                                               ULTIMO ARQUIVO DO  VO-
                                               LUME DE FITA MAGNETICA
                                             - CONTERA' O CARATER "F"
                                               NO CASO DE ARQUIVO  EM
                                               FITA MAGNETICA QUE NAO
                                               FOR  UNICO OU O ULTIMO
                                               DO VOLUME
                                             - CONTERA' O CARATER "D"
                                               NO CASO DE ARQUIVO  EM
                                               DISQUETE

     LEIAUTE:  LCOS0011
      CGC DA DEPENDENCIA                     PARA OS DOCUMENTOS 4510
                                             E 4780 PREENCHER COM  O
                                             VALOR "999999"
        SEQUENCIAL            1    4 9     4
        DV                    5    6 9     2
      CODIGO DO ITEM (PARA
      ESTAT. BANCARIA)        7    9 9     3
      FILLER (PARA ESTAT.
      BANCARIA               10   14 X     5
      COD-DA-CONTA   (PARA
      BALANCETE PATRIM.)      7   14 9     8
      VALOR  DA CONTA  (EM
      FITA MAGNETICA)        15   32 S9   18 VALOR DA CONTA COM SINAL
      VALOR DA  CONTA  (EM
      DISQUETE)              15   32 9    18 VALOR ABSOLUTO DA CONTA
      SINAL DO VALOR         33   33 X     1 - NO CASO DE ARQUIVO  EM
                                               FITA,  PREENCHIDO  COM
                                               BRANCO
                                             - NO CASO DE ARQUIVO  EM
                                               DISQUETE,   PREENCHIDO
                                               COM O CARATER "+"   OU
                                               BRANCO,  PARA  INDICAR
                                               VALOR POSITIVO, OU   O
                                               CARATER "-" PARA INDI-
                                               CAR VALOR NEGATIVO
      FILLER                 34   34 X     1

     LEIAUTE:  LCOS0012
      IDENTIF. DO REGISTRO    1    1 X     1 "Ð"  (VALOR  HEXADECIMAL
                                             "40" EM ASCII. E "7C" EM
                                             EBCDIC
                              2    2 9     1 1 (ALGARISMO 1)
      NUM. DE REG.GRAVADOS    3    8 9     6 TOTAL DE  REGISTROS GRA-
                                             VADOS NO ARQUIVO, INCLU-
                                             SIVE OS DE CONTROLE
      FILLER                  9   34 X    26

DOCUMENTO:  COS  4910

     LEIAUTE:  LCOS0004
      IDENTIF. DO REGISTRO    1    1 X     1 "Ý" (VALOR  HEXADECIMAL
                                             "23" EM ASCII,E "7B" EM
                                             EBCDIC
                              2    2 X     1 "A" (LETRA A)
                              3    3 9     1 1 (ALGARISMO 1)
      CODIGO DO DOCUMENTO     4    7 9     4
      CGC DA INSTITUICAO      8   21 9    14 CGC COM 14 POSICOES
      FILLER                 22   29 X     8
      DATA DO MOVIMENTO      30   35 9     6 MES E ANO-FORMATO MMAAAA
      FLAG                   36   36 X     1 - CONTERA' O CARATER "*"
                                               NO CASO DO UNICO  OU
                                               ULTIMO ARQUIVO DO  VO-
                                               LUME DE FITA MAGNETICA
                                             - CONTERA' O CARATER "F"
                                               NO CASO DE ARQUIVO  EM
                                               FITA MAGNETICA QUE NAO
                                               FOR  UNICO OU O ULTIMO
                                               DO VOLUME
                                             - CONTERA' O CARATER "D"
                                               NO CASO DE ARQUIVO  EM
                                               DISQUETE
      FILLER                 37   71 X    35

     LEIAUTE:  LCOS0005
      CONTA                   1   10 9    10 CODIGO E DIGITO  VERIFI
                                             CADOR
      FILLER                 11   14 X     4
      VALOR DA COLUNA TO-
      TAL(EM FITA MAGNETI-
      CA)                    15   32 S9   18 VALOR DA COLUNA COM  SI-
                                             NAL
      VALOR DA COLUNA  TO-
      TAL (EM DISQUETE)      15   32 9    18 VALOR ABSOLUTO DA COLUNA
      SINAL (1)              33   33 X     1 - NO CASO DE ARQUIVO  EM
                                               FITA,  PREENCHIDO  COM
                                               BRANCO
                                             - NO CASO  DE ARQUIVO EM
                                               DISQUETE,   PREENCHIDO
                                               COM  O  CARATER "+" OU
                                               BRANCO,   PARA INDICAR
                                               VALOR POSITIVO, OU   O
                                               CARATER "-", PARA  IN-
                                               DICAR VALOR NEGATIVO
      VALOR DA COLUNA REA-
      LIZAVEL/EXIGIVEL ATE
      90 DIAS(EM FITA MAG-
      NETICA)                34   51 S9   18 VALOR DA COLUNA COM  SI-
                                             NAL
      VALOR DA COLUNA REA-
      LIZAVEL/EXIGIVEL ATE
      90 DIAS(EM DISQUETE)   34   51 9    18 VALOR ABSOLUTO DA COLUNA
      SINAL (2)              52   52 X     1 - NO CASO DE ARQUIVO  EM
                                               FITA,  PREENCHIDO  COM
                                               BRANCO
                                             - NO CASO  DE ARQUIVO EM
                                               DISQUETE,   PREENCHIDO
                                               COM  O  CARATER "+" OU
                                               BRANCO,   PARA INDICAR
                                               VALOR POSITIVO, OU   O
                                               CARATER "-", PARA  IN-
                                               DICAR VALOR NEGATIVO
      VALOR DA COLUNA REA-
      LIZAVEL/EXIGIVEL  A
      POS 90 DIAS (EM FI-
      TA MAGNETICA)          53   70 S9   18 VALOR DA COLUNA COM  SI-
                                             NAL
      VALOR DA COLUNA REA-
      LIZAVEL/EXIGIVEL  A
      POS 90 DIAS (EM DIS-
      QUETE)                 53   70 9    18 VALOR ABSOLUTO DA COLUNA
      SINAL (3)              71   71 X     1 - NO CASO DE ARQUIVO  EM
                                               FITA,  PREENCHIDO  COM
                                               BRANCO
                                             - NO CASO  DE ARQUIVO EM
                                               DISQUETE,   PREENCHIDO
                                               COM  O  CARATER "+" OU
                                               BRANCO,   PARA INDICAR
                                               VALOR POSITIVO, OU   O
                                               CARATER "-", PARA  IN-
                                               DICAR VALOR NEGATIVO

     LEIAUTE:  LCOS0006
      IDENTIF. DO REGISTRO    1    1 X     1 "Ð"  (VALOR  HEXADECIMAL
                                             "40" EM ASCII. E "7C" EM
                                             EBCDIC
                              2    2 9     1 1 (ALGARISMO 1)
      NUM. DE REG.GRAVADOS    3    8 9     6 TOTAL DE  REGISTROS GRA-
                                             VADOS NO ARQUIVO, INCLU
                                             SIVE OS DE CONTROLE
      FILLER                  9   71 X    63

DOCUMENTO:  COS  4916

     LEIAUTE:  LCOS0004
      IDENTIF. DO REGISTRO    1    1 X     1 "Ý" (VALOR  HEXADECIMAL
                                             "23" EM ASCII,E "7B" EM
                                             EBCDIC
                              2    2 X     1 "A" (LETRA A)
                              3    3 9     1 1 (ALGARISMO 1)
      CODIGO DO DOCUMENTO     4    7 9     4
      CGC DA INSTITUICAO      8   21 9    14 CGC COM 14 POSICOES
      FILLER                 22   29 X     8
      DATA DO MOVIMENTO      30   35 9     6 MES E ANO-FORMATO MMAAAA
      FLAG                   36   36 X     1 - CONTERA' O CARATER "*"
                                               NO CASO DO UNICO  OU
                                               ULTIMO ARQUIVO DO  VO-
                                               LUME DE FITA MAGNETICA
                                             - CONTERA' O CARATER "F"
                                               NO CASO DE ARQUIVO  EM
                                               FITA MAGNETICA QUE NAO
                                               FOR  UNICO OU O ULTIMO
                                               DO VOLUME
                                             - CONTERA' O CARATER "D"
                                               NO CASO DE ARQUIVO  EM
                                               DISQUETE
      FILLER                 37   71 X    35

     LEIAUTE:  LCOS0005
      CONTA                   1   10 9    10 CODIGO E DIGITO  VERIFI
                                             CADOR
      FILLER                 11   14 X     4
      VALOR DA COLUNA TO-
      TAL(EM FITA MAGNETI-
      CA)                    15   32 S9   18 VALOR DA COLUNA COM  SI-
                                             NAL
      VALOR DA COLUNA  TO-
      TAL (EM DISQUETE)      15   32 9    18 VALOR ABSOLUTO DA COLUNA
      SINAL (1)              33   33 X     1 - NO CASO DE ARQUIVO  EM
                                               FITA,  PREENCHIDO  COM
                                               BRANCO
                                             - NO CASO  DE ARQUIVO EM
                                               DISQUETE,   PREENCHIDO
                                               COM  O  CARATER "+" OU
                                               BRANCO,   PARA INDICAR
                                               VALOR POSITIVO, OU   O
                                               CARATER "-", PARA  IN-
                                               DICAR VALOR NEGATIVO
      VALOR DA COLUNA REA-
      LIZAVEL/EXIGIVEL ATE
      90 DIAS(EM FITA MAG-
      NETICA)                34   51 S9   18 VALOR DA COLUNA COM  SI-
                                             NAL
      VALOR DA COLUNA REA-
      LIZAVEL/EXIGIVEL ATE
      90 DIAS(EM DISQUETE)   34   51 9    18 VALOR ABSOLUTO DA COLUNA
      SINAL (2)              52   52 X     1 - NO CASO DE ARQUIVO  EM
                                               FITA,  PREENCHIDO  COM
                                               BRANCO
                                             - NO CASO  DE ARQUIVO EM
                                               DISQUETE,   PREENCHIDO
                                               COM  O  CARATER "+" OU
                                               BRANCO,   PARA INDICAR
                                               VALOR POSITIVO, OU   O
                                               CARATER "-", PARA  IN-
                                               DICAR VALOR NEGATIVO
      VALOR DA COLUNA REA-
      LIZAVEL/EXIGIVEL  A
      POS 90 DIAS (EM FI-
      TA MAGNETICA)          53   70 S9   18 VALOR DA COLUNA COM  SI-
                                             NAL
      VALOR DA COLUNA REA-
      LIZAVEL/EXIGIVEL  A
      POS 90 DIAS (EM DIS-
      QUETE)                 53   70 9    18 VALOR ABSOLUTO DA COLUNA
      SINAL (3)              71   71 X     1 - NO CASO DE ARQUIVO  EM
                                               FITA,  PREENCHIDO  COM
                                               BRANCO
                                             - NO CASO  DE ARQUIVO EM
                                               DISQUETE,   PREENCHIDO
                                               COM  O  CARATER "+" OU
                                               BRANCO,   PARA INDICAR
                                               VALOR POSITIVO, OU   O
                                               CARATER "-", PARA  IN-
                                               DICAR VALOR NEGATIVO

     LEIAUTE:  LCOS0006
      IDENTIF. DO REGISTRO    1    1 X     1 "Ð"  (VALOR  HEXADECIMAL
                                             "40" EM ASCII. E "7C" EM
                                             EBCDIC
                              2    2 9     1 1 (ALGARISMO 1)
      NUM. DE REG.GRAVADOS    3    8 9     6 TOTAL DE  REGISTROS GRA-
                                             VADOS NO ARQUIVO, INCLU
                                             SIVE OS DE CONTROLE
      FILLER                  9   71 X    63

DOCUMENTO:  COS  4950

     LEIAUTE:  LCOS0001
      IDENTIF. DO REGISTRO    1    1 X     1 "Ý" (VALOR  HEXADECIMAL
                                             "23" EM ASCII,E "7B" EM
                                             EBCDIC
                              2    2 X     1 "A" (LETRA A)
                              3    3 9     1 1 (ALGARISMO 1)
      CODIGO DO DOCUMENTO     4    7 9     4
      CGC DA INSTITUICAO      8   21 9    14 CGC COM 14 POSICOES
      FILLER                 22   27 X     6
      DATA DO MOVIMENTO      28   33 9     6 MES E ANO-FORMATO MMAAAA
      FLAG                   34   34 X     1 - CONTERA' O CARATER "*"
                                               NO CASO DO UNICO  OU
                                               ULTIMO ARQUIVO DO  VO
                                               LUME DE FITA MAGNETICA
                                             - CONTERA' O CARATER "F"
                                               NO CASO DE ARQUIVO  EM
                                               FITA MAGNETICA QUE NAO
                                               FOR  UNICO OU O ULTIMO
                                               DO VOLUME
                                             - CONTERA' O CARATER "D"
                                               NO CASO DE ARQUIVO  EM
                                               DISQUETE

     LEIAUTE:  LCOS0002
      CONTA                   1   10 9    10 CODIGO E DIGITO  VERIFI
                                             CADOR
      FILLER                 11   14 X     4
      VALOR DA  CONTA  (EM
      FITA MAGNETICA)        15   32 S9   18 VALOR DA CONTA COM SINAL
      VALOR  DA CONTA  (EM
      DISQUETE)              15   32 9    18 VALOR ABSOLUTO DA CONTA
      SINAL DO VALOR         33   33 X     1 - NO CASO DE ARQUIVO  EM
                                               FITA,  PREENCHIDO  COM
                                               BRANCO
                                             - NO CASO DE ARQUIVO  EM
                                               DISQUETE,   PREENCHIDO
                                               COM O CARATER "+"   OU
                                               BRANCO,  PARA  INDICAR
                                               VALOR POSITIVO, OU   O
                                               CARATER "-" PARA INDI
                                               CAR VALOR NEGATIVO
      FILLER                 34   34 X     1

     LEIAUTE:  LCOS0003
      IDENTIF. DO REGISTRO    1    1 X     1 "Ð"  (VALOR  HEXADECIMAL
                                             "40" EM ASCII. E "7C" EM
                                             EBCDIC
                              2    2 9     1 1 (ALGARISMO 1)
      NUM. DE REG.GRAVADOS    3    8 9     6 TOTAL DE  REGISTROS GRA-
                                             VADOS NO ARQUIVO, INCLU-
                                             SIVE OS DE CONTROLE
      FILLER                  9   34 X    26

DOCUMENTO:  COS  4196

     LEIAUTE:  LCOS0010
      IDENTIF. DO REGISTRO    1    1 X     1 "Ý" (VALOR  HEXADECIMAL
                                             "23" EM ASCII,E "7B" EM
                                             EBCDIC
                              2    2 X     1 "A" (LETRA A)
                              3    3 9     1 1 (ALGARISMO 1)
      CODIGO DO DOCUMENTO     4    7 9     4
      CGC DA INSTITUICAO      8   21 9    14 CGC COM 14 POSICOES
      FILLER                 22   27 X     6
      DATA DO MOVIMENTO      28   33 9     6 MES E ANO-FORMATO MMAAAA
      FLAG                   34   34 X     1 - CONTERA' O CARATER "*"
                                               NO CASO DO UNICO  OU
                                               ULTIMO ARQUIVO DO  VO-
                                               LUME DE FITA MAGNETICA
                                             - CONTERA' O CARATER "F"
                                               NO CASO DE ARQUIVO  EM
                                               FITA MAGNETICA QUE NAO
                                               FOR  UNICO OU O ULTIMO
                                               DO VOLUME
                                             - CONTERA' O CARATER "D"
                                               NO CASO DE ARQUIVO  EM
                                               DISQUETE

     LEIAUTE:  LCOS0011
      CGC DA DEPENDENCIA                     PARA OS DOCUMENTOS 4510
                                             E 4780 PREENCHER COM  O
                                             VALOR "999999"
        SEQUENCIAL            1    4 9     4
        DV                    5    6 9     2
      CODIGO DO ITEM (PARA
      ESTAT. BANCARIA)        7    9 9     3
      FILLER (PARA ESTAT.
      BANCARIA               10   14 X     5
      COD-DA-CONTA   (PARA
      BALANCETE PATRIM.)      7   14 9     8
      VALOR  DA CONTA  (EM
      FITA MAGNETICA)        15   32 S9   18 VALOR DA CONTA COM SINAL
      VALOR DA  CONTA  (EM
      DISQUETE)              15   32 9    18 VALOR ABSOLUTO DA CONTA
      SINAL DO VALOR         33   33 X     1 - NO CASO DE ARQUIVO  EM
                                               FITA,  PREENCHIDO  COM
                                               BRANCO
                                             - NO CASO DE ARQUIVO  EM
                                               DISQUETE,   PREENCHIDO
                                               COM O CARATER "+"   OU
                                               BRANCO,  PARA  INDICAR
                                               VALOR POSITIVO, OU   O
                                               CARATER "-" PARA INDI-
                                               CAR VALOR NEGATIVO
      FILLER                 34   34 X     1

     LEIAUTE:  LCOS0012
      IDENTIF. DO REGISTRO    1    1 X     1 "Ð"  (VALOR  HEXADECIMAL
                                             "40" EM ASCII. E "7C" EM
                                             EBCDIC
                              2    2 9     1 1 (ALGARISMO 1)
      NUM. DE REG.GRAVADOS    3    8 9     6 TOTAL DE  REGISTROS GRA-
                                             VADOS NO ARQUIVO, INCLU-
                                             SIVE OS DE CONTROLE
      FILLER                  9   34 X    26

DOCUMENTO:  COS  4796

     LEIAUTE:  LCOS0010
      IDENTIF. DO REGISTRO    1    1 X     1 "Ý" (VALOR  HEXADECIMAL
                                             "23" EM ASCII,E "7B" EM
                                             EBCDIC
                              2    2 X     1 "A" (LETRA A)
                              3    3 9     1 1 (ALGARISMO 1)
      CODIGO DO DOCUMENTO     4    7 9     4
      CGC DA INSTITUICAO      8   21 9    14 CGC COM 14 POSICOES
      FILLER                 22   27 X     6
      DATA DO MOVIMENTO      28   33 9     6 MES E ANO-FORMATO MMAAAA
      FLAG                   34   34 X     1 - CONTERA' O CARATER "*"
                                               NO CASO DO UNICO  OU
                                               ULTIMO ARQUIVO DO  VO-
                                               LUME DE FITA MAGNETICA
                                             - CONTERA' O CARATER "F"
                                               NO CASO DE ARQUIVO  EM
                                               FITA MAGNETICA QUE NAO
                                               FOR  UNICO OU O ULTIMO
                                               DO VOLUME
                                             - CONTERA' O CARATER "D"
                                               NO CASO DE ARQUIVO  EM
                                               DISQUETE

     LEIAUTE:  LCOS0011
      CGC DA DEPENDENCIA                     PARA OS DOCUMENTOS 4510
                                             E 4780 PREENCHER COM  O
                                             VALOR "999999"
        SEQUENCIAL            1    4 9     4
        DV                    5    6 9     2
      CODIGO DO ITEM (PARA
      ESTAT. BANCARIA)        7    9 9     3
      FILLER (PARA ESTAT.
      BANCARIA               10   14 X     5
      COD-DA-CONTA   (PARA
      BALANCETE PATRIM.)      7   14 9     8
      VALOR  DA CONTA  (EM
      FITA MAGNETICA)        15   32 S9   18 VALOR DA CONTA COM SINAL
      VALOR DA  CONTA  (EM
      DISQUETE)              15   32 9    18 VALOR ABSOLUTO DA CONTA
      SINAL DO VALOR         33   33 X     1 - NO CASO DE ARQUIVO  EM
                                               FITA,  PREENCHIDO  COM
                                               BRANCO
                                             - NO CASO DE ARQUIVO  EM
                                               DISQUETE,   PREENCHIDO
                                               COM O CARATER "+"   OU
                                               BRANCO,  PARA  INDICAR
                                               VALOR POSITIVO, OU   O
                                               CARATER "-" PARA INDI-
                                               CAR VALOR NEGATIVO
      FILLER                 34   34 X     1

     LEIAUTE:  LCOS0012
      IDENTIF. DO REGISTRO    1    1 X     1 "Ð"  (VALOR  HEXADECIMAL
                                             "40" EM ASCII. E "7C" EM
                                             EBCDIC
                              2    2 9     1 1 (ALGARISMO 1)
      NUM. DE REG.GRAVADOS    3    8 9     6 TOTAL DE  REGISTROS GRA-
                                             VADOS NO ARQUIVO, INCLU-
                                             SIVE OS DE CONTROLE
      FILLER                  9   34 X    26

DOCUMENTO:  COS  4350

     LEIAUTE:  LCOS0001
      IDENTIF. DO REGISTRO    1    1 X     1 "Ý" (VALOR  HEXADECIMAL
                                             "23" EM ASCII,E "7B" EM
                                             EBCDIC
                              2    2 X     1 "A" (LETRA A)
                              3    3 9     1 1 (ALGARISMO 1)
      CODIGO DO DOCUMENTO     4    7 9     4
      CGC DA INSTITUICAO      8   21 9    14 CGC COM 14 POSICOES
      FILLER                 22   27 X     6
      DATA DO MOVIMENTO      28   33 9     6 MES E ANO-FORMATO MMAAAA
      FLAG                   34   34 X     1 - CONTERA' O CARATER "*"
                                               NO CASO DO UNICO  OU
                                               ULTIMO ARQUIVO DO  VO
                                               LUME DE FITA MAGNETICA
                                             - CONTERA' O CARATER "F"
                                               NO CASO DE ARQUIVO  EM
                                               FITA MAGNETICA QUE NAO
                                               FOR  UNICO OU O ULTIMO
                                               DO VOLUME
                                             - CONTERA' O CARATER "D"
                                               NO CASO DE ARQUIVO  EM
                                               DISQUETE

     LEIAUTE:  LCOS0002
      CONTA                   1   10 9    10 CODIGO E DIGITO  VERIFI
                                             CADOR
      FILLER                 11   14 X     4
      VALOR DA  CONTA  (EM
      FITA MAGNETICA)        15   32 S9   18 VALOR DA CONTA COM SINAL
      VALOR  DA CONTA  (EM
      DISQUETE)              15   32 9    18 VALOR ABSOLUTO DA CONTA
      SINAL DO VALOR         33   33 X     1 - NO CASO DE ARQUIVO  EM
                                               FITA,  PREENCHIDO  COM
                                               BRANCO
                                             - NO CASO DE ARQUIVO  EM
                                               DISQUETE,   PREENCHIDO
                                               COM O CARATER "+"   OU
                                               BRANCO,  PARA  INDICAR
                                               VALOR POSITIVO, OU   O
                                               CARATER "-" PARA INDI
                                               CAR VALOR NEGATIVO
      FILLER                 34   34 X     1

     LEIAUTE:  LCOS0003
      IDENTIF. DO REGISTRO    1    1 X     1 "Ð"  (VALOR  HEXADECIMAL
                                             "40" EM ASCII. E "7C" EM
                                             EBCDIC
                              2    2 9     1 1 (ALGARISMO 1)
      NUM. DE REG.GRAVADOS    3    8 9     6 TOTAL DE  REGISTROS GRA-
                                             VADOS NO ARQUIVO, INCLU-
                                             SIVE OS DE CONTROLE
      FILLER                  9   34 X    26

DOCUMENTO:  COS  4110

     LEIAUTE:  LCOS0013
      IDENTIF. DO REGISTRO    1    1 X     1 "Ý" (VALOR HEXADECIMAL
                                             "23" EM ASCII, E "7B" EM
                                             EBCDIC)
                              2    2 X     1 "A" (LETRA A)
                              3    3 9     1 1 (ALGARISMO 1)
      CODIGO DO DOCUMENTO     4    7 9     4
      CGC DA INSTITUICAO      8   21 9    14 CGC COM 14 POSICOES
      FILLER                 22   29 X     8
      DATA DO MOVIMENTO      30   35 9     6 MES E ANO-FORMATO MMAAAA
      FLAG                   36   36 X     1 - CONTERA' O CARATER "*"
                                               NO CASO DO UNICO OU
                                               ULTIMO ARQUIVO NO VO-
                                               LUME DE FITA MAGNETICA
                                             - CONTERA' O CARATER "F"
                                               NO CASO DE ARQUIVO EM
                                               FITA MAGNETICA QUE NAO
                                               FOR UNICO OU O ULTIMO
                                               DO VOLUME
                                             - CONTERA' O CARATER "D"
                                               NO CASO DE QRQUIVO EM
                                               DISQUETE
      FILLER                 37   71 X    35

     LEIAUTE:  LCOS0014
      CONTA                   1   10 9    10 CODIGO E DIGITO VERIFI-
                                             CADOR
      FILLER                 11   14 X     4
      VALOR DA COLUNA TO-
      TAL (EM FITA MAGNETI
      CA)                    15   32 S9   18 VALOR DA COLUNA COM SI-
                                             NAL
      VALOR DA COLUNA TO-
      TAL (EM DISQUETE)      15   32 9    18 VALOR ABSOLUTO DA COLUNA
      SINAL (1)              33   33 X     1 - NO CASO DE ARQUIVO EM
                                               FITA, PREENCHIDO COM
                                               BRANCO
                                             - NO CASO DE ARQUIVO EM
                                               DISQUETE, PREENCHIDO
                                               COM O CARATER "+" OU
                                               BRANCO, PARA INDICAR
                                               VALOR POSITIVO, OU O
                                               CARATER "-" PARA IN-
                                               DICAR VALOR NEGATIVO
      FILLER                 34   71 X    38 PREENCHER COM ZEROS

     LEIAUTE:  LCOS0015
      IDENTIF. DO REGISTRO    1    1 X     1 "Ð" (VALOR HEXADECIMAL
                                             "40" EM ASCII, E "7C" EM
                                             EBCDIC)
                              2    2 9     1 1 (ALGARISMO 1)
      NUM. DE REG.GRAVADOS    3    8 9     6 TOTAL DE REGISTROS GRA-
                                             VADOS NO ARQUIVO, INCLU-
                                             SIVE OS DE CONTROLE.
      FILLER                  9   71 X    63

DOCUMENTO:  COS  4020

     LEIAUTE:  LCOS0004
      IDENTIF. DO REGISTRO    1    1 X     1 "Ý" (VALOR  HEXADECIMAL
                                             "23" EM ASCII,E "7B" EM
                                             EBCDIC
                              2    2 X     1 "A" (LETRA A)
                              3    3 9     1 1 (ALGARISMO 1)
      CODIGO DO DOCUMENTO     4    7 9     4
      CGC DA INSTITUICAO      8   21 9    14 CGC COM 14 POSICOES
      FILLER                 22   29 X     8
      DATA DO MOVIMENTO      30   35 9     6 MES E ANO-FORMATO MMAAAA
      FLAG                   36   36 X     1 - CONTERA' O CARATER "*"
                                               NO CASO DO UNICO  OU
                                               ULTIMO ARQUIVO DO  VO-
                                               LUME DE FITA MAGNETICA
                                             - CONTERA' O CARATER "F"
                                               NO CASO DE ARQUIVO  EM
                                               FITA MAGNETICA QUE NAO
                                               FOR  UNICO OU O ULTIMO
                                               DO VOLUME
                                             - CONTERA' O CARATER "D"
                                               NO CASO DE ARQUIVO  EM
                                               DISQUETE
      FILLER                 37   71 X    35

     LEIAUTE:  LCOS0005
      CONTA                   1   10 9    10 CODIGO E DIGITO  VERIFI
                                             CADOR
      FILLER                 11   14 X     4
      VALOR DA COLUNA TO-
      TAL(EM FITA MAGNETI-
      CA)                    15   32 S9   18 VALOR DA COLUNA COM  SI-
                                             NAL
      VALOR DA COLUNA  TO-
      TAL (EM DISQUETE)      15   32 9    18 VALOR ABSOLUTO DA COLUNA
      SINAL (1)              33   33 X     1 - NO CASO DE ARQUIVO  EM
                                               FITA,  PREENCHIDO  COM
                                               BRANCO
                                             - NO CASO  DE ARQUIVO EM
                                               DISQUETE,   PREENCHIDO
                                               COM  O  CARATER "+" OU
                                               BRANCO,   PARA INDICAR
                                               VALOR POSITIVO, OU   O
                                               CARATER "-", PARA  IN-
                                               DICAR VALOR NEGATIVO
      VALOR DA COLUNA REA-
      LIZAVEL/EXIGIVEL ATE
      90 DIAS(EM FITA MAG-
      NETICA)                34   51 S9   18 VALOR DA COLUNA COM  SI-
                                             NAL
      VALOR DA COLUNA REA-
      LIZAVEL/EXIGIVEL ATE
      90 DIAS(EM DISQUETE)   34   51 9    18 VALOR ABSOLUTO DA COLUNA
      SINAL (2)              52   52 X     1 - NO CASO DE ARQUIVO  EM
                                               FITA,  PREENCHIDO  COM
                                               BRANCO
                                             - NO CASO  DE ARQUIVO EM
                                               DISQUETE,   PREENCHIDO
                                               COM  O  CARATER "+" OU
                                               BRANCO,   PARA INDICAR
                                               VALOR POSITIVO, OU   O
                                               CARATER "-", PARA  IN-
                                               DICAR VALOR NEGATIVO
      VALOR DA COLUNA REA-
      LIZAVEL/EXIGIVEL  A
      POS 90 DIAS (EM FI-
      TA MAGNETICA)          53   70 S9   18 VALOR DA COLUNA COM  SI-
                                             NAL
      VALOR DA COLUNA REA-
      LIZAVEL/EXIGIVEL  A
      POS 90 DIAS (EM DIS-
      QUETE)                 53   70 9    18 VALOR ABSOLUTO DA COLUNA
      SINAL (3)              71   71 X     1 - NO CASO DE ARQUIVO  EM
                                               FITA,  PREENCHIDO  COM
                                               BRANCO
                                             - NO CASO  DE ARQUIVO EM
                                               DISQUETE,   PREENCHIDO
                                               COM  O  CARATER "+" OU
                                               BRANCO,   PARA INDICAR
                                               VALOR POSITIVO, OU   O
                                               CARATER "-", PARA  IN-
                                               DICAR VALOR NEGATIVO

     LEIAUTE:  LCOS0006
      IDENTIF. DO REGISTRO    1    1 X     1 "Ð"  (VALOR  HEXADECIMAL
                                             "40" EM ASCII. E "7C" EM
                                             EBCDIC
                              2    2 9     1 1 (ALGARISMO 1)
      NUM. DE REG.GRAVADOS    3    8 9     6 TOTAL DE  REGISTROS GRA-
                                             VADOS NO ARQUIVO, INCLU
                                             SIVE OS DE CONTROLE
      FILLER                  9   71 X    63

DOCUMENTO:  COS  4026

     LEIAUTE:  LCOS0004
      IDENTIF. DO REGISTRO    1    1 X     1 "Ý" (VALOR  HEXADECIMAL
                                             "23" EM ASCII,E "7B" EM
                                             EBCDIC
                              2    2 X     1 "A" (LETRA A)
                              3    3 9     1 1 (ALGARISMO 1)
      CODIGO DO DOCUMENTO     4    7 9     4
      CGC DA INSTITUICAO      8   21 9    14 CGC COM 14 POSICOES
      FILLER                 22   29 X     8
      DATA DO MOVIMENTO      30   35 9     6 MES E ANO-FORMATO MMAAAA
      FLAG                   36   36 X     1 - CONTERA' O CARATER "*"
                                               NO CASO DO UNICO  OU
                                               ULTIMO ARQUIVO DO  VO-
                                               LUME DE FITA MAGNETICA
                                             - CONTERA' O CARATER "F"
                                               NO CASO DE ARQUIVO  EM
                                               FITA MAGNETICA QUE NAO
                                               FOR  UNICO OU O ULTIMO
                                               DO VOLUME
                                             - CONTERA' O CARATER "D"
                                               NO CASO DE ARQUIVO  EM
                                               DISQUETE
      FILLER                 37   71 X    35

     LEIAUTE:  LCOS0005
      CONTA                   1   10 9    10 CODIGO E DIGITO  VERIFI
                                             CADOR
      FILLER                 11   14 X     4
      VALOR DA COLUNA TO-
      TAL(EM FITA MAGNETI-
      CA)                    15   32 S9   18 VALOR DA COLUNA COM  SI-
                                             NAL
      VALOR DA COLUNA  TO-
      TAL (EM DISQUETE)      15   32 9    18 VALOR ABSOLUTO DA COLUNA
      SINAL (1)              33   33 X     1 - NO CASO DE ARQUIVO  EM
                                               FITA,  PREENCHIDO  COM
                                               BRANCO
                                             - NO CASO  DE ARQUIVO EM
                                               DISQUETE,   PREENCHIDO
                                               COM  O  CARATER "+" OU
                                               BRANCO,   PARA INDICAR
                                               VALOR POSITIVO, OU   O
                                               CARATER "-", PARA  IN-
                                               DICAR VALOR NEGATIVO
      VALOR DA COLUNA REA-
      LIZAVEL/EXIGIVEL ATE
      90 DIAS(EM FITA MAG-
      NETICA)                34   51 S9   18 VALOR DA COLUNA COM  SI-
                                             NAL
      VALOR DA COLUNA REA-
      LIZAVEL/EXIGIVEL ATE
      90 DIAS(EM DISQUETE)   34   51 9    18 VALOR ABSOLUTO DA COLUNA
      SINAL (2)              52   52 X     1 - NO CASO DE ARQUIVO  EM
                                               FITA,  PREENCHIDO  COM
                                               BRANCO
                                             - NO CASO  DE ARQUIVO EM
                                               DISQUETE,   PREENCHIDO
                                               COM  O  CARATER "+" OU
                                               BRANCO,   PARA INDICAR
                                               VALOR POSITIVO, OU   O
                                               CARATER "-", PARA  IN-
                                               DICAR VALOR NEGATIVO
      VALOR DA COLUNA REA-
      LIZAVEL/EXIGIVEL  A
      POS 90 DIAS (EM FI-
      TA MAGNETICA)          53   70 S9   18 VALOR DA COLUNA COM  SI-
                                             NAL
      VALOR DA COLUNA REA-
      LIZAVEL/EXIGIVEL  A
      POS 90 DIAS (EM DIS-
      QUETE)                 53   70 9    18 VALOR ABSOLUTO DA COLUNA
      SINAL (3)              71   71 X     1 - NO CASO DE ARQUIVO  EM
                                               FITA,  PREENCHIDO  COM
                                               BRANCO
                                             - NO CASO  DE ARQUIVO EM
                                               DISQUETE,   PREENCHIDO
                                               COM  O  CARATER "+" OU
                                               BRANCO,   PARA INDICAR
                                               VALOR POSITIVO, OU   O
                                               CARATER "-", PARA  IN-
                                               DICAR VALOR NEGATIVO

     LEIAUTE:  LCOS0006
      IDENTIF. DO REGISTRO    1    1 X     1 "Ð"  (VALOR  HEXADECIMAL
                                             "40" EM ASCII. E "7C" EM
                                             EBCDIC
                              2    2 9     1 1 (ALGARISMO 1)
      NUM. DE REG.GRAVADOS    3    8 9     6 TOTAL DE  REGISTROS GRA-
                                             VADOS NO ARQUIVO, INCLU
                                             SIVE OS DE CONTROLE
      FILLER                  9   71 X    63

DOCUMENTO:  DIP  1010

     LEIAUTE:  LDIP0001
      IDENTIFICACAO           1    1 A     1 PREENCHER COM Ý (VALOR
                                             HEXADECIMAL "23" ASCII E
                                             "7B" EM EBCDIC
                              2    2 A     1 CONTERA "A"(LETRA "A")
                              3    3 A     1 CONTERA "1"(ALGARISMO 1)
      CODIGO DOCUMENTO        4    7 N     4 PREENCHER COM "1010"
      CGC INSTITUICAO         8   21 N    14 CGC DA INSTITUICAO
      NUMERO DA REMESSA      22   29 N     8 PREENCHER NO FORMATO
                                             "AAAANNNN" ONDE AAAA=ANO
                                             E NNNN=SEQUENCIAL REMES-
                                             SA
      DATA REMESSA           30   37 N     8 DATA ENVIO DA REMESSA EM
                                             AAAAMMDD (ANO,MES E DIA)
      MEIO MAGNETICO         38   38 A     1 PREENCHER COM F (FITA)
      FILLER                 39  374 A   336 CONTEM BRANCOS

     LEIAUTE:  LDIP0002
      DADOS BASICOS OPER.                    1 UNICO REG POR OPERACAO
      TIPO DE REGISTRO        1    1 N     1 CONTEM "1" IDENTIFICANDO
                                             DADOS BASICOS OPERACAO
      NUMERO CREDOR           2   31 A    30 MNEMONICO DA IF QUE IDEN
                                             TIFICA INTERNAMENTE UMA
                                             DADA OPERACAO DE CREDITO
      CGC CREDOR             32   45 N    14 IDENTIFICACAO DA UNIDADE
                                             DA IF QUE EFETUOU A OPE-
                                             RACAO DE CREDITO COM A
                                             ENTIDADE DO SETOR PUBL.
      CONTA COSIF            46   55 N    10 IDENTIFICA O CODIGO DA
                                             CONTA COSIF EM QUE A OPE
                                             RACAO SERA CONTABILIZADA
      CGC TOMADOR            56   69 N    14 CGC DA ENTIDADE TOMADO-
                                             RA DE RECURSOS FINANC.
      MUNICIPIO TOMADOR      70  107 A    38 NOME DO MUNICIPIO DE DO-
                                             MICILIO DO TOMADOR.
      UF TOMADOR            108  109 A     2 SIGLA DA UF ONDE SE SI-
                                             TUA O MUN. DO TOMADOR.
      CGC GARANTIDOR        110  123 N    14 CGC DA ENTIDADE PRESTA-
                                             DORA DE GARANTIA.
      MUNICIPIO GARANTIDOR  124  161 A    38 NOME DO MUNICIPIO DE DO-
                                             MICILIO DO GARANTIDOR.
      UF GARANTIDOR         162  163 A     2 SIGLA DA UF ONDE SE SI-
                                             TUA O MUN. DO GARANTIDOR
      DATA CONTRATAC.OPER.  164  171 N     8 DATA EM QUE O CONTRATO
                                             DA OPERACAO DE CREDITO,
                                             FOI ASSINADO.(DDMMAAAA)
      MOEDA OPERACAO        172  174 N     3 CODIGO QUE IDENTIFICA A
                                             MOEDA EM QUE A OPERACAO.
                                             FOI CONTRATADA.
                                             (VER TABELA).
      UPF OPERACAO          175  179 N     5 VALOR EM UPF DA OPERACAO
                                             (SE CONTRATADAS EM UPF).
      VALOR OPERACAO        180  197 N    18 VALOR DO PRINCIPAL DA O-
                                             PERACAO NA MOEDA EM QUE
                                             FOI CONTRATADA (INCLUIN-
                                             DO CENTAVOS).
      VALOR ENCARGOS        198  205 N     8 TAXA DE ENCARGOS PACTUA-
                                             DA PARA A OPERACAO COM 4
                                             INTEIROS E 4 DECIMAIS.
                                             (VER TABELA).
      PERIODO ENCARGO       206  206 N     1 IDENTIFICA A ABRANGENCIA
                                             TEMPORAL REFERENTE A TA-
                                             XA PACTUADA.(VER TABELA)
      TIPO ENCARGO          207  207 N     1 IDENTIFICA SE A TAXA E'
                                             ANTECIPADA OU POSTECIPA-
                                             DA.(VER TABELA)
      CAPITALIZACAO         208  208 N     1 INDICA SE O REGIME DE
                                             CAPITALIZACAO DE TAXA E'
                                             SIMPLES OU COMPOSTO.
                                             (VER TABELA).
      PREFIXADA             209  209 N     1 INDICA SE A OPERACAO DE
                                             CREDITO E' OU NAO INDEXA
                                             DA.(1-SIM 2-NAO).
      INDICE ATUALIZACAO    210  215 A     6 INDICA FATOR DE ATUALIZA
                                             CAO MONETARIA PACTUADO
                                             QUANDO DA REALIZACAO DA
                                             OPERACAO DE CREDITO.
                                             SO DEVE SER PREENCHIDO
                                             QUANDO INDEXADA = 2
      FONTE RECURSOS OPER.  216  218 N     3 IDENTIFICA ORIGEM DOS RE
                                             CURSOS UTILIZADOS PELA
                                             INSTITUICAO NA OPER. DE
                                             CREDITO COM ENTIDADES DO
                                             SETOR PUBL. (VER TABELA)
      NUMERO DO PT          219  228 N    10 IDENFIFICA NUMERO DO PRO
                                             CESSO (PT) DE AUTORIZA -
                                             CAO DA OPERACAO.
      AUTORIZACAO LEGAL     229  248 A    20 IDENTIFICA BASE LEGAL OU
                                             REGULAMENTAR QUE AUTORI-
                                             ZOU A REALIZACAO DA OPE-
                                             RACAO.
      CONDICOES OPERACAO    249  308 A    60 IDENTIFICA METODO AMORTI
                                             ZACAO E PERIODICIDADE DE
                                             PAGAMENTOS DE JUROS E DE
                                             AMORTIZACAO.
      MODALIDADE            309  310 N     2 IDENTIFICA A MODALIDADE
                                             DA OPERACAO.(VER TABELA)
      GARANTIA 1A. OCORR.   311  312 N     2 IDENTIFICA TIPO DE GARAN
                                             TIA PRESTADA PARA REALI-
                                             ZACAO DA OPERACAO DE CRE
                                             DITO. (VER TABELA)
      GARANTIA 2A. OCORR.   313  314 N     2 IDENTIFICA TIPO DE GARAN
                                             TIA PRESTADA PARA REALI-
                                             ZACAO DA OP. DE CREDITO.
                                             (VER TABELA)
      GARANTIA 3A. OCORR.   315  316 N     2 IDENTIFICA TIPO DE GARAN
                                             TIA PRESTADA PARA REALI-
                                             ZACAO DA OP. DE CREDITO.
                                             (VER TABELA)
      GARANTIA 4A. OCORR.   317  318 N     2 IDENTIFICA TIPO DE GARAN
                                             TIA PRESTADA PARA REALI-
                                             ZACAO DA OP. DE CREDITO.
                                             (VER TABELA)
      GARANTIA 5A. OCORR.   319  320 N     2 IDENTIFICA TIPO DE GARAN
                                             TIA PRESTADA PARA REALI-
                                             ZACAO DA OP. DE CREDITO.
                                             (VER TABELA)
      NUM.PARCEL.LIBERACAO  321  323 N     3 IDENTIFICA NUMERO PREVIS
                                             TO DE PARCELAS DE LIBERA
                                             CAO DE RECURSOS.
      NUM.PARCEL.PAGAMENTO  324  326 N     3 IDENTIFICA NUMERO PREVIS
                                             TO DE PARCELAS DE PAGA-
                                             MENTO DA OP.DE CREDITO.
      SALDO LIBERACAO       327  344 N    18 IDENTIFICA O MONTANTE DE
                                             PRINCIPAL A SER LIBERADO
                                             AOS TOMADORES.(INFORM.C/
                                             CENTAVOS, SEM VIRGULA).
      SALDO PAGAMENTO       345  362 N    18 IDENTIFICA O MONTANTE DE
                                             PRINCIPAL A SER RESGATA-
                                             DO PELOS TOMADORES.(INF.
                                             C/CENTAVOS, SEM VIRGULA)
      DATA REFERENCIA       363  370 N     8 DATA NA QUAL O VLR OPER.
                                             FOI ATUALIZADO-DDMMAAAA
      ORIGEM                371  371 A     1 ' '=OPERACAO NOVA; 'P'=
                                             REPACTUACAO;'N'=RENOVA-
                                             CAO;'G'=RENEGOCIACAO
      NUM.OPER.RENEGOCIADA  372  374 N     3 SE ORIGEM 'G',QUANTAS O-
                                             PERACOES SENDO RENEGOC.
      DADOS DO CRONOGRAMA                    INFORMAR TANTOS REGS. DE
             DE LIBERACAO                    11 PARC. QUANTOS NECESSA
                                             RIOS PARA CADASTRAR O TO
                                             TAL DAS PARCELAS DO CRO-
                                             NOGRAMA DE LIBERACAO.

      TIPO DE REGISTRO        1    1 N     1 PREENCHER COM "2", IDEN-
                                             TIFICANDO O REGISTRO DE
                                             CRONOGRAMA DE LIBERACAO.
      NUMERO CREDOR           2   31 A    30 IDENTIFICADOR DA OPERA -
                                             CAO UTILIZADO INTERNAMEN
                                             TE PELA INSTITUICAO.

      CGC CREDOR             32   45 N    14 IDENTIFICACAO DA UNIDADE
                                             DA INST. QUE EFETUOU OP.
                                             DE CREDITO COM A ENTIDA-
                                             DE DO SETOR PUBLICO.
      1 GRUPO DE PARCELA
      NUMERO DA PARCELA      46   48 N     3 IDENTIFICA A PARCELA DE
                                             UMA OP. DE CREDITO A SER
                                             LIBERADA.
      DATA PREVISTA MOVIM.   49   56 N     8 DATA PREVISTA DE MOVIMEN
                                             TACAO PARA LIBERACAO DA
                                             PARCELA.(DDMMAAAA)
      VALOR PRINCIPAL        57   74 N    18 MONTANTE DE PRINCIPAL A
                                             SER LIBERADO DE UMA PAR-
                                             CELA ESPECIFICA. COM
                                             CENTAVOS.
      2 GRUPO DE PARCELA
      NUMERO DA PARCELA      75   77 N     3 IDENTIFICA A PARCELA DE
                                             UMA OPERACAO DE CREDITO
                                             A SER LIBERADA.
      DATA PREVISTA MOVIM.   78   85 N     8 DATA PREVISTA DE MOVIMEN
                                             TACAO PARA LIBERACAO DA
                                             PARCELA.(DDMMAAAA)
      VALOR PRINCIPAL        86  103 N    18 MONTANTE DE PRINCIPAL A
                                             SER LIBERADO DE UMA PAR-
                                             CELA ESPECIFICA. COM
                                             CENTAVOS.
      3 GRUPO DE PARCELA
      NUMERO DA PARCELA     104  106 N     3 IDENTIFICA A PARCELA DE
                                             UMA OP. DE CREDITO A SER
                                             LIBERADA.
      DATA PREVISTA MOVIM.  107  114 N     8 DATA PREVISTA DE MOVIMEN
                                             TACAO PARA LIBERACAO DA
                                             PARCELA. (DDMMAAAA)
      VALOR PRINCIPAL       115  132 N    18 MONTANTE DE PRINCIPAL A
                                             SER LIBERADO DE UMA PAR-
                                             CELA ESPECIFICA. COM
                                             CENTAVOS.
      4 GRUPO DE PARCELA
      NUMERO DA PARCELA     133  135 N     3 IDENTIFICA A PARCELA DE
                                             UMA OPERACAO DE CREDITO
                                             A SER LIBERADA.
      DATA PREVISTA MOVIM.  136  143 N     8 DATA PREVISTA DE MOVIMEN
                                             TACAO PARA LIBERACAO DA
                                             PARCELA.(DDMMAAAA)
      VALOR PRINCIPAL       144  161 N    18 MONTANTE DE PRINCIPAL A
                                             SER LIBERADO DE UMA PAR-
                                             CELA ESPECIFICA. COM
                                             CENTAVOS.
      5 GRUPO DE PARCELA
      NUMERO DA PARCELA     162  164 N     3 IDENTIFICA A PARCELA DE
                                             UMA OPERACAO DE CREDITO
                                             A SER LIBERADA.
      DATA PREVISTA MOVIM.  165  172 N     8 DATA PREVISTA DE MOVIMEN
                                             TACAO PARA LIBERACAO DA
                                             PARCELA.(DDMMAAAA)
      VALOR PRINCIPAL       173  190 N    18 MONTANTE DE PRINCIPAL A
                                             SER LIBERADO DE UMA PAR-
                                             CELA ESPECIFICA. COM
                                             CENTAVOS.
      6 GRUPO DE PARCELA
      NUMERO DA PARCELA     191  193 N     3 IDENTIFICA A PARCELA DE
                                             UMA OPERACAO DE CREDITO
                                             A SER LIBERADA.
      DATA PREVISTA MOVIM.  194  201 N     8 DATA PREVISTA DE MOVIMEN
                                             TACAO PARA LIBERACAO DA
                                             PARCELA. (DDMMAAAA)
      VALOR PRINCIPAL       202  219 N    18 MONTANTE DE PRINCIPAL A
                                             SER LIBERADO DE UMA PAR-
                                             CELA ESPECIFICA. COM
                                             CENTAVOS.
      7 GRUPO DE PARCELA
      NUMERO DA PARCELA     220  222 N     3 IDENTIFICA A PARCELA DE
                                             UMA OPERACAO DE CREDITO
                                             A SER LIBERADA.
      DATA PREVISTA MOVIM.  223  230 N     8 DATA PREVISTA DE MOVIMEN
                                             TACAO PARA LIBERACAO DA
                                             PARCELA. (DDMMAAAA)
      VALOR PRINCIPAL       231  248 N    18 MONTANTE DE PRINCIPAL A
                                             SER LIBERADO DE UMA PAR-
                                             CELA ESPECIFICA. COM
                                             CENTAVOS.
      8 GRUPO DE PARCELA
      NUMERO DA PARCELA     249  251 N     3 IDENTIFICA A PARCELA DE
                                             UMA OPERACAO DE CREDITO
                                             A SER LIBERADA.
      DATA PREVISTA MOVIM.  252  259 N     8 DATA PREVISTA DE MOVIMEN
                                             TACAO PARA LIBERACAO DA
                                             PARCELA. (DDMMAAAA)
      VALOR PRINCIPAL       260  277 N    18 MONTANTE DE PRINCIPAL A
                                             SER LIBERADO DE UMA PAR-
                                             CELA ESPECIFICA. COM
                                             CENTAVOS.
      9 GRUPO DE PARCELA
      NUMERO DA PARCELA     278  280 N     3 IDENTIFICA A PARCELA DE
                                             UMA OPERACAO DE CREDITO
                                             A SER LIBERADA.
      DATA PREVISTA MOVIM.  281  288 N     8 DATA PREVISTA DE MOVIMEN
                                             TACAO PARA LIBERACAO DA
                                             PARCELA. (DDMMAAAA)
      VALOR PRINCIPAL       289  306 N    18 MONTANTE DE PRINCIPAL A
                                             SER LIBERADO DE UMA PAR-
                                             CELA ESPECIFICA. COM
                                             CENTAVOS.
      10 GRUPO DE PARCELA
      NUMERO DA PARCELA     307  309 N     3 IDENTIFICA A PARCELA DE
                                             UMA OPERACAO DE CREDITO
                                             A SER LIBERADA.
      DATA PREVISTA MOVIM.  310  317 N     8 DATA PREVISTA DE MOVIMEN
                                             TACAO PARA LIBERACAO DA
                                             PARCELA. (DDMMAAAA).
      VALOR PRINCIPAL       318  335 N    18 MONTANTE DE PRINCIPAL A
                                             SER LIBERADO DE UMA PAR-
                                             CELA ESPECIFICA. COM
                                             CENTAVOS.
      11 GRUPO DE PARCELA
      NUMERO DA PARCELA     336  338 N     2 IDENTIFICA A PARCELA DE
                                             UMA OPERACAO DE CREDITO
                                             A SER LIBERADA.
      DATA PREVISTA MOVIM.  339  346 N     8 DATA PREVISTA DE MOVIMEN
                                             TACAO PARA LIBERACAO DA
                                             PARCELA. (DDMMAAAAA).
      VALOR PRINCIPAL       347  364 N    18 MONTANTE DE PRINCIPAL A
                                             SER LIBERADO DE UMA PAR-
                                             CELA ESPECIFICA. COM
                                             CENTAVOS.
      FILLER                365  374 N    10 CONTEM BRANCOS

      DADOS DO CRONOGRAMA                    INFORMAR TANTOS REGS. DE
             DE PAGAMENTO                    7 PARCELAS QUANTOS NECES
                                             SARIOS PARA CADASTRAR O
                                             TOTAL DAS PARCELAS DO
                                             CRONOGRAMA DE PAGAMENTO.
      TIPO DE REGISTRO        1    1 N     1 PREENCHER COM '3', IDEN-
                                             TIFICANDO O CRONOGRAMA
                                             DE PAGAMENTO.
      NUMERO CREDOR           2   31 A    30 MNEMONICO DA INSTITUICAO
                                             QUE IDENTIFICA INTERNA-
                                             MENTE UMA DADA OPERACAO
                                             DE CREDITO.
      CGC CREDOR             32   45 N    14 IDENTIFICACAO DA UNIDADE
                                             DA INST. QUE EFETUOU A
                                             OP. DE CREDITO COM A EN-
                                             TIDADE DO SETOR PUBLICO.
      1 GRUPO DE PARCELA
      NUMERO DA PARCELA      46   48 N     3 IDENTIFICA A PARCELA DE
                                             UMA OPERACAO DE CREDITO
                                             A SER PAGA.
      DATA PREVISTA MOVIM.   49   56 N     8 DATA PREVISTA DE MOVIMEN
                                             TACAO PARA PAGAMENTO DA
                                             PARCELA. (DDMMAAAAA).
      VALOR PRINCIPAL        57   74 N    18 VALOR REFERENTE APENAS
                                             AO PRINCIPAL DE UMA PAR-
                                             CELA ESPECIFICA A SER
                                             PAGA PELO TOMADOR. COM
                                             CENTAVOS.
      VALOR DE ENCARGOS      75   92 N    18 VALOR DE ENCARGOS PREVIS
                                             TOS DA PARCELA DE REFE-
                                             RENCIA. COM CENTAVOS.
      2 GRUPO DE PARCELA
      NUMERO DA PARCELA      93   95 N     3 IDENTIFICA A PARCELA DE
                                             UMA OPERACAO DE CREDITO
                                             A SER PAGA.
      DATA PREVISTA MOVIM.   96  103 N     8 DATA PREVISTA DE MOVIMEN
                                             TACAO PARA PAGAMENTO DA
                                             PARCELA. (DDMMAAAA).
      VALOR PRINCIPAL       104  121 N    18 VALOR REFERENTE APENAS
                                             AO PRINCIPAL DE UMA PAR-
                                             CELA ESPECIFICA A SER PA
                                             GA PELO TOMADOR. COM
                                             CENTAVOS.
      VALOR DE ENCARGOS     122  139 N    18 VALOR DE ENCARGOS PREVIS
                                             TOS DA PARCELA DE REFE-
                                             RENCIA. COM CENTAVOS.
      3 GRUPO DE PARCELA
      NUMERO DA PARCELA     140  142 N     3 IDENTIFICA A PARCELA DE
                                             UMA OPERACAO DE CREDITO
                                             A SER PAGA.
      DATA PREVISTA MOVIM.  143  150 N     8 DATA PREVISTA DE MOVIMEN
                                             TACAO PARA PAGAMENTO DA
                                             PARCELA. (DDMMAAAA).
      VALOR PRINCIPAL       151  168 N    18 VALOR REFERENTE APENAS
                                             AO PRINCIPAL DE UMA PAR-
                                             CELA ESPECIFICA A SER PA
                                             GA PELO TOMADOR. COM
                                             CENTAVOS.
      VALOR DE ENCARGOS     169  186 N    18 VALOR DE ENCARGOS PREVIS
                                             TOS DA PARCELA DE REFE-
                                             RENCIA. COM CENTAVOS.
      4 GRUPO DE PARCELA
      NUMERO DA PARCELA     187  189 N     3 IDENTIFICA A PARCELA DE
                                             UMA OPERACAO DE CREDITO
                                             A SER PAGA.
      DATA PREVISTA MOVIM.  190  197 N     8 DATA PREVISTA DE MOVIMEN
                                             TACAO PARA PAGAMENTO DA
                                             PARCELA. (DDMMAAAA)
      VALOR PRINCIPAL       198  215 N    18 VALOR REFERENTE APENAS
                                             AO PRINCIPAL DE UMA PAR-
                                             CELA ESPECIFICA A SER PA
                                             GA PELO TOMADOR. COM
                                             CENTAVOS.
      VALOR DE ENCARGOS     216  233 N    18 VALOR DE ENCARGOS PREVIS
                                             TOS DA PARCELA DE REFE-
                                             RENCIA. COM CENTAVOS.
      5 GRUPO DE PARCELA
      NUMERO DA PARCELA     234  236 N     3 IDENTIFICA A PARCELA DE
                                             UMA OPERACAO DE CREDITO
                                             A SER PAGA.
      DATA PREVISTA MOVIM.  237  244 N     8 DATA PREVISTA DE MOVIMEN
                                             TACAO PARA PAGAMENTO DA
                                             PARCELA. (DDMMAAAA).
      VALOR PRINCIPAL       245  262 N    18 VALOR REFERENTE APENAS
                                             AO PRINCIPAL DE UMA PAR-
                                             CELA ESPECIFICA A SER PA
                                             GA PELO TOMADOR. COM
                                             CENTAVOS.
      VALOR DE ENCARGOS     263  280 N    18 VALOR DE ENCARGOS PREVIS
                                             TOS DA PARCELA DE REFE-
                                             RENCIA. COM CENTAVOS.
      6 GRUPO DE PARCELA
      NUMERO DE PARCELA     281  283 N     3 IDENTIFICA A PARCELA DE
                                             UMA OPERACAO DE CREDITO
                                             A SER PAGA.
      DATA PREVISTA MOVIM.  284  291 N     8 DATA PREVISTA DE MOVIMEN
                                             TACAO PARA PAGAMENTO DA
                                             PARCELA. (DDMMAAAA).
      VALOR PRINCIPAL       292  309 N    18 VALOR REFERENTE APENAS
                                             AO PRINCIPAL DE UMA PAR-
                                             CELA ESPECIFICA A SER PA
                                             GA PELO TOMADOR. COM
                                             CENTAVOS.
      VALOR DE ENCARGOS     310  327 N    18 VALOR DE ENCARGOS PREVIS
                                             TOS DA PARCELA DE REFE-
                                             RENCIA. COM CENTAVOS.
      7 GRUPO DE PARCELA
      NUMERO DE PARCELA     328  330 N     3 IDENTIFICA A PARCELA DE
                                             UMA OPERACAO DE CREDITO
                                             A SER PAGA.
      DATA PREVISTA MOVIM.  331  338 N     8 DATA PREVISTA DE MOVIMEN
                                             TACAO PARA PAGAMENTO DA
                                             PARCELA. (DDMMAAAA)
      VALOR PRINCIPAL       339  356 N    18 VALOR REFERNETE APENAS
                                             AO PRINCIPAL DE UMA PAR-
                                             CELA ESPECIFICA A SER PA
                                             GA PELO TOMADOR.
                                             ( COM CENTAVOS ).
      VALOR DE ENCARGOS     357  374 N    18 VALOR DE ENCARGOS PREVIS
                                             TOS DA PARCELA DE REFE -
                                             RENCIA. ( COM CENTAVOS )

      DADOS OPERACAO QUE                     INFORMAR TANTOS REGS. DE
      ORIGINOU A REPACTUA-                   8 OPERACOES QUANTOS NE -
      CAO, RENOVACAO OU RE                   CESSARIOS P/IDENTIFICAR
      NEGOCIACAO. (NAO IN-                   AS OPERACOES A SEREM RE-
      FORMAR P/OPER.NOVAS)                   PACTUADAS, RENOVADAS OU
                                             RENEGOCIADAS (ESTAS ULTI
                                             MAS LIMITADAS A RENEGO -
                                             CIACAO DE 180 OPERACOES)
      TIPO DE REGISTRO        1    1 N     1 PREENCHER COM 4.
      NUMERO CREDOR           2   31 A    30 VIDE DESCRICAO NO REG.
                                             TIPO '1'.
      CGC CREDOR             32   45 N    14 IDEM
      FILLER                 46   70 A    25 CONTERA BRANCOS
      1.GRUPO IDENTIFICACA
      O OPERACAO ANTERIOR
      - NUM.BACEN ANTERIOR   71   80 N    10 INFORMAR O NUMERO DADO
                                             PELO BANCO CENTRAL PARA
                                             A OPERACAO ORIGINAL QUE
                                             FOI REPACTUADA, RENOVADA
                                             OU RENEGOCIADA.
      - CGC CREDOR ANTER.    81   94 N    14 CGC DO CREDOR DA OPERA-
                                             CAO ORIGINAL
      - CGC TOMADOR ANTER.   95  108 N    14 CGC DO TOMADOR DA OPERA-
                                             CAO ORIGINAL
      2.GRUPO IDENTIFICACA                   SE MAIS DE UMA OPERACAO
      O OPERACAO ANTERIOR                    ORIGINOU A NOVA OPERACAO
      - NUM.BACEN ANTERIOR  109  118 N    10 NUMERO DO BANCO CENTRAL
                                             PARA A OPERACAO ORIGINAL
      - CGC CREDOR ANTER.   119  132 N    14 CGC CREDOR OPERACAO ORI-
                                             GINAL.
      - CGC TOMADOR ANTER.  133  146 N    14 CGC TOMADOR OPERACAO ORI
                                             GINAL.
      3.GRUPO IDENTIFICACA                   SE MAIS DE 2 OPERACOES O
      O OPERACAO ANTERIOR                    RIGINARAM  A NOVA OPERA-
                                             CAO.
      - NUM.BACEN ANTERIOR  147  156 N    10 NUMERO DO BANCO CENTRAL
                                             PARA A OPERACAO ORIGINAL
      - CGC CREDOR ANTER.   157  170 N    14 CGC CREDOR OPERACAO ORI-
                                             GINAL
      - CGC TOMADOR ANTER.  171  184 N    14 CGC TOMADOR OPERACAO ORI
                                             GINAL
      4.GRUPO IDENTIFICACA                   SE MAIS DE 3 OPERACOES_O
      O OPERACAO ANTERIOR                    RIGINARAM A NOVA OPERA-
                                             CAO.
      - NUM.BACEN ANTERIOR  185  194 N    10 NUMERO DO BANCO CENTRAL
                                             PARA A OPERACAO ORIGINAL
      - CGC CREDOR ANTER.   195  208 N    14 CGC CREDOR OPERACAO ORI-
                                             GINAL
      - CGC TOMADOR ANTER.  209  222 N    14 CGC TOMADOR OPERACAO ORI
                                             GINAL
      5.GRUPO IDENTIFICACA                   SE MAIS DE 4 OPERACOES O
      O OPERACAO ANTERIOR                    RIGINARAM A NOVA OPERA-
                                             CAO.
      - NUM.BACEN ANTERIOR  223  232 N    10 NUMERO DO BANCO CENTRAL
                                             PARA A OPERACAO ORIGINAL
      - CGC CREDOR ANTER.   233  246 N    14 CGC CREDOR OPERACAO ORI-
                                             GINAL
      - CGC TOMADOR ANTER.  247  260 N    14 CGC TOMADOR OPERACAO ORI
                                             GINAL
      6.GRUPO IDENTIFICACA                   SE MAIS DE 5 OPERACOES
      O OPERACAO ANTERIOR                    ORIGINARAM A NOVA OPERA-
                                             CAO.
      - NUM.BACEN ANTERIOR  261  270 N    10 NUMERO DO BANCO CENTRAL
                                             PARA A OPERACAO ORIGINAL
      - CGC CREDOR ANTER.   271  284 N    14 CGC CREDOR OPERACAO ORI-
                                             GINAL
      - CGC TOMADOR ANTER.  285  298 N    14 CGC TOMADOR OPERACAO ORI
                                             GINAL
      7.GRUPO IDENTIFICACA
      O OPERACAO ANTERIOR                    SE MAIS DE 6 OPERACOES
                                             ORIGINARAM A NOVA OPERA-
                                             CAO.
      - NUM.BACEN ANTERIOR  299  308 N    10 NUMERO DO BANCO CENTRAL
                                             PARA A OPERACAO ORIGINAL
      - CGC CREDOR ANTER.   309  322 N    14 CGC CREDOR OPERACAO ORI-
                                             GINAL
      - CGC TOMADOR ANTER.  323  336 N    14 CGC TOMADOR OPERACAO ORI
                                             GINAL
      8.GRUPO IDENTIFICACA                   SE MAIS DE 7 OPERACOES
      O OPERACAO ANTERIOR                    ORIGINARAM A NOVA OPERA-
                                             CAO.
      - NUM.BACEN ANTERIOR  337  346 N    10 NUMERO DO BANCO CENTRAL
                                             PARA A OPERACAO ORIGINAL
      - CGC CREDOR ANTER.   347  360 N    14 CGC CREDOR OPERACAO ORI-
                                             GINAL
      - CGC TOMADOR ANTER   361  374 N    14 CGC TOMADOR OPERACAO ORI
                                             GINAL.

     LEIAUTE:  LDIP0003
      IDENTIFICACAO           1    1 A     1 PREENCHER COM Ð (HEXADE-
                                             CIMAL "40" EM ASCII E
                                             "7C" EM EBCDIC)
                              2    2 N     1 PREENCHER COM "1" (ALGA-
                                             RISMO 1)
      NUM.REG.GRAVADOS        3    8 N     6 TOTAL DE REGISTROS GRAVA
                                             DOS INCLUSIVE OS DE IDEN
                                             TIFICACAO E O DE CONTRO-
                                             LE
      FILLER                  9  374 A   366 CONTERA BRANCOS

DOCUMENTO:  DIP  1020

     LEIAUTE:  LDIP0004
      IDENTIFICACAO           1    1 A     1 PREENCHER COM Ý (VALOR H
                                             HEXADECIMAL "23" ASCII E
                                             "7B" EM EBCDIC
                              2    2 A     1 CONTERA "A" (LETRA "A")
                              3    3 A     1 CONTERA "1"(ALGARISMO 1)
      CODIGO DOCUMENTO        4    7 N     4 PREENCHER COM "1020"
      CGC INSTITUICAO         8   21 N    14 CGC DA INSTITUICAO
      NUMERO DA REMESSA      22   29 N     8 PREENCHER NO FORMATO
                                             "AAAANNNN" ONDE AAAA=ANO
                                             E NNNN=SEQUENCIAL REMES-
                                             SA. NAO PODERA COINCIDIR
                                             COM NUMERO DE REMESSA DO
                                             DOC. 1010 OU 1030.
      DATA REMESSA           30   37 N     8 DATA ENVIO REMESSA EM
                                             AAAAMMDD (ANO,MES E DIA)
      MEIO MAGNETICO         38   38 A     1 PREENCHER COM F (FITA)
      FILLER                 39  150 A   112 CONTEM BRANCOS

     LEIAUTE:  LDIP0005
      DADOS BASICOS MOVIM.                   1 REGISTRO PARA CADA LI-
                                             BERACAO OU PAGAMENTO O -
                                             CORRIDO NUMA MESMA DATA.
      TIPO MOVIMENTO          1    1 A     1 PREENCHER COM:
                                             "L" PARA LIBERACAO
                                             "P" PARA PAGAMENTO
      NUMERO BACEN            2   11 N    10 NUMERO DADO PELO BANCO
                                             CENTRAL QUANDO DO CADAS-
                                             TRAMENTO DA OPERACAO.
      NUM. PARCELA MOVIM.    12   14 N     3 NUMERO DA PARCELA QUE I-
                                             DENTIFICA A QUAL PARCELA
                                             PREVISTA NO CRONOGRAMA
                                             SE REFERE A MOVIMENTACAO
      FILLER                 15   17 N     3 CONTERA' ZEROS.
      IND. PARCIAL/TOTAL     18   18 A     1 INDICADOR DO TIPO DE MO-
                                             VIMENTACAO. INFORMAR "P"
                                             PARA LIBERACAO OU PAGA -
                                             MENTO PARCIAL, OU "T" PA
                                             RA LIBERACAO OU PAGAMEN-
                                             TO TOTAL.
      DATA EFETIVO MOVIM.    19   26 N     8 DATA NO FORMATO DDMMAAAA
                                             DA LIBERACAO OU PAGAMEN-
                                             TO.
      VALOR PRINCIPAL        27   44 N    18 VALOR DE PRINCIPAL LIBE-
                                             RADO OU PAGO NESSA PARCE
                                             LA. ( COM CENTAVOS ).
      VALOR ATUALIZACAO      45   62 N    18 VALOR DA ATUALIZACAO MO-
                                             NETARIA DESSA PARCELA.
                                                      (COM CENTAVOS).
      VALOR ENCARGOS         63   80 N    18 EXCLUSIVO DE PAGAMENTO.
                                             VALOR DOS ENCARGOS INCI-
                                             DENTES SOBRE A PARCELA
                                             PAGA ( COM CENTAVOS ).
      TAXA APLICADA          81   88 N     8 EXCLUSIVO DE PAGAMENTO.
                                             TAXA APLICADA PARA CAL-
                                             CULO DOS ENCARGOS, COM 4
                                             INTEIROS E 4 DECIMAIS.
      VALOR MULTA/MORA       89  106 N    18 EXCLUSIVO DE PAGAMENTO.
                                             VALOR DE MULTA OU DE MO-
                                             RA QUE ESTA SENDO PAGO.
                                             COM CENTAVOS.
      TOTAL LIBERADO/PAGO   107  124 N    18 SOMATORIO DOS CAMPOS DE
                                             VALOR EXISTENTES NO RE-
                                             GISTRO. COM CENTAVOS.
      SALDO DEVEDOR         125  142 N    18 VALOR DO SALDO DEVEDOR
                                             NA DATA DA MOVIMENTACAO
                                             CONSIDERANDO O PAGAMENTO
                                             OU A LIBERACAO QUE ESTA
                                             SENDO REGISTRADA.
      FILLER                143  150 A     8 RESERVADO. CONTEM BRANCO

     LEIAUTE:  LDIP0006
      IDENTIFICACAO           1    1 A     1 PREENCHER COM Ð (HEXADE-
                                             CIMAL "40" EM ASCII E
                                             "7C" EM EBCDIC)
                              2    2 N     1 PREENCHER COM "1" (ALGA-
                                             RISMO 1)
      NUM.REG.GRAVADOS        3    8 N     6 TOTAL DE REGISTROS  GRA-
                                             VADOS  INCLUSIVE  OS  DE
                                             IDENTIFICACAO E O DE CON
                                             TROLE
      FILLER                  9  150 A   142 CONTERA BRANCOS

DOCUMENTO:  DIP  1030

     LEIAUTE:  LDIP0007
      IDENTIFICACAO           1    1 A     1 PREENCHER COM Ý (VALOR
                                             HEXADECIMAL "23" ASCII E
                                             "7B" EM EBCDIC
                              2    2 A     1 CONTERA "A"(LETRA "A")
                              3    3 A     1 CONTERA"1"(ALGARISMO"1")
      CODIGO DOCUMENTO        4    7 N     4 PREENCHER COM "1030"
      CGC INSTITUICAO         8   21 N    14 CGC DA INSTITUICAO
      NUMERO DA REMESSA      22   29 N     8 PREENCHER NO FORMATO
                                             "AAAANNNN" ONDE AAAA=ANO
                                             E  NNNN=SEQUENCIAL REMES
                                             SA. NAO PODERA SER DO
                                             MESMO NUMERO DE REMESSA
                                             DOS DOC. 1010 E 1020.
      DATA REMESSA           30   37 N     8 DATA ENVIO DA REMESSA NO
                                             FORMATO AAAAMMDD (ANO,
                                             MES, DIA)
      MEIO MAGNETICO         38   38 A     1 PREENCHER COM 'F' (FITA)
      FILLER                 39  250 A   212 CONTERA BRANCOS

     LEIAUTE:  LDIP0008
      DADOS BASICOS DAS                      UM REGISTRO POR MES PARA
      INFORMACOES MENSAIS                    CADA UMA DAS OPERACOES
                                             "EM SER".
      NUMERO BACEN            1   10 N    10 NUMERO DADO PELO BANCO
                                             CENTRAL QUANDO DO CADAS-
                                             TRAMENTO DA OPERACAO.
      POSICAO                11   16 N     6 MES E ANO DA INFORMACAO
                                             NO FORMATO AAAAMM (ANO E
                                             MES).
      SALDO DEVEDOR          17   34 N    18 SALDO DEVEDOR DA OPERA -
                                             CAO NO FINAL DO MES DA
                                             POSICAO. COM CENTAVOS.
      SALDO DEVEDOR MEDIO    35   52 N    18 PARA ADIANTAMENTOS A DE-
                                             POSITANTES E CREDITO RO-
                                             TATIVO. INFORMAR MEDIA
                                             DO SALDO DEVEDOR DURANTE
                                             O MES DA POSICAO.
                                             COM CENTAVOS.
      TAXA MENSAL            53   60 N     8 TAXA DE JUROS MENSAL APL
                                             ICADA SOBRE O SALDO DEVE
                                             DOR MEDIO NAS OPERACOES
                                             DE ADIANTAMENTOS A DEPOS
                                             ITANTES E CREDITO ROTATI
                                             VO. COM 4 INTEIROS E 4
                                             DECIMAIS.
      VALOR CURSO NORMAL     61   78 N    18 VALOR EM CURSO NORMAL
                                             CONFORME AS NORMAS COSIF
                                             AO FINAL MES POSICAO.
                                             COM CENTAVOS.
      VALOR EM ATRASO        79   96 N    18 VALOR EM ATRASO, CONFORM
                                             E NORMAS COSIF, AO FINAL
                                             MES POSICAO.
                                             COM CENTAVOS.
      VLR CRED. LIQUIDACAO   97  114 N    18 VALOR DO CREDITO EM LIQU
                                             IDACAO, CONFORME NORMAS
                                             COSIF, AO FINAL MES POSI
                                             CAO.
                                             COM CENTAVOS
      INSCRITO PREJUIZO     115  132 N    18 VALOR INSCRITO EM PREJUI
                                             ZO, CONFORME NORMAS
                                             COSIF, AO FINAL DO MES
                                             POSICAO.
                                             COM CENTAVOS.
      RENDAS A APROPRIAR    133  150 N    18 VALOR DAS RENDAS A APRO-
                                             PRIAR AO FINAL DO MES PO
                                             SICAO.
                                             COM CENTAVOS.
      RENDAS APROPRIADAS    151  168 N    18 VALOR DAS RENDAS APROPRI
                                             ADAS NO MES DA POSICAO.
                                             COM CENTAVOS.
      VLOR CREDITO VENCIDO  169  186 N    18 VALOR DO CREDITO VENCIDO
                                             E NAO PAGO NO MES DA PO-
                                             SICAO.
                                             COM CENTAVOS.
      FILLER                186  250 A    64 RESERVADO.CONTERA BRANCO

     LEIAUTE:  LDIP0009
      IDENTIFICACAO           1    1 A     1 PREENCHER COM Ð (HEXADE-
                                             CIMAL "40" EM ASCII E
                                             "7C" EM EBCDIC)
                              2    2 N     1 PREENCHER COM "1" (ALGA-
                                             RISMO "1")
      NUM. REG. GRAVADOS      3    8 N     6 TOTAL DE REGISTROS GRAVA
                                             DOS INCLUSIVE OS DE IDEN
                                             TIFICACAO E O DE CONTRO
                                             LE FINAL.
      FILLER                  9  250 A   242 CONTERA BRANCOS.

DOCUMENTO:  MTF  5816

     LEIAUTE:  LMTF0001
      IDENTIF. DO REGISTRO    1    1 X     1 "Ý" (VALOR HEXADECIMAL
                                             "23" EM ASCII, E "7B" EM
                                              EBCDIC)
                              2    2 X     1 "A" (LETRA A)
                              3    3 9     1 1 (ALGARISMO 1)
      CODIGO DO DOCUMENTO     4    7 9     4 PREENCHIDO COM 5816
      CGC DA INSTITUICAO      8   21 9    14 CGC COM 14 POSI!ÝES
      FILLER                 22   35 X    14 ESPACOS EM BRANCO
      ANO-SEMESTRE           36   41 9     6 FORMATO AAAASS
      FLAG                   42   42 X     1 - CONTERA O CARATER "*",
                                             NO CASO DO UNICO OU UL-
                                             TIMO ARQUIVO DO VOLUME
                                             DE FITA MAGNcTICA
                                             - CONTERA O CARATER "F",
                                             NO CASO DE ARQUIVO EM
                                             FITA MAGNETICA QUE NAO
                                             FOR UNICO OU ULTIMO DO
                                             VOLUME

     LEIAUTE:  LMTF0002
      CGC/CPF                 1   14 9    14 CODIGO E DIGITO VERIFI-
                                             DOR, CGC/CPF DO TITULAR
                                             DO CARTAO
      IND-CGC/CPF            15   15 X     1 F = PESSOA FISICA
                                             J = PESSOA JURIDICA
                                             E = ESTRANGEIRO
      MOEDA                  16   18 9     3 COD. MOEDA. 220(DOLAR)
      VALOR-FATURA-MOEDA     19   35 9    17 VALOR COM SINAL INCLUSI-
                                             VE CENTAVOS
      ANO-MES-FATURA         36   41 9     6 FORMATO AAAAMM
      FILLER                 42   42 X     1 ESPACO EM BRANCO

     LEIAUTE:  LMTF0003
      IDENTIF. DO REGISTRO    1    1 X     1 "Ð (VALOR HEXADECIMAL
                                             "40 EM ASCII, E "7C" EM
                                             EBCDIC)
                              2    2 9     1 1 (ALGARISMO 1)
      NUM. REG. GRAVADOS      3    8 9     6 TOTAL DE REGISTROS GRA-
                                             VADOS NO ARQUIVO INCLU-
                                             SIVE OS DE CONTROLE
      FILLER                  9   42 X    34 ESPACOS EM BRANCO
```
