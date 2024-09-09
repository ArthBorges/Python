def combinador(l1, l2: list) -> list:
    l_combinada = []
    if len(l1) > len(l2):
        maior = len(l1)
    else:
        maior = len(l2)

    for i in range(maior):
        if l1 != []:
            caracter1 = l1.pop()
            l_combinada.append(caracter1)
        if l2 != []:
            caracter2 = l2.pop()
            l_combinada.append(caracter2)

    return l_combinada

def inverte_lista(l1, l2: list) -> list:
    l1_invertida = []
    l2_invertida = []
    for i in range(len(l1)):
        caracter = l1.pop()
        l1_invertida.append(caracter)

    for i in range(len(l2)):
        caracter = l2.pop()
        l2_invertida.append(caracter)

    return l1_invertida, l2_invertida

def main():
    n = int(input())
    for i in range(n):
        frase1, frase2 = input().split(' ')
        l1 = list(frase1)
        l2 = list(frase2)
        l1, l2 = inverte_lista(l1, l2)
        l = combinador(l1, l2)
        res = ''.join(l)
        print(res)

main()