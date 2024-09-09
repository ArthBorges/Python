# Faça um programa em Python 3 que leia um inteiro 0 <= n <= 100 e calcule o valor de n!.

def fatorial(n):
    fatorial = 1
    for i in range(1, n+1):
        fatorial *= i
    return fatorial


def main():
    n = int(input())
    print(fatorial(n))

main()