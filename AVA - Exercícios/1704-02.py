# Faça um programa em Python 3 que leia um número real x > 0 e um número par k ≥ 0. O programa deve calcular o cosseno de x com 4 casas decimais.

def fatorial(n):
    fatorial = 1
    for i in range(1, n+1):
        fatorial *= i

    return fatorial


def cosseno(x, k):
    cos = 0
    neg = 1
    for i in range(0, k+1, 2):
        cos += (x**i/fatorial(i)) * neg
        neg *= -1

    return cos


def main():
    x = float(input())
    k = int(input())
    cos = cosseno(x, k)

    print(f"{cos:.4f}")


main()