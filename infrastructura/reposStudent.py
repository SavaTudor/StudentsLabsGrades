from erori.exceptii import RepoError


class RepositoryStudent(object):
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

    def adauga(self, student):
        """
        :param student: a Student object
        Ridica RepoError cu mesajul "elem existent!\n" daca student este deja in lista __elems
        Raises RepoError with the message:
            "elem existent!\n" if the given student is already in _elems
        Adds student in _elems
        """
        if student in self._elems:
            raise RepoError("elem existent!\n")
        self._elems.append(student)

    def cauta_dupa_id(self, id_stud):
        """
        :param id_stud: id-ul unui student
        :return: un element de clasa Student care are id-ul egal cu parametru dat
        Ridica RepoError cu mesajul "elem inexistent!\n"
        """
        for el in self._elems:
            if el.get_id() == id_stud:
                return el
        raise RepoError("elem inexistent!\n")

    def modifica(self, student_nou):
        """
        :param student_nou: a Student object
        Raises RepoError with the message:
            "elem inexistent!\n" if the student's id doesn't exist in _elems
        Modifies the name and group attributes of the student with the id equal to student_nou.id to student_nou's attributes
        """
        if student_nou not in self._elems:
            raise RepoError("elem inexistent!\n")
        for i in range(len(self._elems)):
            if self._elems[i] == student_nou:
                self._elems[i] = student_nou
                return

    def get_all(self):
        """
        :return: a copy of all the elements in _elems
        """
        return self._elems[:]

    def sterge_dupa_id(self, id_stud):
        """
        :param id_stud: the id of the student that we want to delete
        Raises RepoError with the message:
            "elem inexistent!\n" if there is no student in _elems with the given id
        Deletes the student with the given id from _elems
        """
        for i in range(len(self._elems)):
            if self._elems[i].get_id() == id_stud:
                del self._elems[i]
                return
        raise RepoError("elem inexistent!\n")
