from erori.exceptii import ValidError
from validare.validatorLab import ValidatorLab
from validare.validatorStudent import ValidatorStudent


class ValidatorNote(object):
    def valideaza(self, nota):
        '''
        :param nota: a Note object
        Raises ValidError if the student is not well defined, if the laboratory is not well defined or if the grade is not well defined
        '''
        validatorStudent = ValidatorStudent()
        validatorLab = ValidatorLab()
        erori = ""
        validatorStudent.valideaza(nota.get_student())
        validatorLab.valideaza(nota.get_laborator())
        if nota.get_nota() != float(nota.get_nota()) or (nota.get_nota() < 0 or nota.get_nota() > 10):
            erori += "nota invalida!\n"
        if len(erori) > 0:
            raise ValidError(erori)
        else:
            return True
