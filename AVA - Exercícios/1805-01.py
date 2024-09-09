def separa_letras(sentenca: str) -> list:
    letras = []
    for letra in sentenca:
        if ord(letra) > 64 and ord(letra) < 91 or ord(letra) > 96 and ord(letra) < 123:
            letras.append(letra)

    for i in range(len(letras)):
        num = ord(letras[i])
        if num > 96 and num < 123:
            num -= 32
            caracter = chr(num)
            letras[i] = caracter

    qtd = []
    for i in range(len(letras)):
        qtd.append(ord(letras[i]))

    return qtd


def ordena_letras(qtd: list):
    for i in range(1, len(qtd)):
        temp = qtd[i]
        n = i - 1
        while n >= 0 and qtd[n] > temp:
            qtd[n + 1] = qtd[n]
            n -= 1
            qtd[n + 1] = temp


def conta_letras(qtd: list) -> list:
    qtd_letras = []
    for num in qtd:
        if num not in qtd_letras:
            qtd_letras.append(num)

    qtd_numeros = []
    for i in range(len(qtd_letras)):
        cont = 0
        num = qtd_letras[i]
        for caso in qtd:
            if num == caso:
                cont += 1
        qtd_numeros.append(cont)

    return qtd_letras, qtd_numeros


def imprime(qtd_letras, qtd_numeros: list):
    for i in range(len(qtd_letras)):
        letra = chr(qtd_letras[i])
        print(f'{letra}: {qtd_numeros[i]}')


def main():
    sentenca = input()
    lista = separa_letras(sentenca)
    ordena_letras(lista)
    letra, num = conta_letras(lista)
    imprime(letra, num)


main()