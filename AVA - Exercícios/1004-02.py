# Dado um número inteiro n > 0 temos que o subnúmero par de n é o número gerado a partir da remoção dos dígitos ímpares que aparecem em n.
# Por exemplo, se n = 2546718, o subnúmero par de n é 2468.
# Faça um programa em Python 3 que leia um número inteiro n > 0 e responda qual é o seu subnúmero par.
# Obs.: O número deve se lido como um inteiro e não deve ser transformado para string.

def subnumeros(n):
    subnum = 0
    i = 1
    while n > 0:
        num = n % 10
        if num % 2 == 0:
            subnum += num * i
            i *= 10
        n //= 10
    return subnum


def main():
    n = int(input())
    subnum = subnumeros(n)
    print(subnum)


main()
