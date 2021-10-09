from erori.exceptii import ValidError


class ValidatorLab(object):
    def __validator_numar(self, s):
        '''
        :param s: a string representing the lab number and the problem number
        :return: True if the string is valid, false otherwise
        s must be of the format "LabNumber_ProblemNumber"
        '''
        if len(s) < 3:
            return False
        x = s.find('_')
        if x == -1:
            return False
        c = ""
        for i in range(0, x):
            c = c + s[i]
        try:
            c = int(c)
            if c < 0:
                return False
        except ValueError:
            return False
        c = ""
        for i in range(x + 1, len(s)):
            c = c + s[i]
        try:
            c = int(c)
            if c < 0:
                return False
        except ValueError:
            return False
        return True

    def __validator_deadline(self, string):
        '''
        :param string: a string representing the laboratory's deadline
        :return: True if the string is valid, false otherwise
        string must be of the format "DD.MM.YYYY"
        '''
        if len(string) < 8:
            return False
        x = string.split('.')
        if len(x) != 3:
            return False
        for i in range(0, len(x)):
            try:
                x[i] = int(x[i])
            except ValueError:
                return False
        for i in range(0, 3):
            if i == 0:
                if x[i] < 0 or x[i] > 31:
                    return False
            if i == 1:
                if x[i] < 0 or x[i] > 12:
                    return False
            if i == 2:
                if x[i] < 2020:
                    return False
        return True

    def valideaza(self, lab):
        '''
        :param lab: a Laborator object
        Ridica ValidError cu mesajul "numar invalid!\n" sau "descriere invalida!\n" sau "deadline invalid!\n"
        Raises ValidError with the message:
            "numar invalid!\n" if the labNumber_problemNumber is invalid
            "descriere invalida!\n" if the description is an empty string
            "deadline invalid!\n" if the deadline is invalid
        '''
        erori = ""
        if not self.__validator_numar(lab.get_nr()):
            erori += "numar invalid!\n"
        if lab.get_descriere() == "":
            erori += "descriere invalida!\n"
        if not self.__validator_deadline(lab.get_deadline()):
            erori += "deadline invalid!\n"
        if len(erori) > 0:
            raise ValidError(erori)
        else:
            return True
