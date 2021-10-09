class Cititor(object):
    def __init__(self, string):
        self.__string = string

    def comanda(self):
        x = self.__string.split(';')
        return x

    def __separator_in_comanda(self, string):
        """
        :return: o lista cu cuvintele din sirul initial despartite
        """
        x = string.split(" ")
        while "" in x:
            x.remove("")
        return x

    def run(self, string):
        return self.__separator_in_comanda(string)
