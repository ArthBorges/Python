def somaMaior(m: list) -> int:
    maior = m[0][0]
    maiores = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] > maior:
                maior = m[i][j]        
        maiores.append(maior)
        maior = 0
    soma = 0
    for i in range(len(maiores)):
        soma += maiores[i]
    return soma

def main():
    m = int(input())
    n = int(input())
    matriz = []
    for i in range(m):
        linha = list(map(int, input().split(' ')))
        matriz.append(linha)
    print(somaMaior(matriz))
    
main()