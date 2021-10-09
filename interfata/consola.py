from auxiliar.cititor import Cititor
from domeniu.entitateCatalog import Note
from domeniu.entitateStudent import Student
from domeniu.entitateLab import Laborator
from erori.exceptii import ValidError, RepoError
import random
import string


class UI(object):

    def __ui_print_menu(self):
        print("-------------------------")
        print("exit")
        print("add_student <id> <nume> <grupa>")
        print("cauta_student <id>")
        print("modifica_student <id> <nume nou> <grupa noua>")
        print("sterge_student <id>")
        print("print_students")
        print("add_lab <nrLab_nrProb> <descriere> <deadline>")
        print("cauta_lab <nrLab_nrProb>")
        print("modifica_lab <nrLab_nrProb> <descriere noua> <deadline nou>")
        print("sterge_lab <nrLab_nrProb>")
        print("print_labs")
        print("asign_lab <id student> <nrLab_nrProb>")
        print("print_note")
        print("cauta_nota <id student> <nrLab_nrProb>")
        print("notare_lab <id student> <nrLab_nrProb> <nota>")
        print("statistica_1 <nrLab_nrProb>")
        print("statistica_2 <nrLab_nrProb>")
        print("statistica_3")
        print("adauga_rand <nr studenti>")

    def __ui_adauga_student(self):
        if len(self.__x) != 4:
            print("comanda invalida!\n")
            return
        self.__srvS.adauga_student(int(self.__x[1]), self.__x[2], int(self.__x[3]))

    def __ui_print_students(self):
        studenti = self.__srvS.get_studenti()
        if len(studenti) == 0:
            print("nu exista studenti in lista!\n")
            return
        for student in studenti:
            print(student)

    def __ui_cauta_dupa_id(self):
        if len(self.__x) != 2:
            print("comanda invalida!\n")
            return
        gasit = self.__srvS.cauta_dupa_id(int(self.__x[1]))
        print(gasit)

    def __ui_modifica(self):
        if len(self.__x) != 4:
            print("comanda invalida!\n")
            return
        student = Student(int(self.__x[1]), self.__x[2], int(self.__x[3]))
        self.__srvS.modifica(student)

    def __ui_sterge_dupa_id(self):
        if len(self.__x) != 2:
            print("comanda invalida!\n")
            return
        note = self.__srvC.get_note()
        for nota in note:
            if nota.get_student().get_id() == int(self.__x[1]):
                self.__srvC.sterge_nota(nota.get_student().get_id(), nota.get_laborator().get_nr())
        self.__srvS.sterge_dupa_id(int(self.__x[1]))

    def __ui_adauga_lab(self):
        if len(self.__x) != 4:
            print("comanda invalida!\n")
            return
        self.__srvL.adauga_lab(self.__x[1], self.__x[2], self.__x[3])

    def __ui_cauta_dupa_nr(self):
        if len(self.__x) != 2:
            print("comanda invalida!\n")
            return
        gasit = self.__srvL.cauta_dupa_nr(self.__x[1])
        print(gasit)

    def __ui_modifica_lab(self):
        if len(self.__x) != 4:
            print("comanda invalida!\n")
            return
        lab = Laborator(self.__x[1], self.__x[2], self.__x[3])
        self.__srvL.modifica(lab)

    def __ui_sterge_dupa_nr(self):
        if len(self.__x) != 2:
            print("comanda invalida!\n")
            return
        note = self.__srvC.get_note()
        for nota in note:
            if nota.get_laborator().get_nr() == self.__x[1]:
                self.__srvC.sterge_nota(nota.get_student().get_id(), nota.get_laborator().get_nr())
        self.__srvL.sterge_dupa_nr(self.__x[1])

    def __ui_print_labs(self):
        labs = self.__srvL.get_labs()
        if len(labs) == 0:
            print("nu exista laboratoare in lista")
            return
        for lab in labs:
            print(lab)

    def __ui_asign_lab(self):
        if len(self.__x) != 3:
            print("comanda invalida!\n")
            return
        self.__srvC.asign_lab(int(self.__x[1]), self.__x[2])

    def __ui_print_note(self):
        note = self.__srvC.get_note()
        if len(note) == 0:
            print("nu exista note in lista!\n")
        for nota in note:
            print(nota)

    def __ui_cauta_nota(self):
        if len(self.__x) != 3:
            print("comanda invalida!\n")
            return
        gasit = self.__srvC.cauta_nota(int(self.__x[1]), self.__x[2])
        print(gasit)

    def __ui_notare_lab(self):
        if len(self.__x) != 4:
            print("comanda invalida!\n")
            return
        student = self.__srvS.cauta_dupa_id(int(self.__x[1]))
        lab = self.__srvL.cauta_dupa_nr(self.__x[2])
        nota_noua = Note(student, lab, float(self.__x[3]))
        self.__srvC.notare_lab(nota_noua)

    def __ui_stats_1(self):
        if len(self.__x) != 2:
            print("comanda invalida!\n")
            return
        lista = self.__srvC.stats1(self.__x[1])
        print(lista)

    def __ui_stats_2(self):
        if len(self.__x) != 2:
            print("comanda invalida!\n")
            return
        lista = self.__srvC.stats2(self.__x[1])
        print(lista)

    def __ui_stats_3(self):
        x = self.__srvC.stats3()
        if len(x) == 0:
            print("nu exista medii!\n")
            return
        print(x)

    def __ui_random_studenti(self):
        '''
            adauga un nr dat de studenti generati aleator
        '''
        if len(self.__x) != 2:
            print("comanda invalida!\n")
            return
        self.__srvS.adauga_rand(int(self.__x[1]))

    def __ui_raport(self):
        if len(self.__x) != 1:
            print("comanda invalida!\n")
            return
        lista = self.__srvC.stats4()
        print(lista)

    def __init__(self, srvS, srvL, srvC):
        self.__srvC = srvC
        self.__srvS = srvS
        self.__srvL = srvL
        self.__x = []
        self.__batch = []

        self.__comenzi = {
            'add_student': self.__ui_adauga_student,
            "cauta_student": self.__ui_cauta_dupa_id,
            "modifica_student": self.__ui_modifica,
            "sterge_student": self.__ui_sterge_dupa_id,
            "print_students": self.__ui_print_students,
            "add_lab": self.__ui_adauga_lab,
            "cauta_lab": self.__ui_cauta_dupa_nr,
            "modifica_lab": self.__ui_modifica_lab,
            "sterge_lab": self.__ui_sterge_dupa_nr,
            "print_labs": self.__ui_print_labs,
            "asign_lab": self.__ui_asign_lab,
            "print_note": self.__ui_print_note,
            "cauta_nota": self.__ui_cauta_nota,
            "notare_lab": self.__ui_notare_lab,
            "statistica_1": self.__ui_stats_1,
            "statistica_2": self.__ui_stats_2,
            "statistica_3": self.__ui_stats_3,
            "adauga_rand": self.__ui_random_studenti,
            "raport": self.__ui_raport
        }

    def run(self):
        self.__ui_print_menu()
        exit = 0
        while True:
            instruct = input(">>>")
            self.__cititor = Cititor(instruct)
            self.__batch = self.__cititor.comanda()
            for i in range(0, len(self.__batch)):
                self.__x = self.__cititor.run(self.__batch[i])
                if self.__x[0] == "exit":
                    print("Exiting")
                    exit = 1
                    break
                if self.__x[0] in self.__comenzi:
                    try:
                        self.__comenzi[self.__x[0]]()
                    except ValueError:
                        print("date invalide!\n")
                        print(self.__x[i])
                        break
                    except ValidError as ve:
                        print(ve)
                        break
                    except RepoError as re:
                        print(re)
                        break
                else:
                    print("comanda invalida!\n")
            if exit:
                break
