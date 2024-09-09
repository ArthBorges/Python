def soma_seq(l1, l2: list) -> list:
    l_soma = []
    resto = 0
    for i in range(len(l1) - 1, -1, -1):
        soma = l1[i] + l2[i] + resto
        inteiro = soma % 10
        resto = soma // 10
        l_soma.append(inteiro)
    if resto != 0:
        l_soma.append(resto)
    return l_soma

def main():
    l1 = list(map(int, input().split(' ')))
    l2 = list(map(int, input().split(' ')))
    soma = soma_seq(l1, l2)
    for i in range(len(soma)):
        num = soma.pop()
        print(f'{num}', end=' ')
main()