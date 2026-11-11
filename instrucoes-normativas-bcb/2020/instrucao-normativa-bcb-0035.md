---
titulo: "Instrução Normativa BCB N° 35"
orgao: "Banco Central do Brasil"
tipo: "Instrução Normativa BCB"
numero: "35"
data: 2020-10-29
ementa: "Divulga a versão 1.0 do Manual de Escopo de Dados e Serviços do Open Banking."
revogada: true
responsavel: "DENOR"
versao_texto: "texto do portal do BCB"
versao_normativo: "2"
publicacao: "Publicada no DOU de 13/11/2020, Seção 1, p. 51-55."
atualizacoes: ["Instrução Normativa BCB nº 96/2021 - Revogação total."]
normas_vinculadas: ["RESOLUÇÃO CONJUNTA 1/2020", "INSTRUÇÃO NORMATIVA BCB 96/2021", "RESOLUÇÃO BCB 32/2020", "RESOLUÇÃO 4072/2012", "RESOLUÇÃO 3954/2011", "RESOLUÇÃO 3919/2010", "CIRCULAR 4015/2020"]
referencias: ["Portaria BCB nº 84.287/2015, Anexo (Regimento Interno do BCB), arts. 23, inciso I, \"a\", e 62, inciso IV.", "Resolução BCB nº 32/2020, art. 3º, inciso I.", "Cita Resolução Conjunta CMN/BCB nº 1/2020.", "Cita Resoluções CMN ns. 3.919/2010 e 4.072/2012.", "Cita Resolução CMN nº 3.954/2011, art. 8º.", "Cita Circular BCB nº 4.015/2020.", "Cita Resolução BCB nº 32/2020."]
fonte: "https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Instru%C3%A7%C3%A3o%20Normativa%20BCB&numero=35"
baixado_em: 2026-11-10
---
# Instrução Normativa BCB N° 35

INSTRUÇÃO NORMATIVA BCB Nº 35, DE 29
DE OUTUBRO DE 2020

[Documento normativo revogado pela
Instrução Normativa BCB nº 96, de 14/4/2021.](https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Instru%C3%A7%C3%A3o%20Normativa%20BCB&numero=96)

Divulga a versão 1.0 do Manual de Escopo de Dados e Serviços do **Open Banking**.

Os Chefes do Departamento de Regulação do Sistema Financeiro (Denor) e de Tecnologia da Informação (Deinf), no uso das atribuições que lhe conferem os arts. 23, inciso I, alínea "a", 62, inciso IV, do Regimento Interno do Banco Central do Brasil, anexo à Portaria nº 84.287, de 27 de fevereiro de 2015, com base no art. 3º, inciso I, da Resolução BCB nº 32, de 29 de outubro de 2020,

R E S O L V E M :

Art. 1º  Esta Instrução Normativa divulga a versão 1.0 do Manual de Escopo de Dados e Serviços do **Open Banking**, de observância obrigatória por parte das instituições participantes, conforme Anexo.

Parágrafo único.  O manual de que trata o **caput**, em sua versão mais recente, estará acessível na página do **Open Banking** no sítio eletrônico do Banco Central do Brasil na internet.

Art. 2º  Esta Instrução Normativa entra em vigor na data de sua publicação.

João André Calvino Marques Pereira                   Haroldo Jayme Martins Froes Cruz
                        Chefe do Departamento de                                   Chefe do Departamento de
                        Regulação do Sistema Financeiro                         Tecnologia da Informação

ANEXO À INSTRUÇÃO NORMATIVA BCB Nº 35, DE 29 DE OUTUBRO DE 2020

**Manual de Escopo de Dados e Serviços do Open Banking Versão 1.0**

# **Histórico de revisão**

|  |  |  |
| --- | --- | --- |
| **Data** | **Versão** | **Descrição das alterações** |
| 29/10/2020 | 1.0 | Versão inicial. |

# **Apresentação**

Este manual detalha os campos referentes aos dados e serviços objeto de compartilhamento no âmbito do **Open Banking**, observado o escopo mínimo disposto na Circular nº 4.015, de 4 de maio de 2020.

# **Termos de Uso**

Este manual detalha os requisitos técnicos para a implementação dos elementos necessários à operacionalização do **Open Banking**, complementando a regulamentação vigente sobre o tema.

O manual será revisto e atualizado periodicamente a fim de preservar a compatibilidade com a regulamentação, bem como para incorporar os aprimoramentos decorrentes da evolução do **Open Banking** e da tecnologia.

Informações mais detalhadas e exemplos da aplicação deste manual poderão ser encontrados nos guias e tutoriais disponíveis no Portal do **Open Banking** no Brasil, na Área do Desenvolvedor.

Sugestões, críticas ou pedidos de esclarecimento de dúvidas relativas ao conteúdo deste documento podem ser enviados ao Banco Central do Brasil por meio dos canais institucionais dessa autarquia.

# **Referências**

Estas especificações baseiam-se, referenciam e complementam, quando aplicável, os seguintes documentos:

|  |  |
| --- | --- |
| **Referência** | **Origem** |
| Resolução Conjunta nº 1, de 2020 | https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20Conjunta&numero=1 |
| Circular nº 4.015, de 2020 | https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Circular&numero=4015 |
| Resolução BCB nº 32, de 2020 | https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20BCB&numero=32 |
| Resolução CMN nº 3.919, de 2010 | <https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o&numero=3919> |
| Resolução CMN nº 4.072, de 2012 | https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o&numero=4072 |
| ISO 4217 | <https://www.iso.org/iso-4217-currency-codes.html> |
| ISO 3166 | https://www.iso.org/iso-3166-country-codes.html |
| Documento 3040 | <https://www.bcb.gov.br/estabilidadefinanceira/scrdoc3040> |

# **1. Introdução**

Os dados e serviços objeto de compartilhamento representam parte primordial do **Open Banking**, pois serão determinantes para o grau de utilidade e interesse no **Open Banking** pela sociedade. Desse modo, a garantia da qualidade, disponibilidade e integridade é fundamental para que os elementos necessários à construção da confiança no **Open Banking** estejam presentes.

Este manual foi elaborado com o objetivo de assegurar o nível de detalhamento e padronização necessários para cada um dos dados relacionados na Resolução Conjunta nº 1 e na Circular nº 4.015, ambas de 2020. Neste documento, os dados são desdobrados em uma série de campos com propósitos específicos, cujo compartilhamento é obrigatório. Excepcionalmente, alguns campos foram assinalados como optativos, de modo a disponibilizar um período para adequação dos sistemas de informação antes da sua conversão em obrigatórios. Finalmente, as instituições participantes do **Open Banking** possuem autonomia para decidir sobre o compartilhamento de dados adicionais aos relacionados neste manual, desde que respeitado o consentimento prévio do cliente ao se tratar de dados pessoais e observada a regulamentação vigente.

Para os aspectos operacionais do **Open Banking**, é necessária a consulta de fontes complementares de informação, disponíveis no Portal do **Open Banking** no Brasil, no qual poderão ser encontradas as especificações relativas a tipo, formato, tamanho e demais atributos pertinentes aos campos de dados, matéria que extrapola a finalidade deste documento.

# **2. Canais de Atendimento**

A Resolução Conjunta nº 1 e a Circular nº 4.015, ambas de 2020, estabelecem a obrigatoriedade de compartilhamento dos dados sobre os canais de atendimento dos participantes, a exemplo dependências próprias, correspondentes no País e canais eletrônicos, além de outros canais disponíveis aos clientes. Esses dados precisam abranger, no mínimo, os divulgados na forma de dados abertos conforme a regulamentação em vigor, e atender, no mínimo, o nível de granularidade especificado nos campos relacionados nas tabelas adiante.

Para a implementação das APIs nos moldes requeridos pela regulamentação vigente, orientações detalhadas de caráter técnico deverão estar previstas no Portal do **Open Banking** no Brasil.

## 2.1              Dependências Próprias

Os campos objeto de compartilhamento obrigatório para os dados de identificação, localização, forma de acesso e serviços prestados de dependências próprias são os relacionados na Tabela 2.1, com exceção dos assinalados com asterisco (\*), de compartilhamento opcional, mas recomendado, considerando a perspectiva de se tornarem obrigatórios no futuro.

Informações adicionais como a visão de alto nível, o dicionário de dados e o código das APIs podem ser encontradas no Portal do **Open Banking** no Brasil.

|  |  |  |
| --- | --- | --- |
| **Dado** | **Campo** | **Esclarecimentos adicionais** |
| Identificação | Marca | Nome da marca reportada pelo participante do **Open Banking**. O conceito a que se refere a marca é, em essência, uma promessa das instituições em fornecer uma série específica de atributos, benefícios e serviços uniformes aos clientes. |
| Nome da instituição | Nome da instituição pertencente à marca, responsável pela dependência. |
| CNPJ da instituição | Número completo do CNPJ da instituição responsável pela dependência. |
| Nome da dependência |  |
| CNPJ da dependência\* |  |
| Código identificador da dependência |  |
| Dígito verificador da dependência |  |
| Campo adicional para URL (CNPJs) - se aplicável | URL de **link**, para lista complementar, com os nomes e CNPJs agrupados no caso de instituições oferecerem produtos e serviços com as mesmas características. |
| Tipo de dependência | Tipo de dependência, segundo a classificação do art. 1º da Resolução CMN nº 4.072, de 2012, discriminados na Seção 4.1 deste manual. |
| Código da agência vinculada ao Posto de Atendimento - se aplicável\* |  |
| Data de abertura da dependência\* |  |
| Localização | Endereço completo |  |
| Complemento\* |  |
| Bairro |  |
| Município |  |
| Código IBGE de município\* | 7 dígitos (o último é um código verificador) |
| Sigla da Unidade de Federação |  |
| CEP |  |
| País\* |  |
| Código do país\* | De acordo com o código "alpha3" do ISO-3166. |
| Latitude\* | Entre -90 e 90. Formato numérico, 2 casas antes da vírgula, 11 posições. |
| Longitude\* | Entre -180 e 180. Formato numérico, 3 casas antes da vírgula, 11 posições. |
| Forma de acesso | Horário de abertura |  |
| Horário de encerramento |  |
| Dias de funcionamento |  |
| Indicador de restrição de acesso\* |  |
| Tipo de telefone\* | Fixo ou celular |
| DDI\* |  |
| DDD\* |  |
| Número de telefone\* |  |
| Serviços prestados | Nomes dos serviços prestados | Relação dos serviços efetivamente prestados, discriminados na Seção 4.2 deste manual. |
| Códigos dos serviços prestados | Códigos dos serviços efetivamente prestados, discriminados na Seção 4.2 deste manual. |

Tabela 2.1: Dados de dependências próprias e respectivos campos

## 2.2              Correspondentes no País

Os campos objeto de compartilhamento obrigatório para os dados de identificação, localização e serviços prestados por correspondentes no País são os relacionados na Tabela 2.2. Os campos assinalados com asterisco (\*) são de compartilhamento opcional, com perspectiva de se tornarem obrigatórios nas próximas fases de implementação do **Open Banking**.

Informações adicionais como a visão de alto nível, o dicionário de dados e o código das APIs podem ser encontradas no Portal do **Open Banking** no Brasil.

|  |  |  |
| --- | --- | --- |
| **Dado** | **Campo** | **Esclarecimentos adicionais** |
| Identificação | Marca | Nome da marca reportada pelo participante do **Open Banking**. O conceito a que se refere a marca é, em essência, uma promessa das instituições em fornecer uma série específica de atributos, benefícios e serviços uniformes aos clientes. |
| Nome da instituição titular | Nome da instituição pertencente à marca, responsável pelo correspondente. |
| CNPJ da instituição titular | Número completo do CNPJ da instituição responsável pelo correspondente. |
| Nome do contratante |  |
| CNPJ do contratante |  |
| Nome do correspondente no País |  |
| Nome do conglomerado do correspondente\* |  |
| CNPJ do correspondente |  |
| Substabelecimento\* | 1. Não; 2. Sim |
| Localização | Endereço completo |  |
| Complemento\* |  |
| Bairro |  |
| Município |  |
| Código IBGE de município\* | 7 dígitos (o último é um código verificador) |
| Sigla da Unidade de Federação |  |
| CEP |  |
| País\* |  |
| Código do país\* | De acordo com o código "alpha3" do ISO-3166. |
| Latitude\* | Entre -90 e 90. Formato numérico, 2 casas antes da vírgula, 11 posições. |
| Longitude\* | Entre -180 e 180. Formato numérico, 3 casas antes da vírgula, 11 posições. |
| Forma de acesso | Horário de abertura\* |  |
| Horário de encerramento\* |  |
| Dias de funcionamento\* |  |
| Indicador de restrição de acesso\* |  |
| Tipo de telefone\* | Fixo ou celular |
| DDI\* |  |
| DDD\* |  |
| Número de telefone\* |  |
| Serviços prestados | Nomes dos serviços prestados | Relação dos serviços efetivamente prestados, discriminados na Seção 4.3 deste manual. |
| Códigos dos serviços prestados | Códigos dos serviços efetivamente prestados, discriminados na Seção 4.3 deste manual. |

Tabela 2.2: Dados de correspondentes no País e respectivos campos

## 2.3         Canais Eletrônicos

Os campos objeto de compartilhamento obrigatório para os dados de tipo, forma de acesso e serviços prestados de canais de atendimento eletrônico são os relacionados na Tabela 2.3.

Informações adicionais como a visão de alto nível, o dicionário de dados e o código das APIs podem ser encontradas no Portal do **Open Banking** no Brasil.

|  |  |  |
| --- | --- | --- |
| **Dado** | **Campo** | **Esclarecimentos adicionais** |
| Canal | Marca | Nome da marca reportada pelo participante do **Open Banking**. O conceito a que se refere a marca é, em essência, uma promessa das instituições em fornecer uma série específica de atributos, benefícios e serviços uniformes aos clientes. |
| Nome da instituição | Nome da instituição pertencente à marca |
| CNPJ da instituição |  |
| Campo adicional para URL (CNPJs) - se aplicável | URL de **link**, para lista complementar, com os nomes e CNPJs agrupados no caso de instituições oferecerem produtos e serviços com as mesmas características. |
| Tipo de canal | **Internet** **banking**, **mobile banking** ou **chat** |
| Forma de acesso | Tipo de acesso | 1.URL para acesso ao **internet banking**  2.URL para aquisição do app  3.URL para **chat**  4.Outros |
| Serviços prestados | Nomes dos serviços prestados | Relação dos serviços efetivamente prestados, discriminados na Seção 4.2 deste manual. |
| Códigos dos serviços prestados | Códigos dos serviços efetivamente prestados, discriminados na Seção 4.2 deste manual. |

Tabela 2.3: Dados de canais de atendimento eletrônico e respectivos campos

## 2.4         Outros Canais Disponíveis

### **2.4.1 Canais Telefônicos**

Os campos objeto de compartilhamento obrigatório para os dados de tipo, forma de acesso e serviços prestados de canais telefônicos são os relacionados na Tabela 2.4.

Informações adicionais como a visão de alto nível, o dicionário de dados e o código das APIs podem ser encontradas no Portal do **Open Banking** no Brasil.

|  |  |  |
| --- | --- | --- |
| **Dado** | **Campo** | **Esclarecimentos adicionais** |
| Canal | Marca | Nome da marca reportada pelo participante do **Open Banking**. O conceito a que se refere a marca é, em essência, uma promessa das instituições em fornecer uma série específica de atributos, benefícios e serviços uniformes aos clientes. |
| Nome da instituição | Nome da instituição pertencente à marca |
| CNPJ da instituição |  |
| Campo adicional para URL (CNPJs) - se aplicável | URL de **link,** para lista complementar, com os nomes e CNPJs agrupados no caso de instituições oferecerem produtos e serviços com as mesmas características. |
| Tipo de canal | Central telefônica, SAC e ouvidoria |
| Forma de acesso | DDI |  |
| DDD |  |
| Número de telefone |  |
| Tipo de acesso | 1. Central telefônica  2. SAC  3. Ouvidoria  4. Outros |
| Serviços prestados | Nomes dos serviços prestados | Relação dos serviços efetivamente prestados, discriminados na Seção 4.2 deste manual. |
| Códigos dos serviços prestados | Códigos dos serviços efetivamente prestados, discriminados na Seção 4.2 deste manual. |

Tabela 2.4.1: Dados de canais telefônicos e respectivos campos

### **2.4.2 Terminais de Autoatendimento****Compartilhados**

Os campos para os dados de identificação, localização, forma de acesso e serviços prestados de terminais de autoatendimento de terceiros compartilhados são os relacionados na Tabela 2.4.2. No momento, o compartilhamento dos dados relativos aos terminais de autoatendimento de terceiros compartilhados é facultativo. Assim, seguindo o padrão das outras seções deste manual para indicação dos campos opcionais, todos os campos foram assinalados com asterisco (\*).

Informações adicionais como a visão de alto nível, o dicionário de dados e o código das APIs podem ser encontradas no Portal do **Open Banking** no Brasil.

|  |  |  |
| --- | --- | --- |
| **Dado** | **Campo** | **Esclarecimentos adicionais** |
| Identificação\* | Marca\* | Nome da marca reportada pelo participante do **Open Banking**. O conceito a que se refere a marca é, em essência, uma promessa das instituições em fornecer uma série específica de atributos, benefícios e serviços uniformes aos clientes. |
| Nome da instituição titular\* | Nome da instituição pertencente à marca, responsável pela dependência. |
| CNPJ da instituição titular\* | Número completo do CNPJ da instituição responsável pela dependência. |
| Campo adicional para URL (CNPJs) - se aplicável\* | URL de **link**, para lista complementar, com os nomes e CNPJs agrupados no caso depara o caso instituições ofertantesoferecerem de produtos e serviços com as mesmas características. |
| Nome do proprietário\* |  |
| Localização\* | Endereço completo\* |  |
| Complemento\* |  |
| Bairro\* |  |
| Município\* |  |
| Código IBGE de município\* | 7 dígitos (o último é um código verificador) |
| Sigla da Unidade de Federação \* |  |
| CEP\* |  |
| País\* |  |
| Código do país\* | De acordo com o código "alpha3" do ISO-3166. |
| Latitude\* | Entre -90 e 90. Formato numérico, 2 casas antes da vírgula, 11 posições. |
| Longitude\* | Entre -180 e 180. Formato numérico, 3 casas antes da vírgula, 11 posições. |
| Forma de acesso\* | Horário de abertura\* |  |
| Horário de encerramento\* |  |
| Dias de funcionamento\* |  |
| Indicador de restrição de acesso\* |  |
| Serviços prestados\* | Nomes dos serviços prestados\* | Relação dos serviços efetivamente prestados, discriminados na Seção 4.2 deste manual. |
| Códigos dos serviços prestados\* | Códigos dos serviços efetivamente prestados, discriminados na Seção 4.2 deste manual. |

Tabela 2.4.2: Dados de terminais de autoatendimento e respectivos campos

# **3. Produtos e Serviços**

A Resolução Conjunta nº 1, de 2020, estabelece a obrigatoriedade de compartilhamento de dados de produtos e serviços relacionados com contas de depósito à vista, contas de depósito de poupança e contas de pagamentos pré-pagas e pós-pagas, enquanto a Circular nº 4.015, de 2020, especifica os campos mínimos desses dados. Esses campos obrigatórios estão relacionados nas tabelas a seguir com informações adicionais e descrição de atributos, quando pertinentes.

Para a implementação das APIs nos moldes requeridos pela regulamentação, orientações detalhadas de caráter mais técnico deverão estar previstas no Portal do **Open Banking** no Brasil.

## 3.1Contas de depósito à vista, de poupança e de pagamento pré-pagas

Os campos objeto de compartilhamento obrigatório para os dados de identificação, tarifas, pacotes de serviços disponibilizados, formas de movimentação, termos e condições contratuais, canais disponíveis para abertura e encerramento, público-alvo e forma de remuneração e taxa de rendimento, conforme o caso, para contas de depósito à vista, contas de depósito de poupança e contas de pagamentos pré-pagas são os relacionados na Tabela 3.1.

Informações adicionais como a visão de alto nível, o dicionário de dados e o código das APIs podem ser encontradas no Portal do **Open Banking** no Brasil.

|  |  |  |
| --- | --- | --- |
| **Dado** | **Campo** | **Esclarecimentos adicionais** |
| Identificação | Marca | Nome da marca reportada pelo participante do **Open Banking**. O conceito a que se refere a marca é, em essência, uma promessa das instituições em fornecer uma série específica de atributos, benefícios e serviços uniformes aos clientes. |
| Nome da instituição | Nome da instituição pertencente à marca |
| CNPJ da instituição |  |
| Campo adicional para URL (CNPJs) - se aplicável | URL de **link**, para lista complementar, com os nomes e CNPJs agrupados no caso depara o caso instituições ofertantesoferecerem de produtos e serviços com as mesmas características. |
| Tipo de conta | Conta de depósito à vista, conta de depósito de poupança ou conta de pagamentos pré-paga, nos termos na regulamentação vigente. |
| Tarifas cobradas por serviços avulsos | Denominação | Relação dos serviços objeto de cobrança de tarifas, conforme Resolução CMN nº 3.919, de 2010. |
| Siglas | Conforme Resolução CMN nº 3.919, de 2010. |
| Fatos geradores de cobrança | Conforme Resolução CMN nº 3.919, de 2010. |
| Moeda | De acordo com o ISO 4217. |
| Valor | Distribuição de frequência relativa dos valores referentes à cobrança de tarifas pela prestação dos serviços prioritários, informados nos termos da Resolução BCB nº 32, de 2020. |
| Pacotes de serviços | Denominação dos pacotes de serviços | Conforme Resolução CMN nº 3.919, de 2010. |
| Nome dos serviços incluídos | Conforme Resolução CMN nº 3.919, de 2010. |
| Fatos geradores de cobrança | Conforme Resolução CMN nº 3.919, de 2010. |
| Moeda | De acordo com o ISO 4217. |
| Eventos previstos no pacote de serviços | Quantidade mensal |
| Moeda | De acordo com o ISO 4217. |
| Tarifa mensal | Distribuição de frequência relativa dos valores referentes à cobrança de tarifas, nos termos da Resolução BCB nº 32, de 2020. |
| Formas de movimentação | Formas de movimentação | 1. movimentação eletrônica  2. movimentação com cheque  3. movimentação com cartão  4. movimentação presencial |
| Termos e condições contratuais | Saldo mínimo (moeda) | De acordo com o ISO 4217. |
| Saldo mínimo (valor) | Campo aberto. |
| Critérios de elegibilidade | Campo aberto. |
| Procedimentos de encerramento | Campo aberto (possibilidade de incluir URL) |
| Canais disponíveis para abertura e encerramento | Lista de canais | 1. dependências próprias, 2. correspondentes no País, 3. **internet banking**, 4. **mobile banking**, 5. central telefônica, 6. **chat**, 7. outros |
| Público-alvo | Lista de público-alvo | 1. Pessoa Natural, 2. Pessoa Jurídica, 3. Ambos |
| Forma de remuneração e taxa de rendimento | Descrição da forma de remuneração, se aplicável | Informação conforme a regulamentação em vigor. |
| Percentual em favor do titular da conta de pagamento pré-paga, se aplicável | Campo aberto. |

Tabela 3.1: Dados de contas de depósito à vista, de poupança e de pagamento pré-pagas e respectivos campos

## 3.2         Contas de pagamento pós-pagas

Os campos objeto de compartilhamento obrigatório para os dados de identificação, programas de benefícios e recompensas, taxas de remuneração, público-alvo e termos e condições contratuais para contas de pagamentos pós-pagas são os relacionados na Tabela 3.2.

Informações adicionais como a visão de alto nível, o dicionário de dados e o código das APIs podem ser encontrados no Portal do **Open Banking** no Brasil.

|  |  |  |
| --- | --- | --- |
| **Dado** | **Campo** | **Esclarecimentos adicionais** |
| Identificação | Marca | Nome da marca reportada pelo participante do **Open Banking**. O conceito a que se refere a marca é, em essência, uma promessa das instituições em fornecer uma série específica de atributos, benefícios e serviços uniformes aos clientes. |
| Nome da instituição | Nome da instituição pertencente à marca |
| CNPJ da instituição |  |
| Campo adicional para URL (CNPJs) - se aplicável | URL de **link**, para lista complementar, com os nomes e CNPJs agrupados no caso depara o caso instituições ofertantesoferecerem de produtos e serviços com as mesmas características |
| Denominação | Identificação do nome da conta de pagamento pós-paga (cartão) |
| Classificação | Categoria atribuída ao cartão de pagamento, sob uma certa denominação, que lhe agrega um conjunto de benefícios, diferenciando-o de acordo com o perfil do cliente. |
| Arranjo de pagamento | Instituidor do arranjo de pagamento. |
| Programa de benefícios e recompensas | Programa de benefícios ou recompensas | 1. Não; 2. Sim |
| Termos e condições do programa | Campo aberto (possibilidade de incluir URL) |
| Tarifas | Denominação | Conforme Resolução CMN nº 3.919, de 2010. |
| Siglas | Conforme Resolução CMN nº 3.919, de 2010. |
| Fatos geradores de cobrança | Conforme Resolução CMN nº 3.919, de 2010. |
| Moeda | De acordo com o ISO 4217. |
| Valor | Distribuição de frequência relativa dos valores referentes à cobrança de tarifas pela prestação de serviços prioritários relacionados à cartão de crédito, informados nos termos da Resolução BCB nº 32, de 2020. |
| Taxas de remuneração | Crédito rotativo (moeda) | De acordo com o ISO 4217. |
| Crédito rotativo (valor) | Distribuição de frequência relativa dos valores referentes ao crédito rotativo nos termos da Resolução BCB nº 32, de 2020. |
| Parcelamento de saldo devedor da fatura (moeda) | De acordo com o ISO 4217. |
| Parcelamento de saldo devedor da fatura | Distribuição de frequência relativa dos valores referentes ao crédito rotativo nos termos da Resolução BCB nº 32, de 2020. |
| Outras operações de crédito | 1. Saque na função crédito, 2. Pagamento de contas, 3.Outros |
| Moeda | De acordo com o ISO 4217. |
| Público-alvo | Lista de público-alvo | 1. Pessoa Natural, 2. Pessoa Jurídica, 3. Ambos |
| Termos e condições contratuais | Regra de pagamento mínimo de saldo devedor da fatura, se aplicável | Percentual do valor do saldo devedor da fatura |
| Critérios de elegibilidade | Campo aberto (possibilidade de incluir URL) |
| Procedimentos de encerramento | Campo aberto (possibilidade de incluir URL) |

Tabela 3.2: Dados de contas de pagamento pós-pagas e respectivos campos

## 3.3         Operações de Crédito

Os campos objeto de compartilhamento obrigatório para os dados de modalidade, tarifas, taxas de juros remuneratórios, público-alvo, tipo de garantia exigíveis e termos e condições contratuais para operações de crédito são os relacionados nas tabelas adiante.

Informações adicionais como a visão de alto nível, o dicionário de dados e o código das APIs podem ser encontradas no Portal do **Open Banking** no Brasil.

### **3.3.1 Adiantamento a Depositantes**

|  |  |  |
| --- | --- | --- |
| **Dado** | **Campo** | **Esclarecimentos adicionais** |
| Identificação | Marca | Nome da marca reportada pelo participante do **Open Banking**. O conceito a que se refere a marca é, em essência, uma promessa das instituições fornecer uma série específica de atributos, benefícios e serviços uniformes aos clientes. |
| Nome da instituição | Nome da instituição, pertencente à marca, responsável pela comercialização das modalidades de direitos creditórios descontados. |
| CNPJ da instituição |  |
| Campo adicional para URL (CNPJs) - se aplicável | URL de **link**, para lista complementar, com os nomes e CNPJs agrupados no caso de instituições oferecerem produtos e serviços com as mesmas características. |
| Tarifas | Denominação | Conforme Resolução CMN nº 3.919, de 2010. |
| Siglas | Conforme Resolução CMN nº 3.919, de 2010. |
| Fatos geradores de cobrança | Conforme Resolução CMN nº 3.919, de 2010. |
| Moeda | De acordo com o ISO 4217. |
| Valor | Distribuição de frequência relativa dos valores referentes às tarifas cobradas pela prestação do serviço prioritário de concessão de adiantamento a depositante, nos termos da Resolução BCB nº 32, de 2020. |
| Taxas de juros remuneratórios | Referencial ou indexador | Tipos de taxas referenciais ou indexadores e percentuais adotados, conforme Anexo do Documento 3040. |
| Taxa pré-fixada contratada | Distribuição de frequência relativa da parcela prefixada dos juros cobrados na situação de adimplência, de acordo com a Resolução BCB nº 32, de 2020, e o Documento 3040. |
| Público-alvo | Lista de público-alvo | 1. Pessoa Natural, 2. Pessoa Jurídica, 3. Ambos |
| Termos e condições contratuais | Termos e condições contratuais | Campo aberto (possibilidade de incluir URL) |

Tabela 3.3.1: Dados de adiantamento a depositantes e respectivos campos

### **3.3.2 Empréstimos**

|  |  |  |
| --- | --- | --- |
| **Dado** | **Campo** | **Esclarecimentos adicionais** |
| Identificação | Marca | Nome da marca reportada pelo participante do **Open Banking**. O conceito a que se refere a marca é, em essência, uma promessa das instituições em fornecer uma série específica de atributos, benefícios e serviços uniformes aos clientes. |
| Nome da instituição | Nome da instituição pertencente à marca |
| CNPJ da instituição |  |
| Campo adicional para URL (CNPJs) - se aplicável | URL de **link**, para lista complementar, com os nomes e CNPJs agrupados no caso de instituições oferecerem produtos e serviços com as mesmas características. |
| Modalidades | Conforme Circular nº 4.015, de 2020 e Anexo do Documento 3040 |
| Tarifas | Denominação das tarifas | Conforme regulamentação vigente |
| Siglas das tarifas | Conforme regulamentação vigente |
| Fatos geradores de cobrança | Conforme regulamentação vigente |
| Moeda | De acordo com o ISO 4217. |
| Valor | Distribuição de frequência relativa dos valores referentes às tarifas cobradas, nos termos da Resolução BCB nº 32, de 2020. |
| Taxas de juros remuneratórios | Referencial ou indexador | Tipos de taxas referenciais ou indexadores e percentuais adotados, conforme Anexo do Documento 3040. |
| Taxa pré-fixada contratada | Distribuição de frequência relativa da parcela prefixada dos juros cobrados na situação de adimplência, de acordo com a Resolução BCB nº 32, de 2020, e o Documento 3040. |
| Público-alvo | Lista de público-alvo | 1. Pessoa Natural, 2. Pessoa Jurídica, 3. Ambos |
| Tipos de garantia exigíveis | Lista de tipos de garantias | Conforme Anexo do Documento 3040 |
| Termos e condições contratuais | Termos e condições contratuais | Campo aberto (possibilidade de incluir URL) |

Tabela 3.3.2: Dados de empréstimos e respectivos campos

### **3.3.3 Direitos Creditórios Descontados**

|  |  |  |
| --- | --- | --- |
| **Dado** | **Campo** | **Esclarecimentos adicionais** |
| Identificação | Marca | Nome da marca reportada pelo participante do **Open Banking**. O conceito a que se refere a marca é, em essência, uma promessa das instituiçõesem fornecer uma série específica de atributos, benefícios e serviços uniformes aos clientes. |
| Nome da instituição | Nome da instituição, pertencente à marca, responsável pela comercialização das modalidades de direitos creditórios descontados. |
| CNPJ da instituição |  |
| Campo adicional para URL (CNPJs) - se aplicável | URL de **link**, para lista complementar, com os nomes e CNPJs agrupados no caso de instituições oferecerem produtos e serviços com as mesmas características. |
| Modalidades | Conforme Circular nº 4.015, de 2020 e Anexo do Documento 3040 |
| Tarifas | Denominação | Conforme regulamentação vigente |
| Siglas | Conforme regulamentação vigente |
| Fatos geradores de cobrança | Conforme regulamentação vigente |
| Moeda | De acordo com o ISO 4217. |
| Valor | Distribuição de frequência relativa dos valores referentes às tarifas cobradas, nos termos da Resolução BCB nº 32, de 2020. |
| Taxas de juros remuneratórios | Referencial ou indexador | Tipos de taxas referenciais ou indexadores e percentuais adotados, conforme Anexo do Documento 3040. |
| Taxa pré-fixada contratada | Distribuição de frequência relativa da parcela prefixada dos juros cobrados na situação de adimplência, de acordo com a Resolução BCB nº 32, de 2020, e o Documento 3040. |
| Público-alvo | Lista de público-alvo | 1. Pessoa Natural, 2. Pessoa Jurídica, 3. Ambos |
| Tipos de garantia exigíveis | Lista de tipos de garantias | Conforme Anexo do Documento 3040 |
| Termos e condições contratuais | Termos e condições contratuais | Campo aberto (possibilidade de incluir URL) |

Tabela 3.3.3: Dados de direitos creditórios descontados e respectivos campos

### **3.3.4 Financiamentos**

|  |  |  |
| --- | --- | --- |
| **Dado** | **Campo** | **Esclarecimentos adicionais** |
| Identificação | Marca | Nome da marca reportada pelo participante do **Open Banking**. |
| Nome da instituição | Nome da instituição, pertencente à marca reportada, responsável pela comercialização das modalidades de financiamentos. |
| CNPJ da instituição |  |
| Campo adicional para URL (CNPJs) - se aplicável | URL de **link**, para lista complementar, com os nomes e CNPJs agrupados no caso de instituições oferecerem produtos e serviços com as mesmas características. |
| Modalidades | Conforme Circular nº 4.015, de 2020 e Anexo do Documento 3040 |
| Tarifas | Denominação | Conforme regulamentação vigente |
| Siglas | Conforme regulamentação vigente |
| Fatos geradores de cobrança | Conforme regulamentação vigente |
| Moeda | De acordo com o ISO 4217. |
| Valor | Distribuição de frequência relativa dos valores referentes às tarifas cobradas, nos termos da Resolução BCB nº 32, de 2020. |
| Taxas de juros remuneratórios | Referencial ou indexador | Tipos de taxas referenciais ou indexadores e percentuais adotados, conforme Anexo do Documento 3040. |
| Taxa pré-fixada contratada | Distribuição de frequência relativa da parcela prefixada dos juros cobrados na situação de adimplência, de acordo com a Resolução BCB nº 32, de 2020, e o Documento 3040. |
| Público-alvo | Lista de público-alvo | 1. Pessoa Natural, 2. Pessoa Jurídica, 3. Ambos |
| Tipos de garantia exigíveis | Lista de tipos de garantias | Conforme Anexo do Documento 3040 |
| Termos e condições contratuais | Termos e condições contratuais | Campo aberto (possibilidade de incluir URL) |

Tabela 3.3.4: Dados de financiamentos e respectivos campos

# **4. Classificação dos Serviços e Dependências**

## 4.1         Tipos de dependências

A Resolução CMN nº 4.072, de 26 de abril de 2012, relaciona no art.1º os tipos de dependências permitidos para as instituições autorizadas a funcionar pelo Banco Central do Brasil:

I - Agência;

II - Posto de Atendimento (PA);

III - Posto de Atendimento Eletrônico (PAE); e

IV - Unidade Administrativa Desmembrada (UAD).

## 4.2         Tipos de serviços prestados por agências ou postos de atendimento

A relação de serviços prestados por agências ou postos de atendimento deve estar alinhada com a estabelecida pela regulamentação aplicável à sua divulgação na forma de dados abertos, discriminando, no mínimo, o seguinte:

I - abertura de contas de depósitos ou de pagamento pré-paga;

II - saque de moeda em espécie;

III - recebimentos, pagamentos de qualquer natureza;

IV- transferências eletrônicas visando à movimentação de contas de depósitos ou de pagamento de titularidade de clientes;

V - consulta a saldos e extratos de contas de depósitos e de contas de pagamento;

VI - aplicações e resgates de investimentos;

VII - execução ativa e passiva de ordens de pagamento por solicitação de clientes e usuários;

VIII - depósitos de moeda em espécie e de cheques;

IX - operações de crédito, bem como outros serviços prestados para o acompanhamento da operação;

X - cartão de crédito;

XI - seguros;

XII - operações de arrendamento mercantil;

XIII - abertura de conta de pagamento pós-paga;

XIV - compra e venda de moeda estrangeira em espécie;

XV - compra e venda de cheque ou cheque de viagem, bem como carga de moeda estrangeira em cartão pré-pago;

XVI - compra e venda de ouro; e

XVII - outros produtos ou serviços.

Atenção: Os códigos correspondentes aos serviços relacionados deverão ser padronizados para observância comum por todas as instituições participantes.

## 4.3         Tipos de serviços prestados por correspondentes no País

A Resolução CMN nº 3.954, de 24 de abril de 2012, relaciona em seu art. 8º as seguintes atividades de atendimento realizadas por correspondentes no País:

I - recepção e encaminhamento de propostas de abertura de contas de depósitos à vista, a prazo e de poupança mantidas pela instituição contratante;

II - realização de recebimentos, pagamentos e transferências eletrônicas visando à movimentação de contas de depósitos de titularidade de clientes mantidas pela instituição contratante;

III - recebimentos e pagamentos de qualquer natureza, e outras atividades decorrentes da execução de contratos e convênios de prestação de serviços mantidos pela instituição contratante com terceiros;

IV - execução ativa e passiva de ordens de pagamento cursadas por intermédio da instituição contratante por solicitação de clientes e usuários;

V - recepção e encaminhamento de propostas referentes a operações de crédito e de arrendamento mercantil de concessão da instituição contratante;

VI - recebimentos e pagamentos relacionados a letras de câmbio de aceite da instituição contratante;

VIII - recepção e encaminhamento de propostas de fornecimento de cartões de crédito de responsabilidade da instituição contratante; e

IX - realização de operações de câmbio de responsabilidade da instituição contratante.

Atenção: Os códigos correspondentes aos serviços relacionados deverão ser padronizados para observância comum por todas as instituições participantes.

Brasília, 29 de outubro de 2020.
