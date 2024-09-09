def preencheM(n: int):
    m = [[0]*n for i in range(n)]
    contador = 1
    for j in range(n):
        if j % 2 == 0:
            for i in range(n):
                m[i][j] = contador
                contador += 1
        else:
            for i in range(n-1, -1, -1):
                m[i][j] = contador
                contador += 1
    imprime(m)

def imprime(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            print(M[i][j], end='\t')
        print()

def main():
    n = int(input())    
    preencheM(n)
    
main()