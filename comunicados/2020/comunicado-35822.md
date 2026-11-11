---
titulo: "Comunicado N° 35.822"
orgao: "Banco Central do Brasil"
tipo: "Comunicado"
numero: "35822"
data: 2020-06-18
ementa: "Divulga informações complementares sobre a utilização das mensagens de afastamento de sigilo bancário do Catálogo 4.14 do CCS (mensagens CCS0011 e CCS0012)."
revogada: false
responsavel: "DEATI"
versao_texto: "texto do portal do BCB"
fonte: "https://www.bcb.gov.br/estabilidadefinanceira/exibeoutrasnormas?tipo=Comunicado&numero=35822"
baixado_em: 2026-11-11
---
# Comunicado N° 35.822

Divulgamos informações complementares sobre as mensagens CCS0011 e CCS0012, implantadas em produção em 13 de abril de 2020, com vistas a esclarecer acerca dos cenários de utilização das mensagens de afastamento de sigilo bancário, objeto dos comunicados nº 34.459, de 17 de outubro de 2019, e nº 35.189, de 14 de fevereiro de 2020.

2.       Como definido no Documento de Requisitos do Negócio (DRN) – Requisição de movimentações – do Catálogo 4.14 do CCS, os cenários de utilização das mensagens de afastamento de sigilo bancário são: Cenário 1 - utilização por Comissão de Inquérito (Coinq); e Cenário 2: utilização pelo Judiciário. Complementamos o Cenário 2 com as definições e esclarecimentos decorrentes das alterações consolidadas no Comunicado nº 34.435, de 15 de outubro de 2019, que contempla também a explicação das *tags* de maior relevância das mensagens CCS0011 e CCS0012, para sanar as dúvidas decorrentes do início da utilização dessas mensagens.

3.       São definidos ainda os subcenários de quebra de sigilo, que dependem das informações solicitadas e da forma de envio. Assim, as informações requisitadas podem ser transmitidas: Subcenário 2.1 - exclusivamente pelo Sistema de Investigação de Movimentações Bancárias (Simba); Subcenário 2.2 – exclusivamente por e-mail institucional; e Subcenário 2.3 – concomitante pelos 2 meios de transmissão, com envio pelo e-mail institucional de todas as informações solicitadas, podendo o envio ser fracionado, e com o encaminhamento pelo Simba das informações passíveis de transmissão por esse meio.

4.        A tabela a seguir descreve e exemplifica todas as *tags* da mensagem CCS0011. Tais  informações complementam as validações e os tipos de dados definidos nos arquivos XSD do catálogo vigente, disponíveis na página de Comunicação Eletrônica de Dados no Sistema Financeiro, no endereço: https://www.bcb.gov.br/estabilidadefinanceira/comunicacaodados. Por sua vez, a definição dos domínios está disponível no endereço: https://www.bcb.gov.br/content/estabilidadefinanceira/cedsfn/Catalogos/Documentos\_auxiliares/Dicionario\_dominios/Dom20200529.xls.

|  |  |
| --- | --- |
| **Tag** | **Descrição** |
| CodMsg | Conteúdo fixo: CCS0011. |
| NumCtrlCCS | Número único por mensagem, para identificação das mensagens enviadas pelo CCS.    Essa tag deve ser utilizada na mensagem de retorno (CCS0012), na tag NumCtrlCCSOr, para associar a mensagem de retorno à respectiva mensagem de envio da ordem. |
| CNPJBaseEntRespons | CNPJ base (8 primeiros dígitos) da entidade responsável pelo envio das informações.    No caso de instituição que pertença a um agrupamento, é a instituição líder do agrupamento, definida no cadastro das instituições no CCS.    No caso de instituição que não participa de agrupamento, é o CNPJ base da instituição. |
| CNPJBasePart | CNPJ base (8 primeiros dígitos) da instituição que possui o relacionamento com o cliente.    No caso de instituição que pertença a um agrupamento, pode ser o CNPJ da instituição líder, quando o relacionamento é direto com a líder, ou o CNPJ de uma outra empresa do agrupamento, quando o relacionamento é com essa empresa.    No caso de instituições que não participam de agrupamento, o conteúdo desta tag é igual ao da tag CNPJBaseEntRespons. |
| TpPessoa | Tipo de pessoa.    O domínio é: ‘F’ para pessoa física e ‘J’ para pessoa jurídica. |
| CNPJ\_CPFPessoa | Número de Identificação da Pessoa Jurídica no Cadastro Nacional de Pessoa Jurídica (CNPJ) ou o Número no Cadastro de Pessoa Física (CPF).    Formatação: somente números. |
| DtIni | Data de início do período de afastamento do sigilo bancário. O período de afastamento inclui esta data. |
| DtFim | Data de término do período de afastamento do sigilo bancário. O período de afastamento inclui esta data. |
| CodSistEnvio | Sistema utilizado para envio das informações solicitadas.    Domínio (opções definidas no XSD):    ‘S’ para envio via Simba; dependendo das informações solicitadas, existe a possibilidade de envio apenas via Simba, quando solicitado apenas o extrato de movimentação via Simba, ou envio via Simba e e-mail institucional, quando solicitadas informações que não são passíveis de transmissão via Simba.    ‘T’ para envio futuro pelo STA; no momento a opção ‘T’ define que o envio deve ser realizado por e-mail institucional. |
| SiglaOrgaoCCSDest | Sigla do órgão destinatário das informações solicitadas.    No caso do envio via Simba (CodSistEnvio = ‘S’), a tag será preenchida com a sigla do órgão de destino que consta no caso Simba (tag NumCtrlEnvio).    Exemplo: Para o código de caso Simba 002-PF-123456-12, a tag SiglaOrgaoCCSDest será preenchida com PF.    Quando o sistema de envio for STA (CodSistEnvio = ‘T’), a tag será preenchida com JUD, indicando que a informação será transmitida para um órgão do judiciário. |
| NumCtrlAutcQuebrSigl | Número identificador (único) de uma autorização de quebra de sigilo. Este identificador é o mesmo em todas as mensagens CCS0011 de uma autorização de quebra de sigilo. |
| NumCtrlEnvio | No caso do envio via Simba (CodSistEnvio = ‘S’), a tag será preenchida com o número de caso Simba (número de cooperação técnica).    Quando o sistema de envio for STA (CodSistEnvio = ‘T’), a tag será preenchida com o identificador único da requisição no sistema CCS. |
| NumProcJud | Número do Processo Judicial informado. |
| CodTribl | Código do tribunal associado a conta que autorizou a quebra de sigilo.    Esse código segue a Resolução nº 65 do CNJ, de 16 de dezembro de 2008. O tribunal é identificado por 3 dígitos. O primeiro dígito identifica o segmento do Poder Judiciário (Art. 1º, § 4º) e os dois próximos dígitos identificam o tribunal do respectivo segmento (Art. 1º, § 5º).    Esses códigos são publicados no layout do arquivo 12 (arquivo de varas e juízos), publicado no site do Bacen Jud e enviado às instituições participantes, nos campos TIPO\_JUSTICA (nesse caso sem o zero à esquerda) e NUMERO\_ JUDICIARIO\_TRIBUNAL.    Exemplo: 611 identifica o TRE-MT, pois 6 identifica a Justiça Eleitoral e ‘11’ o TRE-MT (os valores atuais do campo TIPO\_JUSTICA do Bacen Jud serão atualizados de acordo com a resolução supracitada). |
| NomTribl | Nome do tribunal associado a conta que autorizou a quebra de sigilo. |
| CodVaraTribl | Código da vara informada como origem da quebra de sigilo.    Essa tag é preenchida com um código de 3 dígitos que identifica unicamente uma vara no tribunal, como consta no cadastro do Bacen Jud. Esse código é publicado no layout do arquivo 12 (arquivo de varas e juízos), no campo NUMERO\_JUDICIARIO\_VARA, publicado no site do Bacen Jud e enviado às instituições participantes.    Para as varas cujo código esteja faltando na base de dados do Bacen Jud, esta tag será preenchida com o código ‘999’. |
| NomVaraTribl | Nome da vara informada como origem da quebra de sigilo. |
| NomJuiz | Nome do juiz que autorizou a quebra de sigilo, mesmo que por delegação. |
| DescCargoJuiz | Cargo do juiz que autorizou a quebra de sigilo, mesmo que por delegação. |
| TxtObsOrdem | Campo texto utilizado para o envio padronizado das informações requeridas na quebra de sigilo, bem como de informações adicionais para a operacionalização da ordem. Esse campo não é utilizado para o envio de texto livre, sendo o preenchimento realizado pelo SISBAJUD, sistema que irá substituir gradualmente o Bacen Jud, baseado nas opções selecionadas pelo demandante. |
| DtHrLimResp | Data e hora limite para o atendimento da ordem de afastamento de sigilo bancário dentro do prazo estipulado pelo demandante. |
| DtHrBC | Data e hora da geração do processamento da mensagem no BC. |
| DtMovto | Data de movimento da mensagem. |

5.        A tabela abaixo define as hashtags envidas na *tag* TxtObsOrdem. Reforça-se que essa tag não será utilizada para o envio de texto livre, admitindo apenas hashtags padronizadas, para que o tratamento seja padronizado e possa ser automatizado pelas instituições participantes. Cada hashtag é separada por um espaço em branco:

|  |  |  |
| --- | --- | --- |
| **Hashtag** | **Nome** | **Descrição** |
| #extratoMovimentacao  CartaCircular3454    [*sem espaços ou quebra de linha]* | Extrato de movimentação - Carta-Circular 3454 (Simba) | Extrato de movimentação no formato definido pela Carta-Circular 3.454/2010 (padrão Simba), em formato estruturado para análise de dados, com identificação de origem e destino das movimentações.    Essas informações poderão ser enviadas via sistema Simba, o que exige o preenchimento do número de Caso Simba, e/ou por e-mail. |
| #extratoMercantil | Extrato Mercantil | Extrato de movimentação mercantil, em formato aberto (txt, csv, xlsx, ...) e estruturado para análise de dados, sem identificação de origem e destino das movimentações.    Essa opção tem a vantagem de ser atendida mais rapidamente que a opção de extrato no formato da Carta-Circular 3454/2010.    Essas informações serão enviadas ao e-mail institucional, informado necessariamente. |
| #extratoAplicacoesFinanceiras | Extrato de aplicações financeiras | Essas informações serão fornecidas preferencialmente em formato aberto (txt, csv, xlsx, ...) e/ou PDF/A e enviadas ao e-mail institucional, informado necessariamente. |
| #faturaCartaoCredito | Fatura de cartão de crédito | Essas informações serão fornecidas preferencialmente em formato aberto (txt, csv, xlsx, ...) e/ou PDF/A e enviadas ao e-mail institucional, informado necessariamente. |
| #propostaAberturaConta | Proposta de abertura de conta | Essas informações serão fornecidas preferencialmente em PDF/A e enviadas ao e-mail institucional, informado necessariamente. |
| #registroCambio | Movimentação (remessas e recebimento) de Câmbio | Registro de movimentações de câmbio, incluindo as remessas e recebimentos de recursos internacionais, operações de câmbio, outros registros de manutenção de recursos no exterior,  conversões de moeda estrangeira em moeda nacional e transferências de moeda e outros valores para o exterior.    Essas informações serão fornecidas preferencialmente em formato aberto (txt, csv, xlsx, ...) e/ou PDF/A e enviadas ao e-mail institucional, informado necessariamente. |
| #contratoCambio | Contrato de Câmbio | Cópia dos contratos de câmbio mantidos nas instituições.    Essas informações serão fornecidas preferencialmente em formato aberto (txt, csv, xlsx, ...) e/ou PDF/A e enviadas ao e-mail institucional, informado necessariamente. |
| #copiaCheque | Cópia de cheque | Essas informações serão fornecidas em formato PDF/A e enviadas ao e-mail institucional, informado necessariamente. |
| #mailto:{email} | E-mail institucional | Endereço de e-mail institucional a ser utilizado para o envio das informações solicitadas pelas demais tags, incluindo as geradas no formato definido pela Carta-Circular 3.454/2010.    As informações que não puderem ser enviadas pelo Simba deverão ser obrigatoriamente enviadas pelo e-mail informado. Caso o sistema de envio seja Simba (tag CodSistEnvio = ‘S’), deverá ocorrer a transmissão pelos dois meios (e-mail e Simba).    A variável {email} será substituída pelo e-mail institucional informado pelo juízo. Exemplo: #mailto:email-da-vara@tjmt.jus.br |

6.         O cenário 2.2, de envio exclusivo pelo e-mail institucional, bem como as hashtags #extratoMercantil e #registroCambio, definidas na tabela anterior, terão o início de utilização definido para 27/6, data de implantação do Catálogo 5.00.

7.         Enquanto não existir hashtags ou tag para informar se o demandante deseja ou não afastar o sigilo para as contas e produtos nos quais os investigados são apenas procuradores, representantes ou autorizados a movimentar os recursos, deve-se tratar a quebra de sigilo também para essas contas que os investigados não necessariamente constam como titulares.

8.           A tabela abaixo descreve as tags da mensagem CCS0012:

|  |  |
| --- | --- |
| **Tag** | **Descrição** |
| CodMsg | Conteúdo fixo: CCS0012. |
| NumCtrlIF | Número de controle da instituição participante para identificação única da resposta. |
| CNPJBaseEntRespons | CNPJ base (8 primeiros dígitos) da entidade responsável pelo envio das informações. Deve ser preenchida com o conteúdo da mesma tag da mensagem CCS0011 que deu origem à resposta. |
| NumCtrlCCSOr | Deve ser preenchida com o conteúdo da tag NumCtrlCCS da mensagem CCS0011 que deu origem à resposta. |
| SitAtedmntReq | Domínio que define a situação do atendimento da ordem. A próxima tabela aprofunda a explicação dos valores desse domínio. |
| NumCtrlEntr | Número de controle de entrega, que varia conforme a forma de envio definida na mensagem CCS0011.    No caso do envio via Simba (CodSistEnvio = ‘S’), a tag deverá ser preenchida com comprovante de envio pelo Simba.    Quando o sistema de envio for STA (CodSistEnvio = ‘T’), a tag deverá ser preenchida com o valor da tag NumCtrlEnvio. |
| DtHrEntr | Data e hora do envio da informação solicitada.    No caso do envio via Simba (CodSistEnvio = ‘S’), a tag deverá ser preenchida com a data e hora informada no recibo de envio pelo Simba.    Quando o sistema de envio for STA (CodSistEnvio = ‘T’), a tag deverá ser preenchida com a data e gora do último e-mail enviado. |
| TxtObsResp | Campo texto livre opcional disponível para a instituição reportar detalhes relevantes do atendimento. |
| DtMovto | Data de movimento da mensagem. |

9.         A próxima tabela descreve a utilização do domínio da situação do atendimento da ordem (tag SitAtedmntReq):

|  |  |  |
| --- | --- | --- |
| **Valor do domínio** | **Descrição do domínio** | **Observações** |
| 01 | Solicitação atendida | Valor utilizado quando a solicitação for atendida, mesmo nos casos em que a informação solicitada não existir para o cliente no período de afastamento do sigilo.    Por exemplo: se o cliente não possuir cartão de crédito e a ordem determinar o envio apenas dessa informação. |
| 02 | Relacionamento migrado para outra instituição financeira | A informação solicitada, levando-se em conta o período de afastamento do sigilo, é de responsabilidade de outra instituição, devido a transferência do cliente para outra instituição participante.    Os detalhes, incluindo a instituição atualmente responsável pelas informações, devem ser enviados pela tag TxtObsResp. |
| 03 | Relacionamento inexistente | O investigado não possui relacionamento com a instituição no período de afastamento do sigilo. |
| 04 | Liminar | Deve ser utilizado no caso de existência de ordem judicial que impede o envio das informações solicitadas. |
| 05 | Conta inválida | Não deve ser utilizado. Previsão para futura expansão da mensagem para indicação eventual de agência e conta. |
| 06 | Conta inexistente | Não deve ser utilizado. Previsão para futura expansão da mensagem para indicação eventual de agência e conta. |
| 07 | Conta encerrada | Não deve ser utilizado. Previsão para futura expansão da mensagem para indicação eventual de agência e conta. |
| 08 | Agência inexistente | Não deve ser utilizado. Previsão para futura expansão da mensagem para indicação eventual de agência e conta. |

10.       Os e-mails enviados ao destinatário devem constar no início do assunto: ‘Quebra de sigilo NumCtrlAutcQuebrSigl - Envio NumCtrlEnvio’, substituindo as tags pelos respectivos valores.

11.        Mesmo que a mensageria permita o envio de ordens em janela mais ampla, o SISBAJUD irá enviar as mensagens na mesma janela de horário das demais mensagens do CCS. Na homologação será possível o envio em qualquer horário.

12.         As mensagens CCS0011 enviadas em produção pelos tribunais do Banco Central do Brasil não são ordens reais, sendo utilizadas para verificação do ambiente, devendo ser tratadas tempestivamente com envio de informações fictícias e retorno das mensagens de resposta (CCS0012). Nesses casos, não deve ocorrer a transmissão de informações via Simba, já que o número de caso Simba informado é fictício.

13.       Eventuais dúvidas acerca do Grupo de Serviços CCS deverão ser dirimidas exclusivamente pelo e-mail ccs@bcb.gov.br.

|  |
| --- |
| Departamento de Atendimento Institucional  Carlos Eduardo Rodrigues da Cunha Gomes |
| Chefe de Unidade      Departamento de Tecnologia da Informação |
| Haroldo Jayme Martins Froes Cruz |
| Chefe de Unidade |
