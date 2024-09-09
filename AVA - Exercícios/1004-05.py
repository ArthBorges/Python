# Faça um programa em Python 3 que leia um número real x > 0 e um número inteiro n ≥ 0 e calcule o valor de e^x com 4 casas decimais.

def fatorial(n):
    fatorial = 1
    for i in range(1, n+1):
        fatorial *= i
    return fatorial


def const_euler(e, n):
    res = 1
    while n > 0:
        res += ((e**n)/fatorial(n))
        n -= 1
    return res


def main():
    e = float(input())
    n = int(input())
    res = const_euler(e, n)
    print(f"{res:.4f}")


main()
