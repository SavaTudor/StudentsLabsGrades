import string
import random

from domeniu.entitateStudent import Student
from erori.exceptii import RepoError, ValidError


class ServiceStudent(object):
    def __init__(self, valid, repo):
        self.__valid = valid
        self.__repo = repo

    def adauga_student(self, id_stud, nume, grupa):
        """
        :param id_stud:id-ul unui nou student
        :param nume: numele unui nou student
        :param grupa: grupa unui nou student
        Ridica ValidError cu mesajul "id invalid!\n" sau "nume invalid!\n" sau "grupa invalida!\n" daca datele nu sunt corecte
        Ridica RepoError cu mesajul "elem existent!\n" daca student este deja in lista __elems
        Adauga pe Student in repo
        """
        student = Student(id_stud, nume, grupa)
        self.__valid.valideaza(student)
        self.__repo.adauga(student)

    def get_studenti(self):
        """
        :return: o copie a tuturor elementelor din repository de students
        """
        return self.__repo.get_all()

    def cauta_dupa_id(self, id_stud):
        """
        :param id_stud:id-ul studentului pe care il cautam
        :return: un element de clasa Student care are id-ul egal cu parametru dat
         Ridica RepoError cu mesajul "elem inexistent!\n" daca nu exista studentul cautat
        """
        return self.__repo.cauta_dupa_id(id_stud)

    def modifica(self, student_nou):
        """
        :param student_nou: noile date pentru studentul cu id-ul egal cu cel al studentului nou
        :return: -
        Ridica RepoError cu mesajul "elem inexistent!\n" daca id-ul lui student_nou nu exista in lista __elems
        Ridica ValidError student_nou nu ebine definit
        Modifica campurile nume si grupa ale studentului cu id-ul egal cu cele din student_nou
        """
        self.__valid.valideaza(student_nou)
        self.__repo.modifica(student_nou)

    def sterge_dupa_id(self, id_stud):
        """
        :param id: id-ul studentului care vrem sa il stergem
        :return: -
        Ridica RepoError cu mesajul "elem inexistent!\n" daca nu exista studentul cu id-ul dat in lista
        Sterge studentul cu id-ul dat din lista __elems
        """
        self.__repo.sterge_dupa_id(id_stud)

    def adauga_rand(self, nr):
        """
        def string_rand(lungime):
            litere = string.ascii_lowercase
            result_str = random.choice(litere).upper()
            for i in range(lungime - 1):
                result_str += random.choice(litere)
            return result_str
        """

        def string_rand_recursiv(lungime, poz, litere):
            """
            :param lungime: lungimea ceruta a stringului
            :param poz: pozitia pe care ne aflam in string
            :param litere: sirul de litere abcd...xyz
            :return: un string creat random de lungime data
            Creeaza un nume aleator pentru un student
            """
            if lungime == poz + 1:
                return ""
            else:
                if poz == 0:
                    return random.choice(litere).upper() + string_rand_recursiv(lungime, poz + 1, litere)
                else:
                    return random.choice(litere) + string_rand_recursiv(lungime, poz + 1, litere)

        k = 0
        while k < nr:
            id_stud = random.randint(1, 1000)
            nr_litere = random.randint(3, 15)
            """
            nume = string_rand(nr_litere)
            """
            litere = string.ascii_lowercase
            nume = ""
            nume = string_rand_recursiv(nr_litere, 0, litere)
            grupa = random.randint(1, 1000)
            student = Student(id_stud, nume, grupa)
            self.__valid.valideaza(student)
            try:
                self.__repo.adauga(student)

            except RepoError:
                k = k - 1
                continue

            k = k + 1
