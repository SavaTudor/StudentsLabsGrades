from domeniu.entitateLab import Laborator
from erori.exceptii import RepoError
from infrastructura.reposLab import RepositoryLab


class RepositoryFileLab(RepositoryLab):
    def __init__(self, filename):
        RepositoryLab.__init__(self)
        self.__fileName = filename

    def __incarca_din_fisier(self):
        """
        :return: o lista cu toate laboratoerele din fisier
        """
        try:
            f = open(self.__fileName, "r")
        except IOError:
            return
        line = f.readline().strip()
        self._elems = []
        while line != "":
            entitate = line.split(";")
            lab = Laborator(entitate[0], entitate[1], entitate[2])
            self._elems.append(lab)
            line = f.readline().strip()
        f.close()

    def __append_in_fisier(self, lab):
        """
        :return: -
        face append la fisierul self.__fileName
        """
        try:
            f = open(self.__fileName, "a")
        except IOError:
            return
        string = lab.get_nr() + ";" + lab.get_descriere() + ";" + lab.get_deadline() + "\n"
        f.write(string)
        f.close()

    def __stocheaza_in_fisier(self):
        """
        :return: -
        functia stocheaza laboratoarele din lista, cate unul pe linie, campurile fiind despartite de ;
        """
        f = open(self.__fileName, "w")
        for lab in self._elems:
            string = lab.get_nr() + ";" + lab.get_descriere() + ";" + lab.get_deadline() + "\n"
            f.write(string)
        f.close()

    def __len__(self):
        self.__incarca_din_fisier()
        return len(self._elems)

    def adauga(self, lab):
        """
        :param lab: un obiect lab apartinand clasei Laborator
        Ridica RepoError cu mesajul "elem existent!\n" daca lab este deja in lista __elems
        Adauga pe lab in lista __Elems
        """
        self.__incarca_din_fisier()
        if lab in self._elems:
            raise RepoError("elem existent!\n")
        self.__append_in_fisier(lab)

    def cauta_dupa_nr(self, nr):
        """
       :param nr: numarul unui laborator
       :return: un element de clasa Laborator care are numarul egal cu parametru dat
       Ridica RepoError cu mesajul "elem inexistent!\n"
       """
        self.__incarca_din_fisier()
        for el in self._elems:
            if el.get_nr() == nr:
                return el
        raise RepoError("elem inexistent!\n")

    def modifica(self, lab_nou):
        """
        :param lab_nou: un obiect apartinand clasei Laborator
        :return: -
        Ridica RepoError cu mesajul "elem inexistent!\n" daca numarul lui lab_nou nu exista in lista __elems
        Modifica campurile descriere si deadline ale laboratorului cu numarul egal cu cele din lab_nou
        """
        self.__incarca_din_fisier()
        if lab_nou not in self._elems:
            raise RepoError("elem inexistent!\n")
        for i in range(len(self._elems)):
            if self._elems[i] == lab_nou:
                self._elems[i] = lab_nou
                self.__stocheaza_in_fisier()
                return

    def get_all(self):
        """
       :return: o copie a tuturor elementelor din fisier
       """
        self.__incarca_din_fisier()
        return self._elems[:]

    def sterge_dupa_nr(self, nr):
        """
        :param nr: nr-ul studentului care vrem sa il stergem
        :return: -
        Ridica RepoError cu mesajul "elem inexistent!\n" daca nu exista laboratorul cu numarul dat in lista
        Sterge laboratorul cu numarul dat din fisier
        """
        self.__incarca_din_fisier()
        for i in range(len(self._elems)):
            if self._elems[i].get_nr() == nr:
                del self._elems[i]
                self.__stocheaza_in_fisier()
                return
        raise RepoError("elem inexistent!\n")
