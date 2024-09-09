# No sistema de numeração ternário, os únicos algarismos que podem ser utilizados são o 0 (zero), 1 (um) e o 2 (dois).
# Sendo assim, para representar o número decimal 3 na base ternária temos que utilizar dois algarismos: 10.
# Seguindo essa lógica, o número decimal 4 em ternário é 11. E assim por diante.
# Faça um programa que leia um número decimal e converta-o para a base ternária.

def calc_ternario(decimal):
    ternario = 0
    pos = 1

    while decimal > 0:
        resto = decimal % 3
        ternario += resto * pos
        pos *= 10
        decimal //= 3

    return ternario


def main():
    n = int(input())
    ternario = calc_ternario(n)
    print(ternario)


main()
