# Faça um programa em Python 3 que leia um número inteiro positivo e responda quantos dígitos esse número tem.

def conta_dig(n):
    if n == 0:
        contador = 1
    else:
        contador = 0
        while n != 0:
            contador += 1
            n = n // 10
    return contador


def main():
    n = int(input())
    res = conta_dig(n)
    print(res)


main()
