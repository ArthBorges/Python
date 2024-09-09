def verifica_num(l: list, k: int) -> int:
    maior = 0
    menor = 0
    for i in range(len(l)):
        if l[i] > k:
            maior += 1
        if l[i] < k:
            menor += 1
    return maior, menor

def main():
    l = list(map(int, input().split(' ')))
    k = int(input())
    maior, menor = verifica_num(l, k)
    print(f'Maior: {maior}\nMenor: {menor}')
main()