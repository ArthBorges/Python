def inverte_frase(l: list) -> list:
    l_invertida = []
    metade_dir = []
    metade = len(l) // 2

    for i in range(metade, len(l)):
        caracter = l.pop()
        metade_dir.append(caracter)

    for i in range(len(l)):
        caracter = l.pop()
        l_invertida.append(caracter)

    for i in range(len(metade_dir)):
        caracter = metade_dir.pop()
        l.append(caracter)

    for i in range(len(l)):
        caracter = l.pop()
        l_invertida.append(caracter)

    return l_invertida

def main():
    n = int(input())
    for i in range(n):
        l = list(input())
        l = inverte_frase(l)
        res = ''.join(l)
        print(res)

main()