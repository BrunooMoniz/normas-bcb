---
titulo: "Circular Nº 3.634"
orgao: "Banco Central do Brasil"
tipo: "Circular"
numero: "3634"
data: 2013-03-04
ementa: "Estabelece os procedimentos para o cálculo da parcela dos ativos ponderados pelo risco (RWA) referente às exposições sujeitas à variação de taxas de juros prefixadas denominadas em real cujo requerimento de capital é calculado mediante abordagem padronizada (RWAjur1), de que trata a Resolução nº 4.193, de 1º de março de 2013."
revogada: false
responsavel: "SECRE"
versao_texto: "PDF do portal do BCB"
publicacao: "Publicada no DOU de 6/3/2013, Seção 1, p. 13/14."
atualizacoes: ["Circular BCB nº 3.947/2019 - Alteração, a partir de 1º/10/2019 - Nova redação: art. 1º, caput e inciso II; art. 2º, caput e § 4º.", "Resolução BCB nº 266/2022 - Alteração, a partir de 1º/7/2023 - Nova redação: ementa, preâmbulo, art. 1º, caput, inciso I e § 1º. Inclusão: art. 1º, inciso I, “a” e “b”.", "Resolução BCB nº 447/2024 - Alteração, a partir de 1º/1/2025 - Nova redação: art. 1º, inciso I. Revogação: art. 1º, inciso I, “a” e “b”."]
normas_vinculadas: ["RESOLUÇÃO BCB 447/2024", "RESOLUÇÃO BCB 266/2022", "RESOLUÇÃO 4193/2013", "RESOLUÇÃO 3464/2007", "CIRCULAR 3947/2019", "CIRCULAR 3674/2013", "CIRCULAR 3646/2013", "CIRCULAR 3645/2013", "CIRCULAR 3568/2011", "CIRCULAR 3498/2010", "CIRCULAR 3361/2007", "RESOLUÇÃO BCB 580/2026"]
referencias: ["Lei nº 4.595/1964, arts. 9º; 10, inciso IX; e 11, inciso VII.", "Resolução CMN nº 4.193/2013, arts. 3º, § 2º, e 15.", "Cita Resolução CMN nº 3.464/2007.", "Revoga, a partir de 1º/10/2013, as Circulares BCB nº 3.361/2007, 3.498/2010, 3.568/2011."]
fonte: "https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Circular&numero=3634"
arquivo: "https://www.bcb.gov.br/pre/normativos/circ/2013/pdf/circ_3634_v1_o.pdf"
sha256_arquivo: 2e227a95fa2609ca0f24ec65920c5022a97c41fe1688e7b419b5d7c1596e7f40
baixado_em: 2026-11-11
---
# Circular Nº 3.634

CIRCULAR Nº 3.634, DE 4 DE MARÇO DE 2013
Estabelece os procedimentos para o cálculo da
parcela dos ativos ponderados pelo risco (RWA)
referente às exposições sujeitas à variação de taxas
de juros prefixadas denominadas em real cujo
requerimento de capital é calculado mediante
abordagem padronizada (RWAJUR1), de que trata a
Resolução nº 4.193, de 1º de março de 2013.
A Diretoria Colegiada do Banco Central do Brasil, em sessão extraordinária
realizada em 1º de março de 2013, com base no disposto nos arts. 9º, 10, inciso IX, e 11, inciso
VII, da Lei nº 4.595, de 31 de dezembro de 1964, e 3º, §2º, e 15 da Resolução nº 4.193, de 1º de
março de 2013,
RESOLVE:
Art. 1º O cálculo do valor diário da parcela dos ativos ponderados pelo risco
(RWA), relativa às exposições sujeitas à variação de taxas de juros prefixadas denominadas em
real cujo requerimento de capital é calculado mediante abordagem padronizada (RWAJUR1), de
que trata a Resolução nº 4.193, de 1º de março de 2013, deve ser efetuado com base na seguinte
fórmula:

RWAJUR1 


 M pret 1 60

 1 60
1 
Padrão 
Padrão
Padrão 
Padrão  

 max 
VaR
,
VaR

max
sVaR
,
sVaR





t i
t 1

t i
t 1
 ,

F 
60
60
i

1
i

1





 



em que:
I - F = fator estabelecido no art. 4º da Resolução nº 4.193, de 2013;
II - Mpret = multiplicador para o dia "t", divulgado diariamente pelo Banco
Central do Brasil, determinado como função decrescente da volatilidade, cujo valor está
compreendido entre 1 e 3;
III - VaRtPadrão = valor em risco, expresso em reais, do conjunto das
exposições de que trata o caput para o dia "t", obtido de acordo com a seguinte fórmula:

VaRtPadrão 

n

n

i 1

j 1

  VaR VaR   , em que:
i ,t

j ,t

i, j

a) n = 10 (número de vértices Pi);
b) VaRi,t = valor em risco, expresso em reais, associado ao vértice Pi no dia
"t", obtido de acordo com a seguinte fórmula:
P
VaRi,t  2,33  i   i,t VMTM i, t  D , em que:
252

1. Pi = vértice considerado para efeito de agrupamento dos fluxos de caixa,
conforme procedimento descrito no art. 3º desta Circular;
2. i,t = volatilidade-padrão para o prazo "i" e dia "t", divulgada diariamente
pelo Banco Central do Brasil;
3. VMTMi,t = soma algébrica, positiva ou negativa, expressa em reais, dos
valores dos fluxos de caixa marcados a mercado no dia "t" e alocados no vértice P i,
conforme procedimento descrito no art. 3º desta Circular; e
4. D = 10 (número de dias úteis considerados necessários para a liquidação
da posição);
c) i,j = correlação entre os vértices "i" e "j", utilizada para efeito de
determinação do VaRt Padrão, obtida de acordo com a seguinte fórmula:

i, j    (1   )








max( Pi ,P j ) 

k



min( Pi ,Pj ) 


, em que:

1. ρ = parâmetro-base para o cálculo de ρi,j, divulgado no último dia útil de
cada mês ou a qualquer momento, a critério do Banco Central do Brasil; e
2. k = fator de decaimento da correlação, divulgado no último dia útil de
cada mês ou a qualquer momento, a critério do Banco Central do Brasil;
IV - sVaRtPadrão = valor em risco estressado, expresso em reais, das
exposições mencionadas no caput para o dia "t", obtido de acordo com a seguinte fórmula:

sVaRtPadrão 

n

n

  sVaR  sVaR
i 1

j 1

i ,t

j ,t

  iS, j , em que:

a) n = 10 (número de vértices Pi);
b) sVaRi,t = valor em risco estressado, expresso em reais, associado ao
vértice Pi no dia "t", obtido de acordo com a seguinte fórmula:
P
sVaR
 2,33  i   S VMTM i, t  D , em que:
i, t
i
252

1. Pi = vértice considerado para efeito de agrupamento dos fluxos de caixa,
conforme procedimento descrito no art. 3º desta Circular;
2. iS = volatilidade-padrão atribuída ao vértice "i", utilizada para o cálculo
do sVaRi,t;

Circular nº 3.634 de 4 de março de 2013

Página 2 de 6

3. VMTMi,t = soma algébrica, positiva ou negativa, expressa em reais, dos
valores dos fluxos de caixa marcados a mercado no dia "t" e alocados no vértice P i,
conforme procedimento descrito no art. 3º desta Circular;
4. D = 10 (número de dias úteis considerados necessários para a liquidação
da posição);
c) Si,j = correlação entre os vértices "i" e "j", utilizada para efeito de
determinação do sVaRtPadrão, obtida de acordo com a seguinte fórmula:

S

i, j

  S  (1   S )








max( Pi ,P j ) 

kS



min( Pi ,Pj ) 


, em que:

1. S = parâmetro-base para o cálculo das correlações utilizadas no
sVaRt

Padrão

;e
2. kS = fator de decaimento para o cálculo das correlações utilizadas no

sVaRtPadrão.
§ 1º O cálculo referido no caput aplica-se às operações sujeitas à variação
de taxas de juros prefixadas referentes a instrumentos financeiros denominados em real e
classificadas na carteira de negociação, na forma da Resolução nº 3.464, de 26 de junho de
2007, inclusive aos instrumentos financeiros derivativos.
§ 2º Os valores de iS, S e kS serão divulgados pelo Banco Central do
Brasil.
§ 3º Para efeito de determinação de VMTMi,t, define-se vértice como o
prazo Pi em que os fluxos de caixa devem ser alocados ou agrupados.
Art. 2º Para a apuração do valor diário da parcela RWAJUR1, define-se cada fluxo
de caixa como o resultado líquido do valor das posições ativas menos o valor das posições
passivas que vencem em um mesmo dia, referentes ao conjunto das operações mantidas em
aberto no dia útil imediatamente anterior.
§ 1º Os fluxos de caixa devem ser obtidos mediante a decomposição de cada
operação mantida em aberto em uma estrutura temporal equivalente de recebimentos e
pagamentos, considerando as datas de vencimento contratadas.
§ 2º O número de fluxos de caixa corresponderá ao número de vencimentos em
que os resultados líquidos apurados nos termos deste artigo forem diferentes de zero.
§ 3º Os valores dos ativos e passivos que compõem os fluxos de caixa devem
compreender o principal, os juros e os demais valores relacionados a cada operação.

Circular nº 3.634, de 4 de março de 2013

Página 3 de 6

§ 4º Os valores dos ativos e passivos que compõem os fluxos de caixa devem ser
marcados a mercado mediante a utilização da estrutura temporal das taxas de juros que
represente as taxas em vigor no mercado no dia útil imediatamente anterior.
§ 5º As operações sem vencimento definido ou cujo vencimento dependa da
aplicação de cláusulas contratuais específicas devem ter os correspondentes fluxos de caixa
obtidos com base em critérios consistentes e passíveis de verificação pelo Banco Central do
Brasil.
§ 6º Para efeito da obtenção dos fluxos de caixa das operações com instrumentos
financeiros derivativos, devem ser observados os seguintes critérios:
I - no caso de operações de swap, o tratamento da posição do contrato
referenciado em real e em taxa de juros prefixada deve ser idêntico ao dispensado a um título
com remuneração em taxa prefixada, com a mesma data de vencimento do swap, cujo valor de
resgate seja o valor final resultante para a posição prefixada em real;
II - no caso de operações com contratos a termo e de futuros referenciados em real
e em taxa de juros prefixada, o tratamento correspondente deve ser idêntico ao dispensado a um
título com remuneração em taxa prefixada, com a mesma data de vencimento dos mencionados
contratos, cujo valor de resgate seja o valor desses contratos;
III - no caso de operações de liquidação futura envolvendo título de renda
prefixada, o tratamento deve ser idêntico ao dispensado a duas posições opostas em títulos
prefixados, sendo:
a) uma, representada por um título com data de vencimento coincidente com a da
transferência, para o adquirente, da propriedade do título objeto da operação, cujo valor de
resgate deve ser o valor da operação; e
b) a outra, representada por um título com a mesma data de vencimento do título
objeto da operação, cujo valor de resgate deve ser o valor de resgate desse último; e
IV - no caso de operações com opções referenciadas em real e em taxa de juros
prefixada:
a) o valor representativo de cada posição deve ser obtido multiplicando-se a
quantidade de contratos pelo seu tamanho e pela variação do preço da opção em relação à
variação do preço de seu ativo objeto (delta); e
b) os fluxos de caixa correspondentes a cada operação devem ser obtidos
separadamente, e seu resultado deve ser incluído no fluxo de caixa da data do vencimento do
contrato.
§ 7º Devem ser excluídos os fluxos de caixa resultantes de derivativo de crédito
utilizado como hedge do ajuste ao valor de mercado das operações com instrumentos financeiros
derivativos em decorrência de variação da qualidade creditícia da contraparte (CVA).
§ 8º Os valores das posições detidas em decorrência de aplicações em cotas de
fundos de investimento devem ser tratados de forma consistente com base na composição
Circular nº 3.634 de 4 de março de 2013

Página 4 de 6

proporcional de suas carteiras ou, na sua impossibilidade, como uma posição sujeita à variação
de taxas de juros prefixadas, alocada no vértice P10 definido no art. 3º desta Circular.
Art. 3º Os fluxos de caixa devem ser agrupados nos seguintes vértices Pi,
conforme o número de dias úteis remanescentes até a data de seu vencimento (Ti):
I - P1, correspondente a 21 dias úteis;
II - P2, correspondente a 42 dias úteis;
III - P3, correspondente a 63 dias úteis;
IV - P4, correspondente a 126 dias úteis;
V - P5, correspondente a 252 dias úteis;
VI - P6, correspondente a 504 dias úteis;
VII - P7, correspondente a 756 dias úteis;
VIII - P8, correspondente a 1.008 dias úteis;
IX - P9, correspondente a 1.260 dias úteis; e
X - P10, correspondente a 2.520 dias úteis.
§ 1º Os fluxos de caixa com prazo inferior a 21 dias úteis devem ser alocados no
vértice P1 na proporção correspondente a Ti/21 do seu valor marcado a mercado.
§ 2º Os fluxos de caixa com prazo superior a 2.520 dias úteis devem ser alocados
no vértice P10, na proporção correspondente à fração Ti/2.520 do seu valor marcado a mercado.
§ 3º Os fluxos de caixa compreendidos entre os prazos de 21 dias úteis e 2.520
dias úteis devem ser alocados nos vértices anterior (Pi) e posterior (Pj), de acordo com os
seguintes critérios:
I - a fração ( Pj – Ti ) / ( Pj – Pi ) do valor marcado a mercado do fluxo de caixa
deve ser alocada no vértice de prazo Pi; e
II - a fração ( Ti – Pi ) / ( Pj – Pi ) do valor marcado a mercado do fluxo de caixa
deve ser alocada no vértice de prazo Pj.
Art. 4º A metodologia de apuração das taxas utilizadas para a marcação a
mercado das exposições sujeitas à variação de taxas de juros prefixadas denominadas em real
deve ser estabelecida com base em critérios consistentes e passíveis de verificação, em
conformidade com as normas em vigor.
§ 1º Não integram a base de cálculo da parcela RWAJUR1 as operações nas quais a
instituição atue exclusivamente como intermediadora, não assumindo quaisquer direitos ou
obrigações para com as partes.

Circular nº 3.634, de 4 de março de 2013

Página 5 de 6

§ 2º Cabe à instituição do conglomerado responsável pela remessa de
informações contábeis ao Banco Central do Brasil a apuração consolidada da parcela RWAJUR1.
Art. 5º Deve ser encaminhado ao Banco Central do Brasil, na forma a ser
estabelecida, relatório detalhando a apuração da parcela RWAJUR1.
Parágrafo único. As instituições devem manter à disposição do Banco Central do
Brasil, pelo prazo de cinco anos, as informações utilizadas para a apuração diária da parcela
RWAJUR1, assim como a metodologia utilizada para apuração do valor de mercado das
respectivas operações.
Art. 6º Esta Circular entra em vigor em 1º de outubro de 2013.
Art. 7º Ficam revogadas, a partir de 1º de outubro de 2013:
I - a Circular nº 3.361, de 12 de setembro de 2007;
II - a Circular nº 3.498, de 28 de junho de 2010; e
III - a Circular nº 3.568, de 21 de dezembro de 2011.
Parágrafo único. As citações à Circular nº 3.361, de 2007, passam a ter como
referência esta Circular.

Luiz Awazu Pereira da Silva
Diretor de Regulação do Sistema Financeiro
Este texto não substitui o publicado no DOU de 6/3/2013, Seção 1, p. 13/14, e no Sisbacen.

Circular nº 3.634 de 4 de março de 2013

Página 6 de 6
