import unittest

from domeniu.entitateCatalog import Note
from domeniu.entitateStudent import Student
from domeniu.entitateLab import Laborator
from erori.exceptii import RepoError
from infrastructura.reposCatalog import RepositoryNote
from infrastructura.reposStudent import RepositoryStudent
from infrastructura.reposLab import RepositoryLab


class TestCaseRepoStudent(unittest.TestCase):
    """
        clasa testeaza functionalitatile din RepositoryStudent
    """

    def setUp(self):
        """
            codul executat inainte de fiecare functie test
        """
        self.repo = RepositoryStudent()
        self.student1 = Student(10, "Jon", 216)
        self.student1_id = Student(10, "Tudor", 220)
        self.student2 = Student(20, "Mihai", 911)
        self.repo.adauga(self.student1)
        self.repo.adauga(self.student2)

    def testAdauga(self):
        """
            testarea functionalitatii de adaugare
        """
        self.assertEqual(len(self.repo), 2)
        self.assertRaises(RepoError, self.repo.adauga, self.student1_id)

    def testCauta(self):
        """
            testarea functionalitatii de cautare
        """
        gasit = self.repo.cauta_dupa_id(10)
        self.assertTrue(gasit.get_nume() == "Jon")
        self.assertEqual(gasit.get_grupa(), 216)
        self.assertRaises(RepoError, self.repo.cauta_dupa_id, 25)

    def testModifica(self):
        """
            testarea functionalitatii de modificare
        """
        self.assertTrue(self.student1 == self.student1_id)
        self.repo.modifica(self.student1_id)
        gasit = self.repo.cauta_dupa_id(self.student1_id.get_id())
        self.assertEqual(gasit.get_nume(), "Tudor")
        self.assertEqual(gasit.get_grupa(), 220)
        self.assertRaises(RepoError, self.repo.modifica, Student(50, "Kiko", 313))

    def testGet(self):
        """
            testarea functionalitatii de get all
        """
        all = self.repo.get_all()
        self.assertEqual(len(all), 2)
        self.assertEqual(all[0], self.student1_id)
        self.assertEqual(all[1], self.student2)

    def testSterge(self):
        """
            testarea functionalitatii de stergere
        """
        self.assertEqual(len(self.repo), 2)
        self.repo.sterge_dupa_id(20)
        self.assertEqual(len(self.repo), 1)
        self.assertRaises(RepoError, self.repo.sterge_dupa_id, 50)


class TestCaseRepoLab(unittest.TestCase):
    """
        clasa testeaza functionalitatile din RepositoryLab
    """

    def setUp(self):
        """
            codul executat inainte de fiecare functie test
        """
        self.repo = RepositoryLab()
        self.lab1 = Laborator("1_1", "oop", "12.12.2020")
        self.lab1_id = Laborator("1_1", "teste", "20.12.2020")
        self.lab2 = Laborator("2_2", "exam", "17.12.2020")
        self.repo.adauga(self.lab1)
        self.repo.adauga(self.lab2)

    def testAdauga(self):
        """
            testeaza functionalitatea de adaugare
        """
        self.assertEqual(len(self.repo), 2)
        self.assertRaises(RepoError, self.repo.adauga, self.lab1_id)

    def testCauta(self):
        """
            testeaza functionalitatea de cautare
        """
        gasit = self.repo.cauta_dupa_nr("1_1")
        self.assertTrue(gasit.get_descriere() == "oop")
        self.assertEqual(gasit.get_deadline(), "12.12.2020")
        self.assertRaises(RepoError, self.repo.cauta_dupa_nr, "3_3")

    def testModifica(self):
        """
            testeaza functionalitatea de modificare
        """
        self.assertTrue(self.lab1 == self.lab1_id)
        self.repo.modifica(self.lab1_id)
        gasit = self.repo.cauta_dupa_nr(self.lab1_id.get_nr())
        self.assertEqual(gasit.get_descriere(), "teste")
        self.assertEqual(gasit.get_deadline(), "20.12.2020")
        self.assertRaises(RepoError, self.repo.modifica, Laborator("5_5", "inex", "1.1.2021"))

    def testGet(self):
        """
            testeaza functionalitatea de get all
        """
        all = self.repo.get_all()
        self.assertEqual(len(all), 2)
        self.assertEqual(all[0], self.lab1_id)
        self.assertEqual(all[1], self.lab2)

    def testSterge(self):
        """
            testeaza functionalitatea de stergere
        """
        self.assertEqual(len(self.repo), 2)
        self.repo.sterge_dupa_nr("1_1")
        self.assertEqual(len(self.repo), 1)
        self.assertRaises(RepoError, self.repo.sterge_dupa_nr, "5_5")


class TestCaseRepoNote(unittest.TestCase):
    """
        clasa testeaza functionalitatile din RepositoryLab
    """

    def setUp(self):
        """
            codul executat inainte de fiecare test
        """
        self.repo = RepositoryNote()
        self.lab1 = Laborator("1_1", "oop", "12.12.2020")
        self.st1 = Student(1, "Tudor", 216)
        self.calif = 10
        self.nota1 = Note(self.st1, self.lab1, self.calif)
        self.nota1_id = Note(self.st1, self.lab1, self.calif - 1.5)
        self.lab2 = Laborator("2_2", "ceva", "25.12.2020")
        self.st2 = Student(2, "Alex", 911)
        self.nota2 = Note(self.st2, self.lab2, self.calif - 3)
        self.repo.adauga(self.nota1)
        self.repo.adauga(self.nota2)

    def testAdauga(self):
        """
            testarea functionalitatii de adaugare
        """
        self.assertEqual(len(self.repo), 2)
        self.assertRaises(RepoError, self.repo.adauga, self.nota1_id)

    def testCauta(self):
        """
            testarea functionalitatii de cautare
        """
        gasit = self.repo.cauta_nota(self.st1, self.lab1)
        self.assertTrue(gasit.get_nota() == self.calif)
        self.assertRaises(RepoError, self.repo.cauta_nota, Student(3, "john", 212),
                          Laborator(3_3, "test", "29.12.2020"))

    def testModifica(self):
        """
            testarea functionalitatii de modificare
        """
        self.assertTrue(self.nota1 == self.nota1_id)
        self.repo.modifica(self.nota1_id)
        gasit = self.repo.cauta_nota(self.nota1_id.get_student(), self.nota1_id.get_laborator())
        self.assertEqual(gasit.get_nota(), self.calif - 1.5)
        self.assertRaises(RepoError, self.repo.modifica,
                          Note(Student(3, "john", 212), Laborator("5_5", "inex", "1.1.2021"), 7.5))

    def testGet(self):
        """
            testarea functionalitatii de get all
        """
        all = self.repo.get_all()
        self.assertEqual(len(all), 2)
        self.assertEqual(all[0], self.nota1_id)
        self.assertEqual(all[1], self.nota2)

    def testSterge(self):
        """
            testarea functionalitatii de stergere
        """
        self.assertEqual(len(self.repo), 2)
        self.repo.sterge_nota(self.st2, self.lab2)
        self.assertEqual(len(self.repo), 1)
        self.assertRaises(RepoError, self.repo.sterge_nota, self.st1, self.lab2)
