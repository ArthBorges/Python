def preencheM(m: list):    
    num = 1
    inicio = 0
    fim = len(m) - 1
    for camada in range(len(m)//2+1):
        for i in range(inicio, fim + 1):
            m[inicio][i] = num
            num += 1
        for i in range(inicio + 1, fim + 1):
            m[i][fim] = num
            num += 1
        for i in range(fim - 1, inicio - 1, -1):
            m[fim][i] = num
            num += 1
        for i in range(fim - 1, inicio, -1):
            m[i][inicio] = num
            num += 1

        inicio += 1
        fim -= 1

    if inicio == fim:
        m[inicio][fim] = num

    t = len(str(len(m) ** 2))
    imprime(m, t)

def imprime(M, t):    
    for i in range(len(M)):
        for j in range(len(M[0])):
            if j == len(M[0]) - 1:
                print(f"{M[i][j]:>{t}}", end='')
            else:
                print(f"{M[i][j]:>{t}}", end=' ')
        print()

def main():
    n = int(input())
    matriz = [[0]*n for i in range(n)]
    preencheM(matriz)
    
main()