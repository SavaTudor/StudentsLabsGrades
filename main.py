import unittest

from business.serviceCatalog import ServiceNote
from infrastructura.reposCatalog import RepositoryNote
from infrastructura.reposFileCatalog import RepositoryFileNote
from infrastructura.reposFileLab import RepositoryFileLab
from infrastructura.reposFileStudent import RepositoryFileStudent
from interfata.consola import UI
from validare.validareCatalog import ValidatorNote
from validare.validatorStudent import ValidatorStudent
from validare.validatorLab import ValidatorLab
from infrastructura.reposStudent import RepositoryStudent
from infrastructura.reposLab import RepositoryLab
from business.serviceStudent import ServiceStudent
from business.serviceLab import ServiceLab

print("selectati metoda de stocare")
n = input("fisier or local\n>>>")
if n == "fisier":
    filenameS = "repoS.txt"
    filenameL = "repoL.txt"
    filenameC = "repoC.txt"

    repoS = RepositoryFileStudent(filenameS)
    repoL = RepositoryFileLab(filenameL)
    repoC = RepositoryFileNote(filenameC, filenameS, filenameL)

else:
    repoS = RepositoryStudent()
    repoL = RepositoryLab()
    repoC = RepositoryNote()

validS = ValidatorStudent()
srvS = ServiceStudent(validS, repoS)
validL = ValidatorLab()
srvL = ServiceLab(validL, repoL)
validC = ValidatorNote()
srvC = ServiceNote(validC, repoC, repoL, repoS)
console = UI(srvS, srvL, srvC)

console.run()
