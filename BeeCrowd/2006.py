def degusta_cha(l: list, n: int) -> int:
    acertos = 0
    for i in range(len(l)):
        if l[i] == n:
            acertos += 1

    return acertos

def main():
    n = int(input())
    l = list(map(int, input().split(" ")))
    resposta = degusta_cha(l, n)
    print(resposta)

main()