import unittest

from auxiliar.cititor import Cititor


class TestCaseCititor(unittest.TestCase):
    def setUp(self):
        x = "3   Tudor 216;2_2 oop 12.12.2020 "
        self.cititor = Cititor(x)

    def testComanda(self):
        x = self.cititor.comanda()
        self.assertEqual(x, ["3   Tudor 216", "2_2 oop 12.12.2020 "])

    def testRun(self):
        x = self.cititor.comanda()
        elem = self.cititor.run(x[0])
        self.assertEqual(elem, ["3", "Tudor", "216"])

