def imprime(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            print(M[i][j], end='\t')
        print()
