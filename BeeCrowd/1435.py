def criaMatriz(n: int) -> list:
    m = [[0]*n for i in range(n)]    
    col = lin = 0
    colf = linf = n-1
    
    for i in range(1, (n + 1) // 2 + 1):    
        for j in range(col, colf + 1):
            m[lin][j] = i
            m[linf][j] = i
        for k in range(lin + 1, colf):
            m[k][col] = i
            m[k][colf] = i            
        col += 1
        colf -= 1
        lin += 1
        linf -= 1

    return m

def imprime(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            if j == len(M[0]) - 1:
                print(f"{M[i][j]:>3}", end='')
            else:
                print(f"{M[i][j]:>3}", end=' ')
        print()
    print()

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        else:         
            m = criaMatriz(n)
            imprime(m)          

main()