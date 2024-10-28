import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_alustaminen_negatiivisella_arvolla(self):
        self.varasto_neg = Varasto(-1, -1)
        self.assertAlmostEqual(self.varasto_neg.tilavuus, 0)
        self.assertAlmostEqual(self.varasto_neg.saldo, 0)

    def test_alkusaldo_tilavuutta_suurempi(self):
        self.varasto_suurempi_alkusaldo = Varasto(1, 2)
        self.assertAlmostEqual(self.varasto_suurempi_alkusaldo.tilavuus, 1)
        self.assertAlmostEqual(self.varasto_suurempi_alkusaldo.saldo, 1)

    def test_negatiivisen_luvun_lisays(self):
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_liian_suuren_lisays(self):
        self.varasto.lisaa_varastoon(20)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ota_negatiivinen(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-1), 0)

    def test_ota_maksimi(self):
        self.varasto_uusi = Varasto(10, 5)
        self.assertAlmostEqual(self.varasto_uusi.ota_varastosta(100), 5)

    def test_tulostus(self):
        self.varasto_tulostus = Varasto(5, 3)
        self.assertAlmostEqual(str(self.varasto_tulostus), f"saldo = {self.varasto_tulostus.saldo}, vielä tilaa {self.varasto_tulostus.paljonko_mahtuu()}")