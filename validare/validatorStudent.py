from erori.exceptii import ValidError


class ValidatorStudent(object):
    def valideaza(self, student):
        '''
        :param student: a Student object
        Raises ValidError with the message:
            "id invalid!\n", if the student's id is invalid
            "nume invalid!\n", if the student's name is invalid
            "grupa invalida!\n", if the student's group is invalid
        '''
        erori = ""
        if student.get_id() < 0 or student.get_id() != int(student.get_id()):
            erori += "id invalid!\n"
        if student.get_nume() == "":
            erori += "nume invalid!\n"
        grupa = student.get_grupa()
        if student.get_grupa() < 0 or student.get_grupa() != int(student.get_grupa()):
            erori += "grupa invalida!\n"
        if len(erori) > 0:
            raise ValidError(erori)
        else:
            return True
