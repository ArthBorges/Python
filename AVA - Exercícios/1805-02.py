def produto_vetor(u, v: list) -> float:
    tam = len(u)
    prod = 0
    for i in range(tam):
        prod += u[i] * v[i]
    return prod

def main():
    vetor_u = list(map(float, input().split(' ')))
    vetor_v = list(map(float, input().split(' ')))
    res = produto_vetor(vetor_u, vetor_v)
    print(f'{res:.4f}')

main()