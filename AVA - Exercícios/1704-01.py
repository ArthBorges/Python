# Faça um programa em Python 3 que leia um inteiro n > 0, em seguida leia uma sequência de n números inteiros e calcule
# a soma dos números pares e a soma dos números ímpares da sequência.

def pares_impar(n):
    pares = 0
    impar = 0

    while n > 0:
        m = int(input())
        if m % 2 == 0:
            pares += m
        else:
            impar += m
        n -= 1
    return pares, impar


def main():
    n = int(input())
    pares, impar = pares_impar(n)
    print(f"Pares: {pares}")
    print(f"Impares: {impar}")


main()
