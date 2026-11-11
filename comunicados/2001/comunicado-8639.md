---
titulo: "COMUNICADO N. 008639"
orgao: "Banco Central do Brasil"
tipo: "Comunicado"
numero: "8639"
data: 2001-07-12
ementa: "Comunica mensagens para teste no Sistema de Pagamentos Brasileiro no período de 16 a 20.07.2001"
revogada: false
responsavel: "DEINF"
versao_texto: "texto do portal do BCB"
fonte: "https://www.bcb.gov.br/estabilidadefinanceira/exibeoutrasnormas?tipo=Comunicado&numero=8639"
baixado_em: 2026-11-11
---
# COMUNICADO N. 008639

```
                        COMUNICADO N. 008639
                        --------------------

                                     Comunica mensagens para teste no
                                     Sistema de Pagamentos Brasileiro
                                     no período de 16 a 20.07.2001

      O  Banco Central do Brasil,  em vista do que dispoe o artigo 3º
alínea "b", inciso IV, parágrafo 1º, da Circular 3032, de 11.05.2001,
comunica as mensagens do Sistema de Pagamentos Brasileiro que estarão
disponíveis para teste no período de 16 a 20.07.2001.

  SELIC

    SEL1007 - Liquidação de Leilão
    SEL1056 - Retorno de Compromissada - 1 ou mais dias

    a) Ofertas Públicas (fictícias) a liquidar em 04.06.2001:

        Título        Vencimento    Tipo              Aviso(fictício)
        100000        04/07/2002    01-Primário-Venda    Com.9001
        100000        03/07/2002    02-Secundário-Venda  Com.9003
        100000        04/07/2002    03-Secundário-Compra Com.9002

        Obs.: Os arquivos dos avisos estarão disponíveis no "site" do
              Selic (www.demab.rtm)

    b) Data de referência para data do movimento, posição de custódia
       e preço de lastro: 04.06.2001

    A  partir  deste  período  as  mensagens que cursarem pelo Selic,
    envolvendo a conta Reserva Bancária,  já estarão sensibilizando a
    posição financeira das instituições (STR).

  LDL - Câmaras LDL
   LDL0011 - IF requisita Transferência da Conta Corrente Câmara para
             Conta Liquidação
   LDL0012 - Câmara requisita Transferência da Conta de Liquidação da
             Câmara para sua Conta Corrente
   LDL0022 - IF requisita Transferência para Depósito Operacional
   LDL0016 - Câmara consulta lançamento
   LDL0017 - Câmara consulta Saldo Conta Liquidação

  RDC - Redesconto
   RDC0002 - IF requisita Redesconto Intradia
   RDC0007 - IF requisita Pagamento de Redesconto
   RDC0004 - IF requisita Redesconto Intradia Associado a uma
             Aquisição
   RDC0003 - IF requisita Redesconto Overnight
   RDC0008 - IF requisita pagamento de redesconto associado a venda
   RDC0005 - IF requisita conversão de redesconto intradia em over-
             night ou recontratação de overnight
   RDC0001 - IF consulta Títulos Redescontáveis
   RDC0006 - IF consulta Redescontos
   RDC0010 - Redesconto avisa Arquivo Títulos Redescontáveis
             Disponível
  STR - Sistema de Transferência de Reservas
   STR0003 - IF requisita Liquidação de Transferência de Numerário
   STR0004 - IF requisita Transferência de Reservas
   STR0010 - IF requisita Transferência para Devolução de
             Transferencias Indevidas
   STR0013 - IF consulta Saldo Reserva Bancária
   STR0005 - IF requisita Transferência entre não Correntistas
   STR0006 - IF requisita Transferência de Conta Cliente para IF
   STR0007 - IF requisita Transferência da IF para Conta Cliente
   STR0008 - IF requisita Transferência entre Contas de diferentes
             Titularidades
   STR0009 - IF requisita Transferência entre Contas de mesma
             Titularidade
   STR0011 - IF requisita Cancelamento de Lançamento Pendente
   STR0015 - STR avisa Fechamento
   STR0016 - STR avisa Saldo Fechamento
   STR0017 - STR avisa Abertura
   STR0001 - IF consulta Horários do STR
   STR0012 - IF consulta Lançamentos

  RCO - Sistema Controle de Compulsórios

   RCO0010- IF requisita Transferência Recursos de Compulsórios para
            conta Reservas Bancárias
   RCO0011 - IF requisita Transferência Recursos da conta Reservas
             Bancárias para Compulsórios
   RCO0018 - IF requisita cancelamento de Lançamento Bacen Pendente
   RCO0005 - IF consulta Estrato Movimentação
   RCO0001 - IF consulta Períodos de Depósitos Compulsórios

  SLB - Sistema de Lançamentos do BC
   SLB0001 - SLB Informa Lançamento Devido pela IF
   SLB0002 - IF requisita Pagamento de Lançamento BACEN
   SLB0003 - SLB informa cancelamento lançamento BACEN
   SLB0004 - IF requisita cancelamento de lançamento SLB pendente
             no STR
   SLB0005 - SLB informa lançamento a crédito efetivado
   SLB0007 - IF requisita pagamento ao BACEN
   SLB0006 - IF consulta Lançamentos SLB

  STN - Sistema de Lançamentos do Tesouro Nacional
   STN0001 - IF requisita Transferência de Reserva para a Conta
             Única
   STN0004 - TN requisita Transferência de recursos da Conta Única
             para Reservas

   STN0008 - IF Requisita Cancelamento de Transferencia Pendente
   STN0013 - TN Requisita Dedução Integral
   STN0015 - TN Requisita Transferencia de Recursos da Conta Única
             para Conta Corrente
   STN0016 - IF Requisita Devolução de Recursos de Conta Corrente
             para Conta Única
   STN0002 - IF Requisita Transferência Recolhimento de Receitas
             Federais
   STN0003 - IF Requisita Dedução de Recolhimento a Maior
   STN0006 - IF Requisita Transferência de Encargos por Atraso
             Recolhimento de Receitas Federais
   STN0007 - IF Requisita Transferência Lançamento Financeiro INSS
   STN0009 - STN informa Dedução Efetivada
   STN0011 - IF consulta Recolhimentos Efetuados em uma Data
   STN0012 - IF consulta Lançamentos Financeiros INSS Efetuados
             em uma Data

Reinaldo Doná Sol                  Sérgio Goldenstein
Chefe do Departamento de           Chefe do Departamento de Operações
Informática, em exercício          do Mercado Aberto
```
