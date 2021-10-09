from erori.exceptii import RepoError


class RepositoryLab(object):
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

    def adauga(self, lab):
        """
        :param lab:a Laborator object
        Raises RepoError with the message:
            "elem existent!\n" if the lab already exists in _elems
        Adds lab in _elems
        """
        if lab in self._elems:
            raise RepoError("elem existent!\n")
        self._elems.append(lab)

    def cauta_dupa_nr(self, nr):
        """
       :param nr: a laboratory's number
       :return: a Laboratory object with the number equal to the one given as parameter
       Raises RepoError with the message:
            "elem inexistent!\n" if a laboratory with the given number doesn't exist in _elems
       """
        for el in self._elems:
            if el.get_nr() == nr:
                return el
        raise RepoError("elem inexistent!\n")

    def modifica(self, lab_nou):
        """
        :param lab_nou: a Laboratory object
        Raises RepoError with the message:
            "elem inexistent!\n" if a laboratory with the id equal to lab_nou.id doesn't exist in _elems
        Modifies the labs attributes with the ones from lab_nou
        """
        if lab_nou not in self._elems:
            raise RepoError("elem inexistent!\n")
        for i in range(len(self._elems)):
            if self._elems[i] == lab_nou:
                self._elems[i] = lab_nou
                return

    def get_all(self):
        """
        :return: a copy of _elems
        """
        return self._elems[:]

    def sterge_dupa_nr(self, nr):
        """
        :param nr: the number of the lab we want to delete
        Raises RepoError with the message:
            "elem inexistent!\n" if a laboratory with the given number doesn't exist in _elems
        Deletes the lab with the given number from _elems
        """
        for i in range(len(self._elems)):
            if self._elems[i].get_nr() == nr:
                del self._elems[i]
                return
        raise RepoError("elem inexistent!\n")
