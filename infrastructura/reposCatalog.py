from erori.exceptii import RepoError


class RepositoryNote(object):
    def __init__(self):
        """
        Initializes _elems with an empty array
        """
        self._elems = []

    def __len__(self):
        """
        :return: _elems length
        """
        return len(self._elems)

    def adauga(self, nota):
        """
        :param nota: a Note object
        Raises RepoError if the given grade already exists in _elems
        Adds nota to _elems
        """
        if nota in self._elems:
            raise RepoError("elem existent!\n")
        self._elems.append(nota)

    def cauta_nota(self, student, lab):
        """
        :param student: the student's whose grade we are searching
        :param lab: the lab from where we want the grade
        :return: Nota object of the given student from the given lab
        Raises RepoError if the requested grade doesn't exist
        """
        for el in self._elems:
            if el.get_student() == student and el.get_laborator() == lab:
                return el
        raise RepoError("elem inexistent!\n")

    def modifica(self, nota_noua):
        """
        :param nota_noua: a Nota object
        Modifies the nota_noua.student's grade from the nota_noua.laboratory with nota_noua.grade
        Raises RepoError with the message:
            "elem inexistent!\n" if the given element doesn't exist
        """
        if nota_noua not in self._elems:
            raise RepoError("elem inexistent!\n")
        for i in range(len(self._elems)):
            if self._elems[i] == nota_noua:
                self._elems[i] = nota_noua
                return

    def get_all(self):
        """
        :return: a copy of _elems
        """
        return self._elems[:]

    def sterge_nota(self, student, lab):
        """
        :param student: the student from which we want to erase the grade
        :param lab: the lab from which we want to erase the grade
        Deletes from _elems the grade of the given student from the given lab
        Raises RepoError if there is no grade for the given student from the given lab
        """
        for i in range(len(self._elems)):
            if self._elems[i].get_student() == student and self._elems[i].get_laborator() == lab:
                del self._elems[i]
                return
        raise RepoError("elem inexistent!\n")
