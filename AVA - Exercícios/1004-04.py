# Faça um programa em Python 3 que leia um inteiro n > 0 e imprima o valor do n-ésimo número harmônico. O valor deve ser apresentado com 4 casas decimais.

def harmonico(n):
    har = 0
    while n > 0:
        har += (1/n)
        n -= 1
    return har


def main():
    n = int(input())
    har = harmonico(n)
    print(f"{har:.4f}")


main()
