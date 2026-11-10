# /// script
# requires-python = ">=3.11"
# dependencies = ["beautifulsoup4>=4.12", "markdownify>=0.13"]
# ///
"""Testes do conversor do BCB. Rodar: uv run scripts/test_bcb.py"""
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import bcb  # noqa: E402

FIX = Path(__file__).parent / "fixtures"


class Basicos(unittest.TestCase):
    def test_tipo_do_titulo(self):
        self.assertEqual(bcb.tipo_do_titulo("Resolução CMN N° 4.966"), "Resolução CMN")
        self.assertEqual(bcb.tipo_do_titulo("Circular Nº 1"), "Circular")
        # 'Normativa' não pode ser confundido com 'No'
        self.assertEqual(bcb.tipo_do_titulo("Instrução Normativa BCB N° 12"), "Instrução Normativa BCB")
        self.assertEqual(bcb.tipo_do_titulo("COMUNICADO N. 002002"), "COMUNICADO")

    def test_tipo_api(self):
        self.assertEqual(bcb.tipo_api("COMUNICADO N. 002002", "Comunicado"), "Comunicado")
        self.assertEqual(bcb.tipo_api("Resolução BCB N° 366", "Resolução"), "Resolução BCB")
        self.assertEqual(bcb.tipo_api("Resolução Nº 1", "Resolução"), "Resolução")

    def test_campos_em_lista(self):
        self.assertEqual(bcb.vinculadas("CIRCULAR;@3913;@2018;#RESOLUÇÃO BCB;@594;@2026;#"),
                         ["CIRCULAR 3913/2018", "RESOLUÇÃO BCB 594/2026"])
        self.assertEqual(bcb.lista("a;#b;#"), ["a", "b"])

    def test_pdf(self):
        self.assertEqual(bcb.escolher_pdf("X_0001_v1_O.pdf;1#;X_0001_v2_L.pdf;2#;X_0001_v10_L.pdf;3#;"), "X_0001_v10_L.pdf")
        self.assertEqual(bcb.escolher_pdf("C_Circ_0073_v1_O.pdf;56#;"), "C_Circ_0073_v1_O.pdf")
        self.assertEqual(bcb.url_pdf("C_Circ_0073_v1_O.pdf", "1972"),
                         "https://www.bcb.gov.br/pre/normativos/c_circ/1972/pdf/c_circ_0073_v1_o.pdf")

    def test_serie_antiga_do_cmn_vai_junto_da_nova(self):
        self.assertEqual(bcb.pasta_do_tipo("Resolução"), bcb.pasta_do_tipo("Resolução CMN"))
        self.assertEqual(bcb.nome_arquivo("Resolução", "1"), "resolucao-cmn-0001.md")

    def test_ordem_comunicado_por_ultimo(self):
        l = [{"tipo": "Comunicado", "data": "1990"}, {"tipo": "Tipo Novo", "data": "1990"}, {"tipo": "Resolução CMN", "data": "2025"}]
        self.assertEqual([x["tipo"] for x in sorted(l, key=bcb.ordem)], ["Resolução CMN", "Tipo Novo", "Comunicado"])


class NormaReal(unittest.TestCase):
    def test_montar_resolucao_cmn(self):
        d = json.loads((FIX / "resolucao-cmn-4839.json").read_text(encoding="utf-8"))
        linha = {"titulo": "Resolução CMN N° 4.839", "tipo": "Resolução CMN", "numero": "4839", "data": "", "responsavel": "SECRE"}
        saida, md, versao = bcb.montar(linha, d, "2026-11-10")
        self.assertEqual(saida.relative_to(bcb.RAIZ).as_posix(), "resolucoes-cmn/2020/resolucao-cmn-4839.md")
        self.assertEqual(versao, "texto do portal do BCB")
        self.assertIn('orgao: "Conselho Monetário Nacional"', md)
        self.assertIn("data: 2020-07-30", md)
        self.assertIn("revogada: true", md)
        self.assertIn("RESOLUÇÃO CMN Nº 4.839", md)
        self.assertNotIn("&#58;", md)


if __name__ == "__main__":
    unittest.main()
