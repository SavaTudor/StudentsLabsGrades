class Note(object):
    def __init__(self, student, laborator, nota):
        """
        :param student: a Student object
        :param laborator: a Laborator object
        :param nota: an integer between 1 and 10, representing the grade
        """
        self.__nota = nota
        self.__laborator = laborator
        self.__student = student

    def get_student(self):
        return self.__student

    def get_laborator(self):
        return self.__laborator

    def get_nota(self):
        """
        the note is 0 if the student hasn't been graded yet
        """
        return self.__nota

    def __eq__(self, other):
        """
        :param other: another Note object
        :return:true if the student and laborator are equal between the two Notes, false otherwise
        """
        return self.__student == other.__student and self.__laborator == other.__laborator

    def __str__(self):
        """
        :return: a string with the format: student.id laborator.nrLab_nrProb grade
        """
        return str(self.__student.get_id()) + " " + self.__laborator.get_nr() + " " + str(self.__nota)
