def conta_impar(x, y: int) -> list:
    res = []
    while len(res) < y:
        for i in range(x, x+5):
            if i % 2 == 1:
                res.append(i)
    print(res)

    soma = 0
    for i in range(len(res)):
       soma += res[i]
    print(soma)

def main():
    n = int(input())
    for i in range(n):
        x, y = map(int, input().split(' '))
        conta_impar(x, y)


main()
#NÃO FINALIZADO