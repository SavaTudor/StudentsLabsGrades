from domeniu.entitateCatalog import Note
from erori.exceptii import RepoError
from infrastructura.reposCatalog import RepositoryNote
from infrastructura.reposFileLab import RepositoryFileLab
from infrastructura.reposFileStudent import RepositoryFileStudent


class RepositoryFileNote(RepositoryNote):
    def __init__(self, filename, filenameS, filenameL):
        RepositoryNote.__init__(self)
        self.__fileName = filename
        self.__repoS = RepositoryFileStudent(filenameS)
        self.__repoL = RepositoryFileLab(filenameL)

    def __incarca_din_fisier(self):
        """
        :return: o lista cu toate notele din fisier
        """
        try:
            f = open(self.__fileName, "r")
        except IOError:
            return
        line = f.readline().strip()
        self._elems = []
        while line != "":
            entitate = line.split(";")
            student = self.__repoS.cauta_dupa_id(entitate[0])
            lab = self.__repoL.cauta_dupa_nr(entitate[1])
            nota = Note(student, lab, float(entitate[2]))
            self._elems.append(nota)
            line = f.readline().strip()
        f.close()

    def __append_in_fisier(self, nota):
        """
        :return: -
        face append la fisierul self.__fileName
        """
        try:
            f = open(self.__fileName, "a")
        except IOError:
            return
        string = str(nota.get_student().get_id()) + ";" + nota.get_laborator().get_nr() + ";" + str(
            nota.get_nota()) + "\n"
        f.write(string)
        f.close()

    def __stocheaza_in_fisier(self):
        """
        :return: -
        functia stocheaza laboratoarele din lista, cate unul pe linie, campurile fiind despartite de ;
        """
        f = open(self.__fileName, "w")
        for nota in self._elems:
            string = str(nota.get_student().get_id()) + ";" + nota.get_laborator().get_nr() + ";" + str(
                nota.get_nota()) + "\n"
            f.write(string)
        f.close()

    def __len__(self):
        self.__incarca_din_fisier()
        return len(self._elems)

    def adauga(self, nota):
        """
        :param nota: un obiect nota apartinand clasei Note
        Ridica RepoError cu mesajul "elem existent!\n" daca lab este deja in fisier
        Adauga pe nota in fisier
        """
        self.__incarca_din_fisier()
        if nota in self._elems:
            raise RepoError("elem existent!\n")
        self.__append_in_fisier(nota)

    def cauta_nota(self, student, lab):
        """
        :param student: studentul caruia ii cautam nota
        :param lab: laboratorul de la care cautam nota
        :return: elementul de tipul Nota corespunzator
        Ridica RepoError daca elementul cautat nu exista
        """
        self.__incarca_din_fisier()
        for el in self._elems:
            if el.get_student() == student and el.get_laborator() == lab:
                return el
        raise RepoError("elem inexistent!\n")

    def modifica(self, nota_noua):
        """
        :param nota_noua: un obiect de tipul Nota care contine nota cea noua, urmand sa o inlocuiasca la student si lab
        :return: -
        Modifica nota studentului la lab din obiect cu nota nou data
        Ridica RepoError daca elementul nu exista in lista
        """
        self.__incarca_din_fisier()
        if nota_noua not in self._elems:
            raise RepoError("elem inexistent!\n")
        for i in range(len(self._elems)):
            if self._elems[i] == nota_noua:
                self._elems[i] = nota_noua
                self.__stocheaza_in_fisier()
                return

    def get_all(self):
        """
       :return: o copie a tuturor elementelor din fisier
       """
        self.__incarca_din_fisier()
        return self._elems[:]

    def sterge_nota(self, student, lab):
        """
       :param student: studentul caruia vrem sa ii stergem nota
       :param lab: laboratorul de la care ii stergem nota
       :return: -
       Functia sterge din fisier nota aferenta studentului si laboratorului dat
       Ridica RepoError daca elementul nu exista in lista
       """

        self.__incarca_din_fisier()
        for i in range(len(self._elems)):
            if self._elems[i].get_student() == student and self._elems[i].get_laborator() == lab:
                del self._elems[i]
                self.__stocheaza_in_fisier()
                return
        raise RepoError("elem inexistent!\n")
