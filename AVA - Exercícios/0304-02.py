# Faça um programa em Python 3 que leia um número inteiro na base decimal e converta-o para a base binária.
# O número lido não deve ser convertido para string.

def calcula_bin(n):
    binario = 0
    pos = 1

    while n > 0:
        resto = n % 2
        binario += resto * pos
        pos = pos * 10
        n = n // 2
    return binario


def main():
    n = int(input())
    binario = calcula_bin(n)
    print(binario)


main()
