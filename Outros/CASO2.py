def preencheM(n: int):
    m = [[0]*n for i in range(n)]
    num = 1

    for i in range(n):
        if i % 2 == 0:
            for j in range(n):
                m[i][j] = num
                num += 1
        else:
            for j in range(n-1, -1, -1):
                m[i][j] = num
                num += 1
    imprime(m)

def imprime(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            print(f"{M[i][j]:>3}", end='\t')
        print()


def main():
    n = int(input())
    preencheM(n)

main()