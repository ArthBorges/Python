# Faça um programa em Python 3 que leia um número inteiro 1 < n < 1000000 e responda se ele é Primo ou Composto.

def verifica_primo(n):
    primo = True

    for i in range(2, n):
        if n % i == 0:
            primo = False

    return primo


def main():
    n = int(input())
    primo = verifica_primo(n)
    if primo:
        print("Primo")
    else:
        print("Composto")


main()
