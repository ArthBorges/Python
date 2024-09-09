# Escreva um programa que leia um número inteiro representando um ano. O programa deve responder se o ano é bissexto ou não.

def bissexto(ano):
    bissexto = False
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        bissexto = True
    return bissexto


def main():
    ano = int(input())
    res = bissexto(ano)
    if res:
        print('Bissexto')
    else:
        print("Ano qualquer")


main()
