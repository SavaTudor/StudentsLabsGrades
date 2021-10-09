import unittest


class Student(object):
    def __init__(self, id_stud, nume, grupa):
        """
        :param id_stud: student's id (integer > 0)
        :param nume: student's name (a non-empty string)
        :param grupa: student's group (integer > 0)
        """
        self.__id = id_stud
        self.__nume = nume
        self.__grupa = grupa

    def get_id(self):
        return self.__id

    def get_nume(self):
        return self.__nume

    def get_grupa(self):
        return self.__grupa

    def __eq__(self, other):
        """
        :param other: another student
        :return: true, if the ids are equal; false otherwise
        """
        return self.__id == other.__id

    def __str__(self):
        """
        :return: a string with the format: id name group
        """
        return str(self.__id) + " " + self.__nume + " " + str(self.__grupa)
