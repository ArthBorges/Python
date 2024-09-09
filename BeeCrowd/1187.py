def somaMedia(m: list, t: str) -> float:
    soma = 0
    cont = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if j < len(m) - (i+1) and j > i:
                soma += m[i][j]
                cont += 1

    if t == 'S':
        return soma
    else:
        return soma / cont

def main():
    t = input()

    n = 12
    m = [[0]*n for i in range(n)]

    for i in range(n):
        for j in range(n):
            m[i][j] = float(input())
    
    valor = somaMedia(m, t)
    print(f"{valor:.1f}")

main()