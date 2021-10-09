from domeniu.entitateLab import Laborator


class ServiceLab(object):
    def __init__(self, valid, repo):
        self.__valid = valid
        self.__repo = repo

    def adauga_lab(self, nr, descriere, deadline):
        """
       :param lab: un obiect lab apartinand clasei Laborator
       Ridica RepoError cu mesajul "elem existent!\n" daca lab este deja in repository
       Adauga pe lab in repositoryLabs
       """
        lab = Laborator(nr, descriere, deadline)
        self.__valid.valideaza(lab)
        self.__repo.adauga(lab)

    def get_labs(self):
        """
      :return: o copie a tuturor elementelor din lista __elems
      """
        return self.__repo.get_all()

    def cauta_dupa_nr(self, nr):
        """
          :param nr: numarul unui laborator
          :return: un element de clasa Laborator care are numarul egal cu parametrul dat
          Ridica RepoError cu mesajul "elem inexistent!\n"
        """
        return self.__repo.cauta_dupa_nr(nr)

    def modifica(self, lab_nou):
        """
        :param lab_nou: un obiect apartinand clasei Laborator
        :return: -
        Ridica RepoError cu mesajul "elem inexistent!\n" daca numarul lui lab_nou nu exista in repository
        """
        self.__valid.valideaza(lab_nou)
        self.__repo.modifica(lab_nou)

    def sterge_dupa_nr(self, nr):
        """
        :param nr: nr-ul studentului care vrem sa il stergem
        :return: -
        Ridica RepoError cu mesajul "elem inexistent!\n" daca nu exista laboratorul cu numarul dat in repository
        Sterge laboratorul cu numarul dat din repository
        """
        self.__repo.sterge_dupa_nr(nr)