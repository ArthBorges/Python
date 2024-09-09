def achaMaior(m: list) -> int:
    maior = m[0][0]
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] > maior:
                maior = m[i][j]    
    return maior

def main():
    m, n = map(int, input().split(' '))
    matriz = []
    for i in range(m):
        linha = list(map(int, input().split(' ')))
        matriz.append(linha)
    print(achaMaior(matriz))

main()