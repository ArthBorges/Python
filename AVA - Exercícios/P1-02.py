# Faça um programa em Python 3 que leia um número ímpar n > 0 e calcule a aproximação do Pi com 4 casas decimais.

def calc_pi(n):
    pi = 4
    sinal = -1
    for i in range(3, n+1, 2):
        num = (4/i)
        pi += num * sinal
        sinal *= -1
    return pi


def main():
    n = int(input())
    pi = calc_pi(n)
    print(f"{pi:.4f}")


main()
