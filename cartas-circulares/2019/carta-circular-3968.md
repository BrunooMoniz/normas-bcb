---
titulo: "Carta Circular N° 3.968"
orgao: "Banco Central do Brasil"
tipo: "Carta Circular"
numero: "3968"
data: 2019-08-07
ementa: "Dispõe sobre as regras de formação do identificador padronizado para as operações de crédito, de que trata a Circular n 3.953, de 10 de julho de 2019, bem como o cronograma e demais condições para sua implantação."
revogada: false
responsavel: "DESIG"
versao_texto: "texto do portal do BCB"
publicacao: "Publicada no DOU de 8/8/2019, Seção 1, p. 308."
atualizacoes: ["Instrução Normativa BCB nº 12/2020 - Alteração, a partir de 1º/10/2020 - Nova redação: ementa;  art. 1º, caput; art. 2º, caput, incisos I e II e § 1º, caput e inciso III; art. 3º, caput; e art. 4º, inciso III, “c”. Inclusão: art. 1º, §§ 1º e 2º; art. 2º, inciso I, “a” e “b”; e art. 4º-A. Revogação: art. 1º, parágrafo único; art. 2º, § 1º, inciso IV; art. 4º, inciso III, “d”; e art. 5º, inciso I, “c”.", "Instrução Normativa BCB nº 19/2020 - Alteração, a partir de 1º/10/2020 - Revogação: art. 1º, § 2º."]
normas_vinculadas: ["INSTRUÇÃO NORMATIVA BCB 19/2020", "INSTRUÇÃO NORMATIVA BCB 12/2020", "CIRCULAR 3953/2019", "INSTRUÇÃO NORMATIVA BCB 30/2020", "INSTRUÇÃO NORMATIVA BCB 61/2020"]
referencias: ["Portaria BCB nº 84.287/2015, Anexo (Regimento Interno do BCB), arts. 23, inciso I, \"a\"; e 77, inciso III.", "Circular BCB nº 3.953/2019."]
fonte: "https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Carta%20Circular&numero=3968"
baixado_em: 2026-11-10
---
# Carta Circular N° 3.968

O Chefe do Departamento de Monitoramento do Sistema Financeiro (Desig), no uso da atribuição que lhe confere o art. 23, inciso I, alínea “a”, do Regimento Interno do Banco Central do Brasil, anexo à Portaria nº 84.287, de 27 de fevereiro de 2015, com base no art. 77, inciso III, do referido Regimento, e tendo em vista o disposto na Circular nº 3.953, de 10 de julho de 2019,

RESOLVE:

Art. 1º O identificador padronizado da operação de crédito, de que trata a Circular nº 3.953, de 10 de julho de 2019, será formado pela concatenação das informações contidas nos campos do SCR abaixo discriminados, respeitando-se a seguinte ordem:

I - CNPJ da instituição;

II - modalidade da operação;

III - tipo do cliente;

IV - código do cliente;

V - código do contrato.

Parágrafo único.  Para a composição e o reporte do código de que trata o caput devem ser observadas as orientações contidas nas instruções de preenchimento e nos manuais, disponíveis na página do Banco Central do Brasil na internet, no endereço eletrônico https://www.bcb.gov.br/estabilidadefinanceira/scrdoc3040.

Art. 2º No caso de alterações que modifiquem os campos relacionados no art. 1º, utilizados para formar o identificador da operação, a instituição deverá:

I - manter inalterado o identificador da operação; ou

II - gerar novo identificador para a operação, com base nas novas informações dos campos relacionados no art. 1º, utilizados para formar o identificador da operação.

§ 1º As alterações de que trata o caput incluem:

I - renegociação que resulte em novo número de contrato e/ou nova modalidade da operação de crédito;

II - modificação de número interno do contrato nos sistemas legados da instituição;

III - modificação da modalidade da operação de crédito;

IV - assunção de dívida.

§ 2º   Na hipótese de geração de novo identificador, a instituição deverá assegurar a rastreabilidade da operação de crédito, informando o novo identificador na informação de saída da operação original.

Art. 3º O identificador padronizado deverá ser atribuído a todas as operações de crédito informadas ao SCR, inclusive para aquelas já existentes, compreendendo:

I - as operações em ser;

II - os créditos baixados como prejuízo.

Art. 4º Foram realizadas as seguintes modificações, com vigência a partir da data-base de maio de 2020:

I - no documento de código 3040 - Dados de Risco de Crédito, tag (Op) - Informações básicas da operação: inclusão do campo “Identificação padronizada da operação de crédito”;

II - no Anexo 26 - Informações Adicionais, domínio 03 (Saídas):  inclusão do subdomínio 16 (Saída por alteração do IPOC), contendo os seguintes campos:

a) Cd (IPOC novo);

b) Valor (valor renegociado), a ser preenchido apenas quando a operação tiver sido renegociada;

c) Qtd (motivo da saída IPOC).

III – Inclusão do Anexo 34 - Motivo de saída IPOC, e seus domínios:

a) 01 (alteração de código de contrato ou modalidade/submodalidade);

b) 02 (renegociação);

c) 03 (assunção de dívida);

d) 99 (outros motivos).

Art. 5º Foram realizadas as seguintes modificações, com vigência a partir da data-base de novembro de 2020:

I -  Anexo 26 - Informações Adicionais, domínio 03 (Saídas): exclusão dos subdomínios:

a) 05 (Renegociada);

b) 07 (Saída por alteração de código de contrato ou modalidade/submodalidade);

c) 12 (Saída por incorporação de instituição financeira);

d) 13 (Saída por assunção de dívida).

Art. 6º Esta Carta Circular entra em vigor na data de sua publicação, observado o cronograma estabelecido no art. 3º da Circular nº 3.953, de 10 de julho de 2019.

Gilneu Francisco Astolfi Vivan
