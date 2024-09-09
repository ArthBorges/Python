# Faça um programa em Python 3 que leia um inteiro n > 0 e em seguida leia uma sequência de n números inteiros, um por linha.
# O seu programa deve responder qual é o maior valor e qual é o menor valor da sequência.


def menor_maior(n):
    num = int(input())
    maior = num
    menor = num

    for i in range(1, n):
        num = int(input())
        if num > maior:
            maior = num
        elif num < menor:
            menor = num

    return menor, maior


def main():
    n = int(input())
    menor, maior = menor_maior(n)

    print(f"Maior = {maior}")
    print(f"Menor = {menor}")


main()

