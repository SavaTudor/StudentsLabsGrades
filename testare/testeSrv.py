import unittest

from business.serviceCatalog import ServiceNote
from business.serviceStudent import ServiceStudent
from business.serviceLab import ServiceLab
from domeniu.entitateCatalog import Note
from domeniu.entitateStudent import Student
from domeniu.entitateLab import Laborator
from erori.exceptii import RepoError, ValidError
from infrastructura.reposCatalog import RepositoryNote
from infrastructura.reposStudent import RepositoryStudent
from infrastructura.reposLab import RepositoryLab
from validare.validareCatalog import ValidatorNote
from validare.validatorStudent import ValidatorStudent
from validare.validatorLab import ValidatorLab


class TestCaseSrvStudent(unittest.TestCase):
    """
        clasa care testeaza functionalitatile din ServiceStudent
    """

    def setUp(self):
        """
            codul care se executa inainte de fiecare test
        """
        self.valid = ValidatorStudent()
        self.repo = RepositoryStudent()
        self.srv = ServiceStudent(self.valid, self.repo)
        self.srv.adauga_student(1, "Tudor", 216)
        self.srv.adauga_student(2, "Cristi", 911)

    def testGet(self):
        """
            testeaza functionalitatea de get all
        """
        studenti = self.srv.get_studenti()
        self.assertEqual(len(studenti), 2)

    def testAdauga(self):
        """
            testeaza functionalitatea de adaugare
        """
        studenti = self.srv.get_studenti()
        self.assertEqual(studenti[0], Student(1, "Tudor", 216))
        self.assertTrue(studenti[1] == Student(2, "Cristi", 911))
        self.assertRaises(ValidError, self.srv.adauga_student, -1, "", -10)
        self.assertRaises(RepoError, self.srv.adauga_student, 1, "Ion", 221)
        self.srv.adauga_student(3, "Mircea", 313)
        studenti = self.srv.get_studenti()
        self.assertEqual(len(studenti), 3)

    def testCauta(self):
        """
            testeaza functionalitatea de cautare
        """
        gasit = self.srv.cauta_dupa_id(1)
        self.assertTrue(gasit.get_nume() == "Tudor")
        self.assertTrue(gasit.get_grupa() == 216)
        self.assertRaises(RepoError, self.srv.cauta_dupa_id, 10)

    def testModifica(self):
        self.srv.modifica(Student(2, "Radu", 414))
        gasit = self.srv.cauta_dupa_id(2)
        self.assertTrue(gasit.get_nume() == "Radu")
        self.assertTrue(gasit.get_grupa() == 414)
        self.assertRaises(ValidError, self.srv.modifica, Student(-1, "", -10))
        self.assertRaises(RepoError, self.srv.modifica, Student(10, "Luci", 217))

    def testSterge(self):
        """
            testeaza functionalitatea de stergere
        """
        studenti = self.srv.get_studenti()
        self.assertEqual(len(studenti), 2)
        self.srv.sterge_dupa_id(2)
        studenti = self.srv.get_studenti()
        self.assertEqual(len(studenti), 1)
        self.assertRaises(RepoError, self.srv.sterge_dupa_id, 100)

    def testAdaugaRand(self):
        studenti = self.srv.get_studenti()
        self.assertEqual(len(studenti), 2)
        self.srv.adauga_rand(3)
        studenti = self.srv.get_studenti()
        self.assertEqual(len(studenti), 5)


class TestCaseSrvLab(unittest.TestCase):
    """
        clasa care testeaza functionalitatile din ServiceLab
    """

    def setUp(self):
        """
           codul care se executa inainte de fiecare test
        """
        self.valid = ValidatorLab()
        self.repo = RepositoryLab()
        self.srv = ServiceLab(self.valid, self.repo)
        self.srv.adauga_lab("1_1", "oop", "12.12.2020")
        self.srv.adauga_lab("2_2", "test", "25.12.2020")

    def testGet(self):
        """
            testeaza functionalitatea de get all
        """
        labs = self.srv.get_labs()
        self.assertEqual(len(labs), 2)

    def testAdauga(self):
        """
            testeaza functionalitatea de adaugare
        """
        labs = self.srv.get_labs()
        self.assertEqual(labs[0], Laborator("1_1", "oop", "12.12.2020"))
        self.assertTrue(labs[1] == Laborator("2_2", "test", "25.12.2020"))
        self.assertRaises(ValidError, self.srv.adauga_lab, "asba", "", "123123421")
        self.assertRaises(RepoError, self.srv.adauga_lab, "1_1", "gui", "20.12.2020")
        self.srv.adauga_lab("3_3", "ceva", "31.12.2020")
        labs = self.srv.get_labs()
        self.assertEqual(len(labs), 3)

    def testCauta(self):
        """
            testeaza functionalitatea de cautare
        """
        gasit = self.srv.cauta_dupa_nr("1_1")
        self.assertEqual(gasit.get_descriere(), "oop")
        self.assertEqual(gasit.get_deadline(), "12.12.2020")
        self.assertRaises(RepoError, self.srv.cauta_dupa_nr, "10_10")

    def testModifica(self):
        """
            testeaza functionalitatea de modificare
        """
        self.srv.modifica(Laborator("1_1", "altceva", "27.12.2020"))
        gasit = self.srv.cauta_dupa_nr("1_1")
        self.assertTrue(gasit.get_descriere(), "altceva")
        self.assertTrue(gasit.get_deadline(), "27.12.2020")
        self.assertRaises(ValidError, self.srv.modifica, Laborator("asada", "", "21312"))
        self.assertRaises(RepoError, self.srv.modifica, Laborator("5_5", "ceva_nou", "1.1.2021"))

    def testSterge(self):
        """
            testeaza functionalitatea de stergere
        """
        labs = self.srv.get_labs()
        self.assertEqual(len(labs), 2)
        self.srv.sterge_dupa_nr("2_2")
        labs = self.srv.get_labs()
        self.assertEqual(len(labs), 1)
        self.assertRaises(RepoError, self.srv.sterge_dupa_nr, "5_5")


class TestCaseSrvNote(unittest.TestCase):
    """
        clasa care testeaza functionalitatile din ServiceNote
    """

    def setUp(self):
        """
            codul care se executa inainte de fiecare test
        """
        self.valid = ValidatorNote()
        self.repo = RepositoryNote()
        self.repoS = RepositoryStudent()
        self.repoL = RepositoryLab()
        self.srv = ServiceNote(self.valid, self.repo, self.repoL, self.repoS)
        self.student1 = Student(1, "Tudor", 216)
        self.repoS.adauga(self.student1)
        self.lab1 = Laborator("1_1", "oop", "12.12.2020")
        self.repoL.adauga(self.lab1)
        self.student2 = Student(2, "Dragos", 911)
        self.repoS.adauga(self.student2)
        self.lab2 = Laborator("2_2", "ceva", "31.12.2020")
        self.repoL.adauga(self.lab2)
        self.srv.asign_lab(1, "1_1")
        self.srv.asign_lab(2, "2_2")

    def testGet(self):
        """
            testeaza functionalitatea de get all
        """
        note = self.srv.get_note()
        self.assertEqual(len(note), 2)

    def testAsign(self):
        """
            testeaza functionalitatea de asignare
        """
        note = self.srv.get_note()
        self.assertTrue(note[0] == Note(self.student1, self.lab1, 0))
        self.assertTrue(note[1] == Note(self.student2, self.lab2, 0))
        self.assertRaises(RepoError, self.srv.asign_lab, 3, "3_3")
        self.srv.asign_lab(1, "2_2")
        note = self.srv.get_note()
        self.assertEqual(len(note), 3)

    def testCauta(self):
        """
            testeaza functionalitatea de cautare
        """
        gasit = self.srv.cauta_nota(1, "1_1")
        self.assertEqual(gasit.get_nota(), 0)
        self.assertRaises(RepoError, self.srv.cauta_nota, 3, "3_3")

    def testNotare(self):
        """
            testeaza functionalitatea de notare
        """
        self.srv.notare_lab(Note(self.student2, self.lab2, 9.5))
        gasit = self.srv.cauta_nota(self.student2.get_id(), self.lab2.get_nr())
        self.assertEqual(gasit.get_nota(), 9.5)
        self.assertRaises(ValidError, self.srv.notare_lab, Note(self.student2, self.lab2, -2))
        self.assertRaises(RepoError, self.srv.notare_lab, Note(self.student2, self.lab1, 9))

    def testSterge(self):
        """
            testeaza functionalitatea de stergere
        """
        note = self.srv.get_note()
        self.assertEqual(len(note), 2)
        self.srv.sterge_nota(1, "1_1")
        note = self.srv.get_note()
        self.assertEqual(len(note), 1)
        self.assertRaises(RepoError, self.srv.sterge_nota, 1, "2_2")

    def testGetStudentsLab(self):
        """
            testeaza functionalitatea de alfare a toti studentilor cu un lab dat
        """
        x = self.srv.get_studenti_lab("1_1")
        self.assertEqual(len(x), 1)
        self.assertEqual(x, [["Tudor", 0]])
        x = self.srv.get_studenti_lab("2_2")
        self.assertEqual(len(x), 1)
        self.assertEqual(x, [["Dragos", 0]])

    def testOrdonareAlfabetic(self):
        """
            testeaza ordonarea alfabetica in functie de primul parametru a unei liste de liste
        """
        x = [["Tudor", 10], ["Dragos", 9.5], ["alex", 9.75]]
        x = self.srv.ordonare_alfabetic(x, 0)
        self.assertEqual(x, [["alex", 9.75], ["Dragos", 9.5], ["Tudor", 10]])

    def testOrdonareNota(self):
        """
             testeaza ordonarea crescatoare dupa nota in functie de al doilea parametru a unei liste de liste
        """
        x = [["Tudor", 10], ["Dragos", 9.5], ["alex", 9.75]]
        x = self.srv.ordonare_nota(x, 1)
        self.assertEqual(x, [["Dragos", 9.5], ["alex", 9.75], ["Tudor", 10]])

    def testStats1(self):
        """
            testeaza creearea raportului de lista de studenti si nota lor la un lab dat
            ordonati alfabetic
        """
        self.repoS.adauga(Student(3, "alex", 219))
        self.srv.asign_lab(3, "1_1")
        self.srv.asign_lab(2, "1_1")
        x = self.srv.stats1("1_1")
        self.assertEqual(x, [["alex", 0], ["Dragos", 0], ["Tudor", 0]])
        self.assertRaises(RepoError, self.srv.stats1, "3_3")

    def testStats2(self):
        """
            testeaza crearea raportului de lista de studenti si nota lor la un lab dat
            ordonati dupa nota
        """
        self.repoS.adauga(Student(3, "alex", 219))
        self.srv.asign_lab(2, "1_1")
        self.srv.asign_lab(3, "1_1")
        self.srv.notare_lab(Note(self.student1, self.lab1, 9))
        self.srv.notare_lab(Note(self.student2, self.lab1, 9.5))
        self.srv.notare_lab(Note(Student(3, "alex", 219), self.lab1, 9.75))
        x = self.srv.stats2("1_1")
        self.assertEqual(x, [["Tudor", 9], ["Dragos", 9.5], ["alex", 9.75]])
        self.assertRaises(RepoError, self.srv.stats2, "3_3")

    def testMedii(self):
        """
            testarea functiei care calculeaza mediile pentru fiecare student
        """
        self.srv.asign_lab(2, "1_1")
        self.srv.asign_lab(1, "2_2")
        self.srv.notare_lab(Note(self.student1, self.lab1, 9.5))
        self.srv.notare_lab(Note(self.student1, self.lab2, 10))
        self.srv.notare_lab(Note(self.student2, self.lab2, 8))
        self.srv.notare_lab(Note(self.student2, self.lab1, 9))
        x = self.srv.medii()
        self.assertEqual(x, [[1, 9.75], [2, 8.5]])

    def testStats3(self):
        """
            testeaza crearea raportului cu studentii care au media la laboratoare mai mica decat 5
        """
        self.srv.asign_lab(2, "1_1")
        self.srv.asign_lab(1, "2_2")
        self.srv.notare_lab(Note(self.student1, self.lab1, 4))
        self.srv.notare_lab(Note(self.student1, self.lab2, 3.5))
        self.srv.notare_lab(Note(self.student2, self.lab2, 8))
        self.srv.notare_lab(Note(self.student2, self.lab1, 9))
        x = self.srv.stats3()
        self.assertEqual(x, [["Tudor", 3.75]])

    def testStats4(self):
        """
            testeaza crearea raportului cu primii 5 studenti cu cele mai multe laboratoare
        """
        self.student3 = Student(3, "Mircea", 313)
        self.repoS.adauga(self.student3)
        self.student4 = Student(4, "Ionut", 212)
        self.repoS.adauga(self.student4)
        self.student5 = Student(5, "Matei", 818)
        self.repoS.adauga(self.student5)
        self.student6 = Student(6, "Chivu", 419)
        self.repoS.adauga(self.student6)
        # avem 1 1_1 si 2 2_2
        self.srv.asign_lab(1, "2_2")
        self.srv.asign_lab(2, "1_1")
        self.srv.asign_lab(3, "1_1")
        self.srv.asign_lab(3, "2_2")
        self.srv.asign_lab(4, "1_1")
        self.srv.asign_lab(4, "2_2")
        self.srv.asign_lab(5, "1_1")
        self.srv.asign_lab(5, "2_2")
        self.srv.asign_lab(6, "1_1")
        x = self.srv.stats4()
        self.assertEqual(x, [["Dragos"], ["Ionut"], ["Matei"], ["Mircea"], ["Tudor"]])
