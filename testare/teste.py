from testare.testeCititor import TestCaseCititor
from testare.testeRepoFile import TestCaseRepoFileStudent, TestCaseRepoFileLab, TestCaseRepoFileNote
from testare.testeDomeniu import *
from testare.testeRepo import *
from testare.testeSrv import *
from testare.testeValidator import *


class Tests():
    def __init__(self):
        self.TesteDomainStudent = TestCaseDomainStudent()
        self.TesteDomainLaborator = TestCaseDomainLab()
        self.TesteDomainNote = TestCaseDomainCatalog()
        self.TesteValidatorStudent = TestCaseValidatorStudent()
        self.TesteValidatorLab = TestCaseValidatorLaborator()
        self.TesteValidatorNota = TestCaseValidatorNota()
        self.TesteRepoStudent = TestCaseRepoStudent()
        self.TesteRepoLab = TestCaseRepoLab()
        self.TesteRepoNote = TestCaseRepoNote()
        self.TesteSrvStudent = TestCaseSrvStudent()
        self.TesteSrvLab = TestCaseSrvLab()
        self.TesteSrvNote = TestCaseSrvNote()
        self.TesteRepoFileStudent = TestCaseRepoFileStudent()
        self.TesteRepoFileLab = TestCaseRepoFileLab()
        self.TesteRepoFileNote = TestCaseRepoFileNote()
        self.TesteCititor = TestCaseCititor()


unittest.main()
