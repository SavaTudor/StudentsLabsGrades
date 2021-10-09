from domeniu.entitateCatalog import Note
from sortari.sort import insertionSort, combSort


class ServiceNote(object):
    def __init__(self, valid, repo, repoLab, repoStud):
        self.__repoL = repoLab
        self.__repoS = repoStud
        self.__repo = repo
        self.__valid = valid

    def asign_lab(self, id_stud, nrlab_nrprob):
        """
        :param id_stud: id-ul studentului caruia ii asignam un laborator
        :param nrlab_nrprob: numarul laboratorului pe care il asignam
        :return:
        adauga in repository o noua nota corespunzatoare studentului caruia ii atribuim laboratorul,
        ce laborator ii atribuim si cu nota data
        Ridica RepoError cu mesajul "elem inexitsten!\n" daca student nu e in repositoryStudent sau daca
        lab nu este in repositoryLab sau studentul dat are deja asignat laboratorul dat
        Ridica ValidError daca nota nu e buna
        """
        student = self.__repoS.cauta_dupa_id(id_stud)
        lab = self.__repoL.cauta_dupa_nr(nrlab_nrprob)
        nota = Note(student, lab, 0)
        self.__valid.valideaza(nota)
        self.__repo.adauga(nota)

    def get_note(self):
        """
        :return: lista tuturor notelor date
        """
        return self.__repo.get_all()

    def cauta_nota(self, id_stud, nrlab_nrprob):
        """
        :param id_stud: studentul caruia ii cautam nota
        :param nrlab_nrprob: problema la care ii cautam nota studentului
        :return: nota studentului
        Ridica RepoError daca studentul nu e in repoStudent sau daca lab nu e in repoLab sau daca nota nu e in repoNota
        """
        student = self.__repoS.cauta_dupa_id(id_stud)
        lab = self.__repoL.cauta_dupa_nr(nrlab_nrprob)
        return self.__repo.cauta_nota(student, lab)

    def notare_lab(self, nota_noua):
        """
        :param nota_noua: nota noua care vrem sa o acordam studentului dat, pe problema data
        :return: -
        Ridica ValidError daca nota nu e bine definita
        Ridica RepoError daca unul dintre elemente nu se afla in repository
        Modifica nota din elems a elementului ce are studentul si laboratorul identic cu cele date
        """
        self.__valid.valideaza(nota_noua)
        self.__repo.modifica(nota_noua)

    def sterge_nota(self, id_stud, nrlab_nrprob):
        """
        :param id_stud: id_ul studentului caruia vrem sa ii stergem o nota
        :param nrlab_nrprob: laboratorul la care ii stergem nota
        :return: -
        Ridica RepoError cu mesajul "elem inexistent!\n"
        sterge din elems nota studentului dat la laboratorul dat
        """
        student = self.__repoS.cauta_dupa_id(id_stud)
        lab = self.__repoL.cauta_dupa_nr(nrlab_nrprob)
        self.__repo.sterge_nota(student, lab)

    def get_studenti_lab(self, nrlab_nrprob):
        """
        :param nrlab_nrprob: numarul laboratorului de la care vrem sa aflam studentii
        :return: o lista de liste cu id-ul si nota unui student la un laborator dat
        Ridica RepoError daca laborator nu e in repository
        """
        x = []
        elems = self.get_note()
        for i in elems:
            if i.get_laborator().get_nr() == nrlab_nrprob:
                elem_nou = [i.get_student().get_nume(), i.get_nota()]
                x.append(elem_nou)
        return x

    def get_studenti_lab_recursiv(self, nrlab_nrprob, elems, x):
        """
        :nrlab_nrprob: numarul laboratorului de la care vrem sa aflam studentii
        :elems: lista de note/asignari de laboratoare
        :x:lista in care se vor afla studentii care au un lab dat
        Ridica RepoError daca laborator nu e in repository
        """
        if len(elems) == 0:
            return
        if elems[0].get_laborator().get_nr() == nrlab_nrprob:
            elem_nou = [elems[0].get_student().get_nume(), elems[0].get_nota()]
            x.append(elem_nou)
        del elems[0]
        self.get_studenti_lab_recursiv(nrlab_nrprob, elems, x)

    def ordonare_alfabetic(self, x, key):
        """
        :param x: o lista de liste
        :return: lista x ordonata alfabetic in functie de primul element din liste
        """
        """
        for i in range(len(x) - 1):
            for j in range(i + 1, len(x)):
                s1 = x[i][0].upper()
                s2 = x[j][0].upper()
                if s1 > s2:
                    aux = x[i]
                    x[i] = x[j]
                    x[j] = aux
        return x
        
        
        def key(elem):
            return elem[0]
        """

        def cmp(x, y):
            """
            :param x, y: elementele pe care le comparam
            :return: daca x < y, returneaza True, altfel False
            prima data compara x[0] cu y[0], iar daca sunt egale, face comparatia intre x[1] si y[1]
            """
            if x[0] == y[0]:
                if x[1] > y[1]:
                    return True
                else:
                    return False
            else:
                if x[0] < y[0]:
                    return True
                else:
                    return False

        insertionSort(x, lambda x: x, cmp)
        return x

    def ordonare_nota(self, x, key):
        """
        :param x: o lista de liste
        :return: lista x ordonata crescator in functie de al doilea elem din liste
        """
        """
        for i in range(len(x) - 1):
            for j in range(i + 1, len(x)):
                if x[i][1] > x[j][1]:
                    aux = x[i]
                    x[i] = x[j]
                    x[j] = aux
        return x
        """

        combSort(x, lambda x: x[1], lambda x, y: x > y)
        return x

    def stats1(self, nrlab_nrprob):
        """
        :param nrlab_nrprob: problema de laborator data
        :return: o lista ordonata alfabetic cu studenti si nota lor la problema data
        Ridica RepoError cu mesajul "elem inexistent!\n" daca nrlab_nrprob nu este in repositoryLabs
        """
        """
        lab = self.__repoL.cauta_dupa_nr(nrlab_nrprob)
        x = self.get_studenti_lab(nrlab_nrprob)
        x = self.ordonare_alfabetic(x)
        """
        lab = self.__repoL.cauta_dupa_nr(nrlab_nrprob)
        x = []
        elems = self.get_note()
        self.get_studenti_lab_recursiv(nrlab_nrprob, elems, x)
        x = self.ordonare_alfabetic(x, 0)
        return x

    def stats2(self, nrlab_nrprob):
        """
        :param nrlab_nrprob: problema de laborator data
        :return: o lista ordonata dupa nota cu studenti si nota lor la problema data
        Ridica RepoError cu mesajul "elem inexistent!\n" daca nrlab_nrprob nu este in repositoryLabs
        """
        lab = self.__repoL.cauta_dupa_nr(nrlab_nrprob)
        x = self.get_studenti_lab(nrlab_nrprob)
        x = self.ordonare_nota(x, 1)
        return x

    def medii(self):
        """
        :return: o lista de liste in care pe prima pozitie se afla id-ul studentului iar pe a 2-a media la laboratoare
        """
        elems = self.get_note()
        x = []
        for i in elems:
            ok = 0
            for j in x:
                if i.get_student().get_id() == j[0]:
                    j[1] += i.get_nota()
                    j[2] += 1
                    ok = 1
            if not ok:
                lista = [i.get_student().get_id(), i.get_nota(), 1]
                x.append(lista)

        for i in x:
            i[1] /= i[2]
            del i[2]

        return x

    def stats3(self):
        """
        :return: o lista de liste cu studentii care nu au media laboratoarelor mai mare egala cu 5
        pe prima poz in liste este numele studentului, iar pe a 2-a media sa
        """
        x = self.medii()
        j = []
        for i in x:
            if i[1] < 5:
                lista = [(self.__repoS.cauta_dupa_id(i[0])).get_nume(), i[1]]
                j.append(lista)
        return j

    def stats4(self):
        """
        :return: primii 5 studenti cu cele mai multe laboratoare
        """
        elems = self.get_note()
        rez = []
        for el in elems:
            ok = 0
            for r in rez:
                if el.get_student().get_id() == int(r[0]):
                    r[1] += 1
                    ok = 1
            if not ok:
                new = [el.get_student().get_id(), 1]
                rez.append(new)
        rez = self.ordonare_nota(rez, 1)
        rez_final = []
        for i in range(len(rez) - 5, len(rez)):
            st = self.__repoS.cauta_dupa_id(rez[i][0])
            new = [st.get_nume(), rez[i][1]]
            rez_final.append(new)
        rez_final = self.ordonare_alfabetic(rez_final, 0)
        for i in rez_final:
            del i[1]
        return rez_final
