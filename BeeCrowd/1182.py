def somaMedia(m: list, c: int, t: str) -> float:
    soma = 0
    for i in range(len(m)):
        soma += m[i][c]

    if t == 'S':
        return soma
    else:
        return soma / len(m)

def main():
    c = int(input())
    t = input()

    n = 12
    m = [[0]*n for i in range(n)]

    for i in range(n):
        for j in range(n):
            m[i][j] = float(input())
    
    valor = somaMedia(m, c, t)
    print(f"{valor:.1f}")

main()