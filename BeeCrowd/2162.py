def picosEvales(l: list) -> int:
    if l[1] > l[0]:
        crescente = True
    elif l[1] < l[0]:
        crescente = False
    else:
        return 0
    for i in range(2, len(l)):
        if l[i] > l[i-1] and not crescente:
            crescente = True
        elif l[i] < l[i-1] and crescente:
            crescente = False
        else:
            return 0
    return 1

def main():
    n = int(input())
    l = list(map(int, input().split(' ')))
    res = picosEvales(l)
    print(res)

main()