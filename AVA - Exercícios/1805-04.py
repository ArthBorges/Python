def derivada(coef: list) -> float:
    l = []
    for i in range(1, len(coef)):
        l.append(coef[i] * i)
    for i in range(len(l)):
        print(f'{l[i]:.4f}')

def main():
    coeficientes = list(map(float, input().split(' ')))
    derivada(coeficientes)

main()