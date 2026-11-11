---
titulo: "Comunicado N° 34.018"
orgao: "Banco Central do Brasil"
tipo: "Comunicado"
numero: "34018"
data: 2019-08-16
ementa: "Comunica às instituições financeiras autorizadas a funcionar pelo Banco Central do Brasil a possibilidade de validação por aplicativo de clientes dessas instituições para credenciamento no Extrato do Registro de Informações no Banco Central do Brasil (Sistema Registrato)."
revogada: false
responsavel: "DEATI"
versao_texto: "texto do portal do BCB"
fonte: "https://www.bcb.gov.br/estabilidadefinanceira/exibeoutrasnormas?tipo=Comunicado&numero=34018"
baixado_em: 2026-11-11
---
# Comunicado N° 34.018

Comunicamos que será implementada uma nova forma de autocredenciamento no Sistema Registrato, cuja forma de validação ocorrerá por meio de aplicativos das instituições financeiras autorizadas a funcionar pelo Banco Central do Brasil.

2.        O procedimento de autocredenciamento por aplicativo será facultativo e realizado em duas etapas, sendo a primeira no aplicativo da instituição financeira e a segunda na página do Banco Central na internet.

3.          Na primeira etapa, a instituição financeira deverá gerar um PIN de quatro números aleatórios (de 0000 até 9999) para o cliente logado no aplicativo da instituição a cada requisição utilizando o mesmo nível de segurança utilizado para uma transação bancária no APP (ex. senha, token).

4.          O PIN gerado deverá ser informado ao Banco Central por meio do Sistema de Mensageria ou do Webservice do STA. O Manual da Mensageria está disponível em https://www.bcb.gov.br/estabilidadefinanceira/comunicacaodados. O Manual do Webservice está em https://www.bcb.gov.br/acessoinformacao/sistematransferenciaarquivos. Os arquivos da mensageria utilizados pelo Registrato são AMES101 (Mensagem da instituição financeira enviada ao Banco Central) e AMES102 (Mensagem de confirmação do Banco Central recebida pela instituição financeira).

5.         O leiaute da mensageria não terá alteração em relação ao já utilizado no procedimento de validação via internet banking. As alterações ocorrerão no conteúdo da tag [TxtFraseSegrc], de acordo com uma das três opções a seguir:

Opção 1 – Direcionamento sem informações cadastrais:

[TxtFraseSegrc]V2NNNN[/TxtFraseSegrc]

             Onde V2 são caracteres fixos que significam procedimento de validação em
             duas etapas e NNNN é o número do PIN gerado aleatoriamente pela
             instituição financeira.

             Nessa opção, a instituição deverá direcionar o cliente para o endereço do
             Registrato (http://[endereço\_base\_registrato]/), onde o cidadão
             preencherá seus dados (número do CPF, nome da Instituição Financeira e
             PIN).

Opção 2 – Direcionamento com informações cadastrais:

             [TxtFraseSegrc]V2NNNNABCDEFGHIJKLMNOP[/TxtFraseSegrc]

             Onde V2 são caracteres fixos que significam procedimento de validação em
             duas etapas e NNNN é o número do PIN gerado aleatoriamente pela
             instituição financeira.

             ABCDEFGHIJKLMNOP é um número de controle aleatório de 16 posições (letras
             e números, desconsiderando maiúsculas e minúsculas). Esse número servirá
             para indicar que a instituição enviará os dados de CPF e nome da
             instituição para preenchimento automático.

             Nessa opção, a instituição deverá direcionar o cliente para o endereço do
             Registrato (http://[endereço\_base\_registrato]?controle=ABCDEFGHIJKLMNOP),
             onde as informações de CPF e Instituição Financeira já estarão
             preenchidas, bastando ao cidadão informar o PIN.

             Opção 3 – Direcionamento com informações cadastrais e PIN:

             [TxtFraseSegrc]V2NNNNABCDEFGHIJKLMNOP[/TxtFraseSegrc]

            Onde V2 são caracteres fixos que significam procedimento de validação em
            duas etapas e NNNN é o número do PIN gerado aleatoriamente pela
            instituição financeira.

            ABCDEFGHIJKLMNOP é um número de controle aleatório de 16 posições (letras
            e números, desconsiderando maiúsculas e minúsculas). Esse número servirá
            para indicar que a instituição enviará os dados de CPF e nome da
            instituição para preenchimento automático.

            Nessa opção, a instituição deverá direcionar o cliente para o endereço
            (http://[endereço\_base\_registrato]?controle=ABCDEFGHIJKLMNOP#NNNN), do
            Registrato, onde as informações de CPF, Instituição Financeira e PIN já
            estarão preenchidas.

6.          A tag [EndIPCli] da RGT0001, que corresponde ao endereço IP do cliente no padrão IPv4 ou IPv6, passará a ter tratamento adicional, de forma que endereços de rede privada serão devolvidos com erro RGT0001E (ex. loopback (127.0.0.1) ou faixas reservadas (10.0.0.0, 192.168.0.0, etc.)).

7.        A instituição financeira deverá informar o PIN gerado ao cliente na tela logada e direcioná-lo para o endereço do Registrato somente após a resposta RGT0001R1 (confirmação que o Banco Central recebeu o PIN).

8.          A validade o PIN será de cinco minutos contados a partir da confirmação.

9.          O PIN será informado ao cliente com a seguinte mensagem: “Utilize o PIN
NNNN para concluir seu cadastro no Registrato”.

10.         O CPF será “suspenso por 24 horas” após cinco tentativas com PIN ou CNPJ
da IF inválidos. Essa situação retornará a mensagem RGT0001E.

11.        Caso o cliente faça um segundo cadastro utilizando o mesmo CPF, Instituição Financeira e PIN, o login criado anteriormente será bloqueado no BCB. O cliente poderá desbloquear refazendo o processo.

12.       O novo procedimento de validação será implementado com base no seguinte cronograma:

Início da homologação – 21/10/2019;

Disponibilização em produção – 11/11/2019;

Divulgação – 11/12/2019.

13.        Eventuais dúvidas sobre a homologação serão dirimidas exclusivamente pelo e-mail registrato.deati@bcb.gov.br.

Brasília, 16 de agostto de 2019

Departamento de Atendimento Institucional
Carlos Eduardo Rodrigues da Cunha Gomes
Chefe de Unidade

Departamento de Tecnologia da Informação
Haroldo Jayme Martins Froes Cruz
Chefe de Unidade
