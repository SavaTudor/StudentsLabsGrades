import unittest

from domeniu.entitateCatalog import Note
from domeniu.entitateStudent import Student
from domeniu.entitateLab import Laborator
from erori.exceptii import RepoError
from infrastructura.reposFileCatalog import RepositoryFileNote
from infrastructura.reposFileLab import RepositoryFileLab
from infrastructura.reposFileStudent import RepositoryFileStudent


class TestCaseRepoFileStudent(unittest.TestCase):
    '''
        clasa testeaza functionalitatile din clasa RepositoryFileStudent
    '''
    def setUp(self):
        '''
        codul executat inainte de fiecare functie test
        '''
        with open("/Users/savatudor/Desktop/FP/lab_7_9/testare/testeRepoStudent.txt", "w") as f:
            f.write("")
        self.repo = RepositoryFileStudent("/Users/savatudor/Desktop/FP/lab_7_9/testare/testeRepoStudent.txt")
        self.assertEqual(len(self.repo), 0)
        self.student1 = Student(1, "Tudor", 216)
        self.student2 = Student(2, "Alex", 911)
        self.student3 = Student(3, "Dragos", 313)
        self.repo.adauga(self.student1)
        self.assertEqual(len(self.repo), 1)

    def testAdauga(self):
        '''
        testarea functionalitatii de adaugare
        '''
        self.repo.adauga(self.student2)
        self.assertEqual(len(self.repo), 2)
        self.assertRaises(RepoError, self.repo.adauga, self.student1)

    def testCauta(self):
        '''
               testarea functionalitatii de cautare
        '''
        gasit = self.repo.cauta_dupa_id(1)
        self.assertTrue(gasit.get_nume() == "Tudor")
        self.assertEqual(gasit.get_grupa(), 216)
        self.assertRaises(RepoError, self.repo.cauta_dupa_id, 5)

    def testModifica(self):
        '''
               testarea functionalitatii de modificare
        '''
        student2_id = Student(1, "Mircea", 1001)
        self.repo.modifica(student2_id)
        gasit = self.repo.cauta_dupa_id(1)
        self.assertEqual(gasit.get_nume(), "Mircea")
        self.assertEqual(gasit.get_grupa(), 1001)
        self.assertRaises(RepoError, self.repo.modifica, Student(10, "Luca", 818))

    def testGet(self):
        '''
            testarea functionalitatii de get all
        '''
        all = self.repo.get_all()
        self.assertEqual(len(all), 1)
        self.assertEqual(all[0].get_nume(), "Tudor")
        self.assertEqual(all[0].get_id(), 1)
        self.assertEqual(all[0].get_grupa(), 216)
        self.repo.adauga(self.student2)
        all = self.repo.get_all()
        self.assertEqual(len(all), 2)

    def testSterge(self):
        '''
            testarea functionalitatii de stergere
        '''
        self.repo.adauga(self.student2)
        self.assertEqual(len(self.repo), 2)
        self.repo.sterge_dupa_id(2)
        self.assertEqual(len(self.repo), 1)
        self.assertRaises(RepoError, self.repo.sterge_dupa_id, 2)


class TestCaseRepoFileLab(unittest.TestCase):
    '''
        clasa testeaza functionalitatile din clasa RepositoryFileLab
    '''
    def setUp(self):
        '''
            codul executat inainte de fiecare functie test
        '''
        with open("/Users/savatudor/Desktop/FP/lab_7_9/testare/testeRepoLab.txt", "w") as f:
            f.write("")
        self.repo = RepositoryFileLab("/Users/savatudor/Desktop/FP/lab_7_9/testare/testeRepoLab.txt")
        self.assertEqual(len(self.repo), 0)
        self.lab1 = Laborator("1_1", "oop", "12.12.2020")
        self.lab2 = Laborator("2_2", "teste", "15.12.2020")
        self.repo.adauga(self.lab1)
        self.assertEqual(len(self.repo), 1)

    def testAdauga(self):
        '''
            testarea functionalitatii de adaugare
        '''
        self.repo.adauga(self.lab2)
        self.assertTrue(len(self.repo) == 2)
        self.assertRaises(RepoError, self.repo.adauga, self.lab1)

    def testCauta(self):
        '''
            testarea functionalitatii de cautare
        '''
        gasit = self.repo.cauta_dupa_nr("1_1")
        self.assertEqual(gasit.get_descriere(), "oop")
        self.assertEqual(gasit.get_deadline(), "12.12.2020")
        self.assertRaises(RepoError, self.repo.cauta_dupa_nr, "3_3")

    def testModifica(self):
        '''
            testarea functionalitatii de modifica
        '''
        lab1_id = Laborator("1_1", "altceva", "30.12.2020")
        self.repo.modifica(lab1_id)
        gasit = self.repo.cauta_dupa_nr("1_1")
        self.assertEqual(gasit.get_descriere(), "altceva")
        self.assertEqual(gasit.get_deadline(), "30.12.2020")
        self.assertRaises(RepoError, self.repo.modifica, Laborator("3_3", "gata", "31.12.2020"))

    def testGet(self):
        '''
            testarea functionalitatii de get all
        '''
        all = self.repo.get_all()
        self.assertEqual(len(all), 1)
        self.assertTrue(all[0].get_nr() == "1_1")
        self.assertTrue(all[0].get_descriere() == "oop")
        self.assertTrue(all[0].get_deadline() == "12.12.2020")
        self.repo.adauga(self.lab2)
        all = self.repo.get_all()
        self.assertEqual(len(all), 2)

    def testSterge(self):
        '''
            testarea functionalitatii de modifica
        '''
        self.repo.adauga(self.lab2)
        self.assertEqual(len(self.repo), 2)
        self.repo.sterge_dupa_nr("2_2")
        self.assertEqual(len(self.repo), 1)
        self.assertRaises(RepoError, self.repo.sterge_dupa_nr, "2_2")


class TestCaseRepoFileNote(unittest.TestCase):
    '''
       clasa testeaza functionalitatile din clasa RepositoryFileNote
    '''
    def setUp(self):
        '''
            codul executat inainte de fiecare functie test
        '''
        '''
        filenameS = "/Users/savatudor/Desktop/FP/lab_7_9/testare/testeRepoStudent.txt"
        filenameL = "/Users/savatudor/Desktop/FP/lab_7_9/testare/testeRepoLab.txt"
        filenameC = "/Users/savatudor/Desktop/FP/lab_7_9/testare/testeRepoNote.txt"
        '''
        filenameS = "testeRepoStudent.txt"
        filenameL = "testeRepoLab.txt"
        filenameC = "testeRepoNote.txt"
        with open(filenameS, "w") as f:
            f.write("")
        self.repoS = RepositoryFileStudent(filenameS)
        with open(filenameL, "w") as f:
            f.write("")
        self.repoL = RepositoryFileLab(filenameL)
        with open(filenameC, "w") as f:
            f.write("")
        self.repo = RepositoryFileNote(filenameC, filenameS, filenameL)
        self.assertEqual(len(self.repo), 0)
        self.student1 = Student(1, "Tudor", 216)
        self.student2 = Student(2, "Alex", 911)
        self.repoS.adauga(self.student1)
        self.repoS.adauga(self.student2)
        self.lab1 = Laborator("1_1", "oop", "12.12.2020")
        self.lab2 = Laborator("2_2", "altceva", "31.12.2020")
        self.repoL.adauga(self.lab1)
        self.repoL.adauga(self.lab2)
        self.nota1 = Note(self.student1, self.lab1, 9.5)
        self.nota2 = Note(self.student2, self.lab1, 8)
        self.repo.adauga(self.nota1)
        self.assertTrue(len(self.repo) == 1)

    def testAdauga(self):
        '''
           testarea functionalitatii de adaugare
        '''
        self.repo.adauga(self.nota2)
        self.assertEqual(len(self.repo), 2)
        self.assertRaises(RepoError, self.repo.adauga, self.nota1)

    def testCauta(self):
        '''
           testarea functionalitatii de cautare
        '''
        gasit = self.repo.cauta_nota(self.student1, self.lab1)
        self.assertEqual(gasit.get_nota(), 9.5)
        self.assertRaises(RepoError, self.repo.cauta_nota, self.student1, self.lab2)

    def testModifica(self):
        '''
            testarea functionalitatii de modificare
        '''
        nota1_id = Note(self.student1, self.lab1, 8.25)
        self.repo.modifica(nota1_id)
        gasit = self.repo.cauta_nota(self.student1, self.lab1)
        self.assertEqual(gasit.get_nota(), 8.25)
        self.assertRaises(RepoError, self.repo.modifica, Note(self.student2, self.lab2, 6))

    def testGet(self):
        '''
               testarea functionalitatii de get all
        '''
        all = self.repo.get_all()
        self.assertEqual(len(all), 1)
        self.assertEqual(all[0].get_student(), self.student1)
        self.assertEqual(all[0].get_laborator(), self.lab1)

    def testSterge(self):
        '''
            testarea functionalitatii de stergere
        '''
        self.repo.adauga(self.nota2)
        self.assertEqual(len(self.repo), 2)
        self.repo.sterge_nota(self.student2, self.lab1)
        self.assertEqual(len(self.repo), 1)
        self.assertRaises(RepoError, self.repo.sterge_nota, self.student2, self.lab1)