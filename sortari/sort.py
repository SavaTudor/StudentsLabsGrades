def insertionSort(x, key, cmp):
    """
    :param x: lista pe care o sortam
    :param key:cheia elementelor din lista pe care le comparam
    :param cmp: criterile de comparatie
    :return: -
    ordoneaza lista x prin procedeul insertionSort
    """
    for i in range(1, len(x)):
        poz = i - 1
        elem = x[i]

        while poz >= 0 and cmp(key(elem), key(x[poz])):
            x[poz + 1] = x[poz]
            poz = poz - 1
        x[poz + 1] = elem


def combSort(x, key, cmp):
    """
    :param x: lista pe care o sortam
    :param key: cheia elementelor pe care le comparam
    :param cmp: criteriile de comparatie
    :return: -
    ordoneaza lista x prin procedeul combSort
    """

    def urmZona(zonaActuala):
        zona = int((zonaActuala * 10) / 13)
        if zona < 1:
            return 1
        return zona

    n = len(x)
    zona = n
    ok = 1
    while zona != 1 or ok:
        zona = urmZona(zona)
        ok = 0
        for i in range(0, n - zona):
            if cmp(key(x[i]), key(x[i + int(zona)])):
                x[i], x[i + int(zona)] = x[i + int(zona)], x[i]
                ok = 1
