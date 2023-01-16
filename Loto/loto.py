import random


def lotofacil(qtd_apostas: int, qtd=15):
    FAIXA = 25
    QTD_MIN = 15
    QTD_MAX = 18
    NUMEROS = range(1, FAIXA + 1)
    lista = []

    if qtd != '':
        if qtd < QTD_MIN or qtd > QTD_MAX:
            print('quantide de numeros para lotofacil deve estar entre: {} e {}'.format(
                QTD_MIN, QTD_MAX))
        else:
            for i in range(0, qtd_apostas):
                x = random.sample(NUMEROS, qtd)
                lista.append(x)
                return lista

    else:
        for i in range(0, qtd_apostas):
            x = random.sample(NUMEROS, QTD_MIN)
            lista.append(x)
            return lista


print('Numeros da lotofacil:')
numeros = lotofacil(2)
for i in numeros:
    print(i)
