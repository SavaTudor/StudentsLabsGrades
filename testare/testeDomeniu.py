import unittest

from domeniu.entitateCatalog import Note
from domeniu.entitateStudent import Student
from domeniu.entitateLab import Laborator


class TestCaseDomainStudent(unittest.TestCase):
    """
        clasa ce testeaza functionalitatile din clasa Student
    """

    def setUp(self):
        """
            codul executat inainte de fiecare test
        """
        self.st = Student(10, "Jon", 216)

    def testCreaza(self):
        """
            testarea functiei care creaza obiectul
        """
        self.assertTrue(self.st.get_id() == 10)
        self.assertTrue(self.st.get_nume() == "Jon")
        self.assertTrue(self.st.get_grupa() == 216)

    def testEgal(self):
        """
            testarea functiei de egal, ce suprascrie functia __eq__
        """
        alt_student = Student(10, "Alex", 220)
        self.assertTrue(self.st == alt_student)

    def testStr(self):
        """
            testarea functiei de string, ce suprascrie functia __str__
        """
        self.assertTrue(str(self.st) == "10 Jon 216")


class TestCaseDomainLab(unittest.TestCase):
    """
        clasa ce testeaza functionalitatile din clasa Laborator
    """

    def setUp(self):
        """
            codul executat inainte de fiecare test
        """
        self.lab = Laborator("2_2", "oop", "12.11.2020")

    def testCreaza(self):
        """
            testarea functiei care creaza obiectul
        """
        self.assertEqual(self.lab.get_nr(), "2_2")
        self.assertTrue(self.lab.get_descriere() == "oop")
        self.assertTrue(self.lab.get_deadline() == "12.11.2020")

    def testEgal(self):
        """
            testarea functiei de egal, ce suprascrie functia __eq__
        """
        alt_lab = Laborator("2_2", "fisiere", "25.12.2020")
        self.assertTrue(self.lab == alt_lab)

    def testStr(self):
        """
            testarea functiei de string, ce suprascrie functia __str__
        """
        self.assertTrue(str(self.lab) == "2_2 oop 12.11.2020")


class TestCaseDomainCatalog(unittest.TestCase):
    """
        clasa ce testeaza functionalitatile din clasa Note
    """

    def setUp(self):
        """
            codul executat inainte de fiecare test
        """
        self.st = Student(10, "Jon", 216)
        self.lab = Laborator("2_2", "oop", "12.11.2020")
        self.nota = Note(self.st, self.lab, 10)

    def testCreaza(self):
        """
            testarea functiei care creaza obiectul
        """
        self.assertEqual(self.nota.get_student().get_id(), 10)
        self.assertEqual(self.nota.get_student().get_nume(), "Jon")
        self.assertEqual(self.nota.get_student().get_grupa(), 216)
        self.assertTrue(self.nota.get_laborator().get_nr() == "2_2")
        self.assertTrue(self.nota.get_laborator().get_descriere() == "oop")
        self.assertTrue(self.nota.get_laborator().get_deadline() == "12.11.2020")

    def testEgal(self):
        """
            testarea functiei de egal, ce suprascrie functia __eq__
        """
        alta_nota = Note(self.st, self.lab, 8.75)
        self.assertTrue(self.nota == alta_nota)

    def testStr(self):
        """
            testarea functiei de string, ce suprascrie functia __str__
        """
        self.assertTrue(str(self.nota) == "10 2_2 10")
