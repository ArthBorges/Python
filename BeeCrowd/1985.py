def verifica_valor(n: int) -> float:
    valor = 0.00
    for i in range(n):
        cod, qtd = input().split(' ')
        qtd = int(qtd)
        if cod == "1001":
            valor += qtd * 1.50
        elif cod == "1002":
            valor += qtd * 2.50
        elif cod == "1003":
            valor += qtd * 3.50
        elif cod == "1004":
            valor += qtd * 4.50
        else:
            valor += qtd * 5.50

    return valor

def main():
    n = int(input())
    valor = verifica_valor(n)
    print(f'{valor:.2f}')

main()