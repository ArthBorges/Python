def transpoe(m: list):
    mt = [[0] * len(m) for i in range(len(m[0]))]
    for i in range(len(m)):
        for j in range(len(m[0])):
            mt[j][i] = m[i][j]                    
    imprimeMatriz(mt)

def imprimeMatriz(M: list):
    for i in range(len(M)):
        for j in range(len(M[0])):
            print(M[i][j], end=" ")
        print("")

def main():
    m, n = map(int, input().split(' '))
    matriz = []
    for i in range(m):
        linha = list(map(int, input().split(' ')))
        matriz.append(linha)
    transpoe(matriz)

main()