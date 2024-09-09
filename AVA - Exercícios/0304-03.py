# O jogo Fizz Buzz é um jogo popular para ensinar crianças sobre divisão de números.
# Elas sentam em círculo e, em sentido horário, cada uma fala em voz alta um número em sequência, começando pelo número 1.
# No entanto, se o número for divisível por 3, a criança não pode falar o número e sim dizer "Fizz".
# Se o número for divisível por 5, ela deve dizer "Buzz". E se o número for divisível por ambos, 3 e 5, ela deve dizer "FizzBuzz".
# Faça um programa em Python que leia um número inteiro n > 0 e imprima a sequência de 1 até n dada por um jogo de Fizz Buzz.

def fizzbuzz(n):
    cont = 1
    while cont <= n:
        if cont % 3 == 0:
            if cont % 5 == 0:
                print("FizzBuzz")
            else:
                print("Fizz")
        elif cont % 5 == 0:
            print("Buzz")
        else:
            print(cont)
        cont += 1


def main():
    n = int(input())
    fizzbuzz(n)


main()
