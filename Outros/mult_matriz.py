def multiplica(A, B: list) -> list:
    m_res = [[0]*len(B[0]) for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                m_res[i][j] += A[i][k] * B[k][j]
    return m_res

def imprime(M: list):
	n = len(M)
	for i in range(n):
		for j in range(n):
			print(M[i][j], end="\t")
		print("")

def main():
    n = int(input())
    A = []
    for i in range(n):
        linha = list(map(int, input().split(' ')))
        A.append(linha)
    
    m = int(input())
    B = []
    for i in range(m):
        linha = list(map(int, input().split(' ')))
        B.append(linha)

    if len(A[0]) == len(B):
        imprime(multiplica(A, B))
    else:
        print('Impossivel Calcular')

main()