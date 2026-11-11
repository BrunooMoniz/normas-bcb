---
titulo: "COMUNICADO N. 008582"
orgao: "Banco Central do Brasil"
tipo: "Comunicado"
numero: "8582"
data: 2001-06-27
ementa: "Comunica mensagens para teste no Sistema de Pagamentos Brasileiro no período de 02 a 06.07.2001"
revogada: false
responsavel: "DEINF"
versao_texto: "texto do portal do BCB"
fonte: "https://www.bcb.gov.br/estabilidadefinanceira/exibeoutrasnormas?tipo=Comunicado&numero=8582"
baixado_em: 2026-11-11
---
# COMUNICADO N. 008582

```
                        COMUNICADO N. 008582
                        --------------------

                                     Comunica mensagens para teste no
                                     Sistema de Pagamentos Brasileiro
                                     no período de 02 a 06.07.2001

      O  Banco Central do Brasil,  em vista do que dispoe o artigo 3º
alínea "b", inciso IV, parágrafo 1º, da Circular 3032, de 11.05.2001,
comunica as mensagens do Sistema de Pagamentos Brasileiro que estarão
disponíveis para teste no período de 02 a 06.07.2001.

2.    Neste  período   poderão  ser   testadas   todas  as  mensagens
liberadas pelo SELIC desde o início dos testes, quais sejam:

      SEL1003      SEL1052      SEL1073
      SEL1013      SEL1066      SEL1074
      SEL1062      SEL3052      SEL1080

3.    Neste período as mensagens de Redesconto estarão sendo tratadas
pelo Selic, afetando, em consequência, a posição de custodia.Todavia,
a posição financeira ainda não será sensibilizada, ficando convencio-
nado o mesmo procedimento para verificação de saldo adotado para   as
mensagens SEL1052 e SEL1066:

      - operações de número par serão consideradas aceitas pelo STR;
      - operações de número ímpar serão consideradas rejeitadas por
        insuficiência de saldo.

  LDL - Câmaras LDL
   LDL0011 - IF requisita Transferência da Conta Corrente Câmara para
             Conta Liquidação
   LDL0012 - Câmara requisita Transferência da Conta de Liquidação da
             Câmara para sua Conta Corrente
   LDL0022 - IF requisita Transferência para Depósito Operacional

  RDC - Redesconto
   RDC0002 - IF requisita Redesconto Intradia
   RDC0007 - IF requisita Pagamento de Redesconto
   RDC0004 - IF requisita Redesconto Intradia Associado a uma
             Aquisição
   RDC0003 - IF requisita Redesconto Overnight
   RDC0008 - IF requisita pagamento de redesconto associado a venda
   RDC0005 - IF requisita conversão de redesconto intradia em over-
             night ou recontratação de overnight

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
             Titularidade
   STR0009 - IF requisita Transferência entre Contas de mesma
             Titularidade
   STR0011 - IF requisita Cancelamento de Lançamento Pendente
   STR0015 - STR avisa Fechamento
   STR0016 - STR avisa Saldo Fechamento
   STR0017 - STR avisa Abertura

  RCO - Sistema Controle de Compulsórios

   RCO0010- IF requisita Transferência Recursos de Compulsórios para
            conta Reservas Bancárias
   RCO0011 - IF requisita Transferência Recursos da conta Reservas
             Bancárias para Compulsórios
   RCO0018 - IF requisita cancelamento de Lançamento Bacen Pendente

  SLB - Sistema de Lançamentos do BC
   SLB0001 - SLB Informa Lançamento Devido pela IF
   SLB0002 - IF requisita Pagamento de Lançamento BACEN
   SLB0003 - SLB informa cancelamento lançamento BACEN
   SLB0004 - IF requisita cancelamento de lançamento SLB pendente
             no STR
   SLB0005 - SLB informa lançamento a crédito efetivado
   SLB0007 - IF requisita pagamento ao BACEN

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

Roberto Ozú                        Sérgio Goldenstein
Chefe do                           Chefe do Departamento de Operações
Departamento de Informática        do Mercado Aberto
```
