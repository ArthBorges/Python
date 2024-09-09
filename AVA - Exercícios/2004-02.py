# Faça um programa em Python 3 que leia um inteiro n > 0, em seguida leia uma sequência de n números inteiros, e imprima
# na saída o tamanho da maior subsequência crescente encontrada na sequência de números lidos.

def maior_sub(n):
    cont = 1
    maiorsub = 1
    ant = int(input())
    for i in range(1, n):
        num = int(input())
        if num > ant:
            cont += 1
            if cont > maiorsub:
                maiorsub = cont
        else:
            cont = 1
        ant = num
    return maiorsub


def main():
    n = int(input())
    tamanho = maior_sub(n)
    print(tamanho)


main()
