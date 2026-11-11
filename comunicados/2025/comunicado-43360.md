---
titulo: "Comunicado N° 43.360"
orgao: "Banco Central do Brasil"
tipo: "Comunicado"
numero: "43360"
data: 2025-06-18
ementa: "Divulga os conjuntos de algoritmos e cifras (cipher suites) aceitos para conexões seguras (HTTPS / TLS) aos sistemas web do Banco Central disponíveis na Internet."
revogada: false
responsavel: "DEINF"
versao_texto: "texto do portal do BCB"
fonte: "https://www.bcb.gov.br/estabilidadefinanceira/exibeoutrasnormas?tipo=Comunicado&numero=43360"
baixado_em: 2026-11-11
---
# Comunicado N° 43.360

A partir de 06 de julho de 2025, às 08:00, o acesso aos sistemas web do Banco Central do Brasil pela internet que utilizam conexões seguras (HTTPS / TLS) precisarão utilizar um dos conjuntos de algoritmos e cifras (cipher suites) listados a seguir.

TLS\_AES\_256\_GCM\_SHA384 (apenas TLS 1.3)

TLS\_AES\_128\_GCM\_SHA256 (apenas TLS 1.3)

TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384

TLS\_ECDHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256

TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA384

TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA256

TLS\_DHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384

TLS\_DHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256

A utilização de configuração diferente das listadas acima acarretará falha no estabelecimento da conexão TLS (TLS Handshake failure).

2.     Os usuários de serviços web services devem verificar e providenciar os necessários ajustes, garantindo que os clientes utilizados sejam compatíveis com as cipher suites permitidas. Os ambientes de homologação dos respectivos sistemas possuem a mesma
configuração que será implantada em produção, podendo ser utilizados para testes.

3.          Os principais sistemas afetados serão:

             Sistema                 Endereço

             BCCorreio          https://bccorreio.bcb.gov.br/bccorreiows/

             PTAX               https://ptax.bcb.gov.br/wsmoeda/

             RDR                https://www3.bcb.gov.br/rdrws/

             SCR                https://scr.bcb.gov.br/wsscr2/

4.        Dúvidas sobre esta mudança poderão ser encaminhadas para a mesa de auxílio de TI, pelo telefone (61) 3414-2156 ou pelo endereço eletrônico suporte.ti@bcb.gov.br.

Caio Moreira Fernandes

Chefe do Departamento de Tecnologia da Informação
