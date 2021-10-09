from domeniu.entitateStudent import Student
from erori.exceptii import RepoError
from infrastructura.reposStudent import RepositoryStudent


class RepositoryFileStudent(RepositoryStudent):
    def __init__(self, filename):
        RepositoryStudent.__init__(self)
        self.__fileName = filename

    def __incarca_din_fisier(self):
        """
        :return: o lista cu toti studentii din fisier
        """
        try:
            f = open(self.__fileName, "r")
        except IOError:
            return
        line = f.readline().strip()
        self._elems = []
        while line != "":
            entitate = line.split(";")
            st = Student(int(entitate[0]), entitate[1], int(entitate[2]))
            self._elems.append(st)
            line = f.readline().strip()
        f.close()

    def __append_in_fisier(self, student):
        """
        :return: -
        face append la fisierul self.__fileName
        """
        try:
            f = open(self.__fileName, "a")
        except IOError:
            return
        string = str(student.get_id()) + ";" + student.get_nume() + ";" + str(student.get_grupa()) + "\n"
        f.write(string)
        f.close()

    def __stocheaza_in_fisier(self):
        """
        :return: -
        functia stocheaza studentii din lista, cate unul pe linie, campurile fiind despartite de ;
        """
        f = open(self.__fileName, "w")
        for st in self._elems:
            string = str(st.get_id()) + ";" + st.get_nume() + ";" + str(st.get_grupa()) + "\n"
            f.write(string)
        f.close()

    def __len__(self):
        self.__incarca_din_fisier()
        return len(self._elems)

    def adauga(self, student):
        """
        :param student: un obiect student apartinand clasei Student
        :return: -
        Ridica RepoError cu mesajul "elem existent!\n" daca student este deja in lista __elems
        Adauga pe student in fisierul self.__fileName
        """
        self.__incarca_din_fisier()
        if student in self._elems:
            raise RepoError("elem existent!\n")
        self.__append_in_fisier(student)

    def cauta_dupa_id(self, id_stud):
        """
        :param id_stud: id-ul unui student
        :return: un element de clasa Student care are id-ul egal cu parametru dat
        Ridica RepoError cu mesajul "elem inexistent!\n"
        """
        self.__incarca_din_fisier()
        for el in self._elems:
            if int(el.get_id()) == int(id_stud):
                return el
        raise RepoError("elem inexistent!\n")

    def modifica(self, student_nou):
        """
        :param student_nou: un obiect apartinand clasei Student
        :return: -
        Ridica RepoError cu mesajul "elem inexistent!\n" daca id-ul lui student_nou nu exista in lista __elems
        Modifica campurile nume si grupa ale studentului cu id-ul egal cu cele din student_nou
        """
        self.__incarca_din_fisier()
        if student_nou not in self._elems:
            raise RepoError("elem inexistent!\n")
        for i in range(len(self._elems)):
            if self._elems[i] == student_nou:
                self._elems[i] = student_nou
                self.__stocheaza_in_fisier()
                return

    def get_all(self):
        """
        :return: o copie a tuturor elementelor din lista __elems
        """
        self.__incarca_din_fisier()
        return self._elems[:]

    def sterge_dupa_id(self, id_stud):
        """
        :param id_stud: id-ul studentului care vrem sa il stergem
        :return: -
        Ridica RepoError cu mesajul "elem inexistent!\n" daca nu exista studentul cu id-ul dat in lista
        Sterge studentul cu id-ul dat din fisier
        """
        self.__incarca_din_fisier()
        for i in range(len(self._elems)):
            if self._elems[i].get_id() == id_stud:
                del self._elems[i]
                self.__stocheaza_in_fisier()
                return
        raise RepoError("elem inexistent!\n")
