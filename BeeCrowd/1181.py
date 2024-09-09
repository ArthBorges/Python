def somaMedia(m: list, l: int, t: str) -> float:
    soma = 0
    for j in range(len(m[0])):
        soma += m[l][j]

    if t == 'S':
        return soma
    else:
        return soma / len(m[0])

def main():
    l = int(input())
    t = input()

    n = 12
    m = [[0]*n for i in range(n)]

    for i in range(n):
        for j in range(n):
            m[i][j] = float(input())
    
    valor = somaMedia(m, l, t)
    print(f"{valor:.1f}")

main()