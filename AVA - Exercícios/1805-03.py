def polinomio(coef: list, x: float) -> float:
    soma = 0
    for i in range(len(coef)):
        soma += coef[i] * x ** i
    
    return soma

def main():
    coeficientes = list(map(float, input().split(' ')))
    k = int(input())
    for i in range(k):
        x = float(input())
        res = polinomio(coeficientes, x)
        print(f'{res:.4f}')

main()