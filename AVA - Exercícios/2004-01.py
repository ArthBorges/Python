# Faça um programa que leia um número real x e um número inteiro não negativo n, e calcule o valor da potência x^n
# Deve ser utilizada uma estrutura de repetição para calcular a potência e não o operador ** do Python.

def calcula(x, n):
    multiplicador = x
    if n == 0:
        x = 1
    for i in range(1, n):
        x *= multiplicador
    return x


def main():
    x = float(input())
    n = int(input())
    res = calcula(x, n)

    print(f"{res:.2f}")


main()
