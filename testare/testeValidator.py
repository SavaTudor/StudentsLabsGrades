from domeniu.entitateCatalog import Note
from domeniu.entitateStudent import Student
from domeniu.entitateLab import Laborator
from erori.exceptii import ValidError
from validare.validareCatalog import ValidatorNote
from validare.validatorStudent import ValidatorStudent
from validare.validatorLab import ValidatorLab
import unittest


class TestCaseValidatorStudent(unittest.TestCase):
    # BlackBox
    """
        clasa care testeaza  functionalitatile din clasa ValidatorStudent
    """
    def setUp(self):
        """
            codul executat inainte de fiecare test
        """
        self.valid = ValidatorStudent()
        self.st_rau1 = Student(-30, "Tudor", 215)
        self.st_rau2 = Student(1, "", 235)
        self.st_rau3 = Student(3, "Tudor", 23.5)
        self.st_rau4 = Student(-30, "", 215)
        self.st_rau5 = Student(30, "", 23.5)
        self.st_rau6 = Student(-30, "Tudor", 23.5)
        self.st_rau7 = Student(-30, "", 23.5)
        self.st_bun = Student(1, "Tudor", 216)

    def testValidator(self):
        """
            testarea funcitei valideaza din cadrul clasei ValidatorStudent, folosind metoda blacbox
        """
        self.assertRaises(ValidError, self.valid.valideaza, self.st_rau1)
        self.assertRaises(ValidError, self.valid.valideaza, self.st_rau2)
        self.assertRaises(ValidError, self.valid.valideaza, self.st_rau3)
        self.assertRaises(ValidError, self.valid.valideaza, self.st_rau4)
        self.assertRaises(ValidError, self.valid.valideaza, self.st_rau5)
        self.assertRaises(ValidError, self.valid.valideaza, self.st_rau6)
        self.assertRaises(ValidError, self.valid.valideaza, self.st_rau7)
        self.assertTrue(self.valid.valideaza(self.st_bun))


class TestCaseValidatorLaborator(unittest.TestCase):
    """
        clasa care testeaza  functionalitatile din clasa ValidatorLaborator
    """
    # BlackBox
    def setUp(self):
        """
            codul executat inainte de fiecare testi
        """
        self.valid = ValidatorLab()
        self.lab_rau1 = Laborator("ab", "oop", "1.12.2020")
        self.lab_rau2 = Laborator("1_1", "", "12.12.2020")
        self.lab_rau3 = Laborator("1_1", "test", "asd.12.2020")
        self.lab_rau4 = Laborator("a_1", "", "12.12.2020")
        self.lab_rau5 = Laborator("1_1", "", "45.12.2020")
        self.lab_rau6 = Laborator("-1_1", "oop", "20.-2.2020")
        self.lab_rau7 = Laborator("1_-2", "", "20.12.2010")
        self.lab_rau8 = Laborator("1_a", "", "20.12.2010")
        self.lab_bun = Laborator("1_1", "oop", "25.12.2020")

    def testValidator(self):
        """
            testarea functiei valideaza din ValidatorLaborator cu metoda blackbox
        """
        self.assertRaises(ValidError, self.valid.valideaza, self.lab_rau1)
        self.assertRaises(ValidError, self.valid.valideaza, self.lab_rau2)
        self.assertRaises(ValidError, self.valid.valideaza, self.lab_rau3)
        self.assertRaises(ValidError, self.valid.valideaza, self.lab_rau4)
        self.assertRaises(ValidError, self.valid.valideaza, self.lab_rau5)
        self.assertRaises(ValidError, self.valid.valideaza, self.lab_rau6)
        self.assertRaises(ValidError, self.valid.valideaza, self.lab_rau7)
        self.assertRaises(ValidError, self.valid.valideaza, self.lab_rau8a)
        self.assertTrue(self.valid.valideaza(self.lab_bun))


class TestCaseValidatorNota(unittest.TestCase):
    """
        clasa care testeaza functionalitatile din clasa ValidatorNota
    """
    #BlackBox
    def setUp(self):
        """
            codul executat inainte de test
        """
        self.valid = ValidatorNote()
        self.st = Student(10, "Tudor", 216)
        self.lab = Laborator("2_2", "oop", "12.12.2020")
        self.nota_rea = Note(self.st, self.lab, -2)
        self.nota_buna = Note(self.st, self.lab, 10)

    def testValidator(self):
        """
            testarea functiei valideaza din cadrul clasei ValidatorNota, cu metoda blackbox
        """
        self.assertRaises(ValidError, self.valid.valideaza, self.nota_rea)
        self.assertTrue(self.valid.valideaza(self.nota_buna))
