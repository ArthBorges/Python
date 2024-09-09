# Faça um programa em Python 3 que leia um número binário e converta-o para a base decimal.
# O número deve ser lido como int e jamais deve ser convertido para string.

def calcula_dec(binario):
    n = 0
    pos = 1

    while binario > 0:
        resto = binario % 10
        n += resto * pos
        pos = pos * 2
        binario = binario // 10
    return n


def main():
    binario = int(input())
    decimal = calcula_dec(binario)
    print(decimal)


main()
