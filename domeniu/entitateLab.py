class Laborator(object):
    def __init__(self, nrLab_nrProb, descriere, deadline):
        """
        :param nrLab_nrProb: a string with the format "labNumber_problemNumber"
        :param descriere: a non-empty string
        :param deadline: a string with the format "DD.MM.YYYY"
        """
        self.__nr = nrLab_nrProb
        self.__descriere = descriere
        self.__deadline = deadline

    def get_nr(self):
        return self.__nr

    def get_descriere(self):
        return self.__descriere

    def get_deadline(self):
        return self.__deadline

    def __eq__(self, other):
        """
        :param other: another Laborator object
        :return: true if the lab number and problem number are equal; false otherwise
        """
        return self.__nr == other.__nr

    def __str__(self):
        """
        :return: a string with the format "nrLab_nrProb description deadline"
        """
        return self.__nr + " " + self.__descriere + " " + self.__deadline
