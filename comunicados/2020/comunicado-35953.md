---
titulo: "Comunicado N° 35.953"
orgao: "Banco Central do Brasil"
tipo: "Comunicado"
numero: "35953"
data: 2020-07-22
ementa: "Divulga novos subcenários de utilização das mensagens de afastamento de sigilo bancário do Catálogo 5.00 do CCS (mensagens CCS0011 e CCS0012), para contemplar o envio das informações solicitadas por meio do Sistema de Transferência de Arquivos (STA)"
revogada: false
responsavel: "DEATI"
versao_texto: "texto do portal do BCB"
fonte: "https://www.bcb.gov.br/estabilidadefinanceira/exibeoutrasnormas?tipo=Comunicado&numero=35953"
baixado_em: 2026-11-11
---
# Comunicado N° 35.953

O Banco Central do Brasil, com base no disposto no art. 10, inciso IX, e 11, inciso VII, da Lei nº 4.595, de 31 de dezembro de 1964, e no art. 10-A da Lei nº 9.613, de 3 de março de 1998, tendo em conta o art. 2º, inciso II da Circular nº 3.347, de 11 abril de 2007, traz a público informações complementares ao Comunicado nº 35.822, de 18 de junho de 2020, sobre as mensagens CCS0011 e CCS0012, com vistas a esclarecer acerca dos cenários de utilização das mensagens de afastamento de sigilo bancário, para contemplar o envio das informações solicitadas por meio do Sistema de Transferência de Arquivos (STA), cuja utilização foi estabelecida por meio da Carta-Circular nº 3.588, de 18 de março de 2013.

2.         Como definido no Comunicado nº 34.818, de 5 de dezembro de 2019, foi feita, em 27 de junho de 2020, a implantação em produção dos sistemas constantes do Catálogo de Serviços do SFN, em sua versão 5.00. Nesse escopo, ficam alterados os subcenários de utilização das aludidas mensagens de afastamento de sigilo bancário do referido catálogo, para contemplar o envio das informações solicitadas por meio do STA, a partir de 24 de agosto de 2020. O período de homologação do envio por meio do STA será de 3 a 21 de agosto e a implantação em produção ocorrerá em 24 de agosto de 2020.

3.      Dessa forma, ficam alterados os Subcenários 2.1 e 2.2 do Cenário 2, de utilização das aludidas mensagens pelo Judiciário, descritos no Comunicado nº 35.822, de 18 de junho de 2020, para as seguintes formas de transmissão das informações requisitadas: pelo Simba – Sistema de Investigação de Movimentações Bancárias e STA (Subcenário 2.1) ou exclusivamente pelo STA (Subcenário 2.2). O Subcenário 2.3 fica descontinuado no ambiente de produção a partir de 24 de agosto de 2020.

4.        Conforme divulgado por meio do Comunicado n° 34.977, de 27 de dezembro de 2019, o segmento das cooperativas de crédito já responde as mensagens CCS0009, CCS0011 e CCS0012 desde a implantação do Catálogo 5.00. Complementamos que as cooperativas deverão enviar arquivos ACCS100, quando os cenários assim exigirem, incluindo o cenário 1, para quebra de sigilo solicitado por Comissão de Inquérito (Coinq). Esclarecemos, por fim, que o segmento seguirá o cronograma de homologação e implantação informado no parágrafo anterior.

5.        A tabela a seguir descreve e exemplifica todas as *tags* da mensagem CCS0011 com alteração de conteúdo ou conceito. Tais informações complementam as validações e tipos de dados definidos nos arquivos XSD do catálogo vigente, disponíveis na página de Comunicação Eletrônica de Dados no Sistema Financeiro, no endereço: https://www.bcb.gov.br/estabilidadefinanceira/comunicacaodados. Por sua vez, a definição dos domínios está disponível no endereço: https://www.bcb.gov.br/content/estabilidadefinanceira/cedsfn/Catalogos/Documentos\_auxiliares/Dicionario\_dominios/Dom20200529.xls.

|  |  |
| --- | --- |
| **Tag** | **Descrição** |
| CodSistEnvio | Sistema utilizado para envio das informações solicitadas.  Domínio (opções definidas no XSD):    ‘S’ para envio via Simba das informações passíveis de envio por este meio e pelo STA de todas as informações solicitadas, incluindo as enviadas pelo Simba.    ‘T’ para envio pelo STA, contemplando todas as informações solicitadas. |
| TxtObsOrdem | Exclusão e inclusão de hashtags, como descrito na próxima tabela. |

6.        A próxima tabela define as inclusões, alterações e exclusões das hashtags envidas na *tag* TxtObsOrdem. Reforça-se que essa tag não será utilizada para o envio de texto livre, admitindo apenas hashtags padronizadas, para que o tratamento seja padronizado e possa ser automatizado pelas instituições participantes. Cada hashtag deve ser separada de outra por um espaço em branco.

|  |  |  |  |
| --- | --- | --- | --- |
| **Hashtag** | **Nome** | **Descrição** | **Alteração** |
| #contador:{contador} | Contador de mensagem de demanda judiciais | Contador de mensagens.  A variável {contador} será preenchida no formato x/t.  Sendo:    x: contador sequencial de mensagens.    t: total de mensagens.    Exemplos: 1/27, 2/27, 27/27, 19/200, 127/200. | Inclusão |
| #extratoMovimentacao  CartaCircular3454    *[sem espaços ou quebra de linha]* | Extrato de movimentação - Carta-Circular 3.454 (Simba) | Extrato de movimentação no formato definido pela Carta-Circular 3.454/2010 (padrão Simba), em formato estruturado para análise de dados, com identificação de origem e destino das movimentações.    Essas informações poderão ser enviadas via sistema Simba, o que exige o preenchimento do número de Caso Simba, e ficarão disponíveis na tela do sistema, assim que enviadas pelas instituições demandadas. | Alteração de descrição |
| #extratoMercantil | Extrato Mercantil | Extrato de movimentação mercantil, em formato aberto (txt, csv, xlsx, ...) e estruturado para análise de dados, sem identificação de origem e destino das movimentações.    Essa opção tem a vantagem de ser atendida mais rapidamente que a opção de extrato no formato da Carta-Circular 3454/2010.    Essas informações ficarão disponíveis na tela do sistema, assim que enviadas pelas instituições demandadas. | Alteração de descrição |
| #extratoAplicacoesFinanceiras | Extrato de aplicações financeiras | Essas informações serão fornecidas preferencialmente em formato aberto (txt, csv, xlsx, ...) e/ou PDF/A e ficarão disponíveis na tela do sistema, assim que enviadas pelas instituições demandadas. | Alteração de descrição |
| #faturaCartaoCredito | Fatura de cartão de crédito | Essas informações serão fornecidas preferencialmente em formato aberto (txt, csv, xlsx, ...) e/ou PDF/A e ficarão disponíveis na tela do sistema, assim que enviadas pelas instituições demandadas. | Alteração de descrição |
| #propostaAberturaConta | Proposta de abertura de conta | Essas informações serão fornecidas preferencialmente em PDF/A e ficarão disponíveis na tela do sistema, assim que enviadas pelas instituições demandadas. | Alteração de descrição |
| #registroCambio | Registro de Câmbio | Registros de movimentações de câmbio, incluindo os ingressos e remessas de recursos internacionais, operações de câmbio, registros de manutenção de recursos no exterior, conversões de moeda estrangeira em moeda nacional e transferências de moeda e outros valores para o exterior.    Essas informações serão fornecidas preferencialmente em formato aberto (txt, csv, xlsx, ...) e/ou PDF/A e ficarão disponíveis na tela do sistema, assim que enviadas pelas instituições demandadas. | Alteração de nome e de descrição |
| #contratoCambio | Contrato de Câmbio | Cópia dos contratos de câmbio mantidos nas instituições.    Essas informações serão fornecidas preferencialmente em formato aberto (txt, csv, xlsx, ...) e/ou PDF/A e ficarão disponíveis na tela do sistema. | Alteração de descrição |
| #copiaCheque | Cópia de cheque | Essas informações serão fornecidas em formato PDF/A e ficarão disponíveis na tela do sistema. | Alteração de descrição |
| #mailto:{email} |  |  | Exclusão.    As informações solicitadas não serão mais enviadas por e-mail. |
| #emailContato:{email} | E-mail institucional para contato pelas instituições participantes | E-mail institucional a ser utilizado para contatos por parte das instituições participantes exclusivamente para comunicação, sendo vedado o envio de informações sigilosas.    A variável {email} será substituída pelo e-mail institucional informado pelo juízo.    Exemplo: #emailContato:email-da-vara@tjmt.jus.br | Inclusão |
| #telefonesContato:{telefones} | Telefones para contato pelas instituições participantes | Telefones (um ou mais) para contato pelas instituições participantes.    A variável {telefones} será substituída pelos telefones informados pelo juízo. Caso sejam informados múltiplos telefones de contatos, eles serão separados por “;”, sem espaço entre eles ou entre o DDD, que virá ente parênteses e o número, que conterá apenas dígitos.    Exemplo com um telefone: #telefonesContato:(61)34142156    Exemplo com dois telefones: #telefonesContato:(61)34142156;(61)999999999 | Inclusão |

7.        A tabela abaixo descreve as alterações das tags da mensagem CCS0012.

|  |  |
| --- | --- |
| **Tag** | **Descrição** |
| NumCtrlEntr | Número de controle de entrega não varia conforme a forma de envio definida na mensagem CCS0011. Ou seja, tanto para o envio via Simba (CodSistEnvio = ‘S’), quanto para o envio via STA (CodSistEnvio = ‘T’), a tag deverá ser preenchida com o protocolo do STA. O número de comprovante Simba, no caso de envio por este meio, deve ser informado na tag TxtObsResp. |
| DtHrEntr | Data e hora do envio da informação solicitada.    Tanto para o envio via Simba (CodSistEnvio = ‘S’), quanto para o envio via STA (CodSistEnvio = ‘T’), a tag deverá ser preenchida com data e hora do protocolo de envio do arquivo STA. |
| TxtObsResp | Para mensagens associadas ao envio via Simba (CodSistEnvio = ‘S’), este campo deve iniciar com a hashtag #comprovanteTransmissaoSimba:{numero-comprovante} e ser seguido por um espaço em branco.    A variável {numero-comprovante} deve ser preenchida com o número de comprovante de transmissão do Simba.    Exemplo: #comprovanteTransmissaoSimba:12345    O restante do campo é um texto livre e opcional, disponível para a instituição reportar detalhes relevantes do atendimento. O conteúdo desse campo ficará disponível na tela do sistema. |

8.        O arquivo ACSS100 deverá ser necessariamente um arquivo compactado em formato zip, contendo todos os arquivos solicitados e apurados até o momento do envio. O nome do arquivo deve ser composto pela tag NumCtrlEnvio da mensagem CCS0011 e, caso seja um arquivo de substituição, deve-se concatenar um caractere “\_” e um sequencial iniciando em 1.

9.      Conteúdo, layout, nomes de arquivos e demais regras relacionadas ao fornecimento de dados transmitidos ao Simba não sofrerão alterações. Os arquivos transmitidos ao Simba devem constar na raiz do arquivo zip enviado ao STA e devem respeitar o formato da Carta-Circular 3.454, de 14 de junho de 2010, ou outro layout acordado com a Unidade gestora do Simba, como no caso das Corretoras e Distribuidoras de Títulos e Valores Mobiliários.

10.        Os demais arquivos solicitados pelas hashtags contidas no campo TxtObsOrdem da mensagem CCS0011 e detalhados no item 5 deste comunicado, também deverão estar localizados na raiz do arquivo compactado e ter o nome iniciado com a respectiva hashtag, sem o caractere “#”, seguido de “\_” e um número sequencial iniciando-se em 1. Por exemplo, se a hashtag “#copiaCheque” deu origem a 3 arquivos na resposta, os nomes desses arquivos deverão ser necessariamente: “copiaCheque\_1”, “copiaCheque\_2” e “copiaCheque\_3”. As extensões desses arquivos podem ser uma das permitidas na descrição da hashtag na tabela do item 6.

11.      A disponibilização do arquivo de resposta (ACCS100) ao demandante está condicionada ao envio da mensagem CCS0012 indicando que os dados solicitados já foram entregues. A mensagem CCS0012 será vinculada ao arquivo ACCS100 por meio da tag NumCtrlEntr, que conterá o protocolo STA do arquivo entregue. A confirmação (CCS0012R1) de recepção da mensagem é gerada imediatamente ao recebimento. Caso exista algum problema na mensagem, será retornado uma mensagem de erro (CCS0012E). Uma vez entregue a mensagem, com sucesso, o arquivo será validado e disponibilizado ao solicitante. Esse passo pode levar alguns minutos ou horas, a depender do tamanho do arquivo entregue.

12.       Caso o ACCS100 seja rejeitado será disponibilizado um relatório de erros, com informações sobre os problemas encontrados, que devem ser corrigidos para um novo envio. O relatório associado ao arquivo enviado estará disponível no STA. O não envio da mensagem CCS0012 confirmando a entrega do arquivo ACCS100, em um intervalo de 5 dias, irá gerar a rejeição do arquivo.

13.       A não recepção de confirmação da mensagem CCS0012, através das mensagens CCS0012R1 ou CCS0012E, deve ser comunicada a este Banco Central tão logo percebido atraso superior a uma hora.

14.       Quanto ao conteúdo dos arquivos solicitados, no caso de arquivos Simba, deve-se seguir sempre o layout da Carta-Circular 3.454, de 2010. Já para os arquivos associados as hashtags, eles deverão ser fornecidos em formato aberto, preferencialmente em formato estruturado, para facilitar a sua análise. As especificações dos tipos de arquivos aceitos para cada informação solicitada consta na descrição das hashtags na tabela do item 5.

15.      As instituições participantes podem enviar vários arquivos ACCS100 e mensagens CCS0012 para responder a uma mensagem CCS0011, A última mensagem CCS0012 substituirá as anteriores no sistema e na tela acessada pelo Judiciário. O arquivo exibido na tela de detalhamento da resposta será o arquivo cujo protocolo STA foi informado na tag NumCtrlEntr da última mensagem CCS0012 enviada.

16.         No caso de envio de múltiplos arquivos e mensagens de resposta, eles devem conter integralmente as informações enviadas até aquele momento, pois o sistema fará a substituição da mensagem pela última e do arquivo pelo informado nesta última mensagem. O sistema não fará a concatenação das mensagens e arquivos, portanto deve-se enviar a integralidade dos dados levantados até o momento do envio.

17.        Mensagens CCS0011 enviadas em produção pelos tribunais do Banco Central do Brasil não são ordens reais, sendo utilizadas para verificação do ambiente, devendo ser tratadas tempestivamente com envio de informações fictícias e retorno das mensagens de resposta (CCS0012) e arquivos associados (ACCS100). Nesses casos, não deve ocorrer a transmissão de informações via Simba, já que o número de caso Simba informado é fictício. Deve-se, para algumas mensagens CCS0011, enviar várias respostas CCS0012 e arquivos associados, para o Banco Central possa verificar o processamento.

18.      Eventuais dúvidas acerca do Grupo de Serviços CCS deverão ser dirimidas exclusivamente pelo e-mail ccs@bcb.gov.br.

Departamento de Atendimento Institucional

Carlos Eduardo Rodrigues da Cunha Gomes
              Chefe de Unidade

Departamento de Tecnologia da Informação

Haroldo Jayme Martins Froes Cruz
              Chefe de Unidade
