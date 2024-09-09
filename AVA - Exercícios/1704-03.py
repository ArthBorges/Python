# Faça um programa em Python 3 que leia um número inteiro não negativo e responda "SIM" se ele for um palíndromo, e "NAO" caso contrário.
# O programa deve ler a entrada como um número inteiro e o número não pode ser transformado para string em nenhum momento.

def palindromo(n):
    palindromo = 0
    while n > 0:
        dig = n % 10
        palindromo = palindromo * 10 + dig
        n //= 10

    return palindromo


def main():
    n = int(input())
    numero = n
    pali = palindromo(n)

    if numero == pali:
        print("SIM")
    else:
        print("NAO")


main()
