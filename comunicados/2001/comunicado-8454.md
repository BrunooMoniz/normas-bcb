---
titulo: "COMUNICADO N. 008454"
orgao: "Banco Central do Brasil"
tipo: "Comunicado"
numero: "8454"
data: 2001-05-18
ementa: "Comunica decisoes do Banco Central do Brasil, relativas a implementacao da Reestruturacao do Sistema de Pagamen- tos Brasileiro."
revogada: false
responsavel: "SECRE"
versao_texto: "texto do portal do BCB"
fonte: "https://www.bcb.gov.br/estabilidadefinanceira/exibeoutrasnormas?tipo=Comunicado&numero=8454"
baixado_em: 2026-11-11
---
# COMUNICADO N. 008454

```
                        COMUNICADO N. 008454
                        --------------------

                               Comunica decisoes  do Banco Central do
                               Brasil,  relativas a  implementacao da
                               Reestruturacao do  Sistema de Pagamen-
                               tos Brasileiro.

         Comunicamos que  o Banco Central do Brasil adotou as seguin-
tes decisoes, no  ambito da  Reestruturacao do Sistema  de Pagamentos
Brasileiro, relativas a prestacao de servicos de tecnologia da infor-
macao:

         I  -  Provedores  de Servicos  de  Tecnologia  da Informacao
(PSTI) podem prestar servicos para uma ou mais instituicoes financei-
ras detentoras de conta  Reservas Bancarias, desde  que observados os
requisitos e as  definicoes referentes a  topologia "n x  2" aqui es-
tabelecidos, bem como  o disposto  no documento Manual  de Mensagens,
disponivel na pagina do Banco Central na Internet (www.bcb.gov.br);

         II -  Considera-se PSTI a entidade que proporciona o encami-
nhamento das  mensagens originadas  das instituicoes  financeiras por
ele servidas ou a elas destinadas, observado que:

         a) uma instituicao  financeira  somente pode  ser  PSTI para
            instituicoes do conglomerado a que pertencer; e

         b) os provedores da rede SPB nao podem ser PSTI;

          III - Define-se "n x 2"  (n variando de 1  a 8) a topologia
em que "n" significa  o numero maximo de  instituicoes que podem com-
partilhar, de forma independente de outros  grupos de ate oito insti-
tuicoes, os servicos  do PSTI  e "2"  o numero  minimo de  Centros de
Servicos de  Informatica (CSI)  possuidos pelo  PSTI e  utilizados na
prestacao desses servicos;

         IV - A topologia n x 2 pode ter as seguintes formas de aglu-
tinacao:

         a) AGLOMERADO BANCARIO: conjunto de,  no maximo, oito insti-
            tuicoes financeiras detentoras de conta Reservas Bancari-
            as nao participantes de um mesmo conglomerado financeiro,
            compartilhando os servicos  de um PSTI  de forma indepen-
            dente de outros aglomerados bancarios; ou

         b) CONGLOMERADO: conjunto de ate oito instituicoes financei-
            ras detentoras de conta  Reservas Bancarias com controla-
            dor comum,  direto ou indireto,  das quais  uma presta os
            servicos tipicos de  PSTI, mesmo que  qualquer das demais
            esteja apta a operar no SPB;

         V - Na prestacao dos servicos, o PSTI deve:

         a) manter inalterado o conteudo das mensagens por ele cursa-
            das;

         b) assegurar e preservar o  sigilo das informacoes processa-
            das por seu intermedio;

         c) oferecer nivel de servicos indiferenciado as instituicoes
            financeiras participantes de um aglomerado ou conglomera-
            do;

         d) ter a  possibilidade de  processar as "mensagens  de eco"
            oriundas das instituicoes financeiras participantes de um
            aglomerado, nao se admitindo  que o PSTI emita essas men-
            sagens em substituicao ou em nome das instituicoes;

         e) possuir, no minimo:

         1. dois Centros de Servicos de Informatica (CSI) independen-
            tes e interligados,  de  modo  a  oferecer  funcionamento
            ininterrupto,  observado o indice de 99,8% de operaciona-
            lidade;

         2. uma ligacao a  cada um dos  provedores de comunicacoes da
            rede SPB, em cada um de seus CSI;

         f) possuir,  para cada aglomerado ou conglomerado, elementos
            computacionais independentes, definindo-se como elementos
            computacionais todas as maquinas,  programas e aplicacoes
            necessarios para cursar as mensagens das instituicoes fi-
            nanceiras participantes do aglomerado ou conglomerado;

         VI - A instituicao  financeira  participante  de  aglomerado
bancario como o definido no item IV-a deve:

         a) zelar pela guarda e integridade do seu  Certificado Digi-
            tal, que nao pode, em nenhuma  hipotese, estar localizado
            nas maquinas servidoras do PSTI;

         b) possuir maquinas e  programas apropriados  para preparar,
            assinar digitalmente, cifrar e encaminhar suas mensagens;

         c) possuir maquinas e programas  apropriados  para  receber,
            conferir  a  assinatura digital, decifrar e  processar as
            mensagens que lhe forem encaminhadas;

         d) possuir duas ligacoes a rede SPB,  para comunicacao com o
            PSTI a que esteja ligada;

         e) ter disponivel,  para supervisao  pelo Banco Central,  os
            programas-fonte de seus  programas  de  acesso ao SPB, os
            diagramas de conexao ao SPB e  os diagramas de programas,
            maquinas e de telecomunicacoes, envolvendo a propria ins-
            tituicao e o PSTI;

         VII - No caso de conglomerado, como definido no item IV-b:

         a) os servicos de processamento de  dados  das  instituicoes
            financeiras participantes devem ser executados em um uni-
            co CSI;

         b) o PSTI do conglomerado nao pode  ter seu centro de infor-
            matica terceirizado,  do contrario,  o conglomerado passa
            a condicao de aglomerado bancario,  sujeitando-se as con-
            dicoes pertinentes;

         c) cada instituicao financeira participante deve possuir seu
            proprio  certificado digital,  devendo suas mensagens ser
            assinadas  com  as chaves privadas  relativas ao seu cer-
            tificado;

         d) a instituicao  financeira  que operar como PSTI deve pos-
            suir dois  CSI independentes e interligados e, no minimo,
            duas ligacoes a rede SPB, de modo a oferecer funcionamen-
            to ininterrupto, observado o indice de 99,8% de operacio-
            nalidade.

        VIII - A instituicao, independentemente da topologia adotada,
que nao puder encaminhar as mensagens relativas a movimentacao de sua
conta Reservas Bancarias ao Banco Central do Brasil, devera adotar os
os procedimentos de contingencia a serem oportunamente divulgados;

         IX - Serao divulgados, oportunamente,  os requisitos minimos
de desempenho e de seguranca de dados que os participantes do SPB de-
verao atender.

         X - Cada instituicao, ao aderir a rede SPB,  devera submeter
ao Banco Central do Brasil a topologia que pretende utilizar e manter
atualizadas as informacoes  pertinentes, as quais  estarao sujeitas a
supervisao desta Autarquia, a exemplo dos  programas-fonte e dos dia-
gramas mencionados no item VI-e.
         XI - E admitida a hospedagem de maquinas  e de aplicativos e
a utilizacao de  centros de  processamento comerciais especializados,
desde que observados todos os criterios  acima definidos para as ins-
tituicoes financeiras participantes e para os PSTI.

         XII - E vedado o transito, entre as partes, das chaves crip-
tograficas privadas utilizadas ou  de mensagens "em  claro" de infor-
macoes.

                                   Brasilia, 18 de maio de 2001

DEPARTAMENTO DE OPERACOES          DEPARTAMENTO DE INFORMATICA
BANCARIAS E DE SISTEMA
DE PAGAMENTOS

Luis Gustavo da Matta Machado           Roberto Ozu
Chefe                                   Chefe
```
