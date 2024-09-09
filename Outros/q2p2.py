def somaOrdena(A, B: list) -> list:
    C = A + B
    for i in range(1, len(C)):
        p = C[i]
        j = i - 1
        while j >= 0 and C[j] > p:
            C[j+1] = C[j]
            j -= 1
        C[j+1] = p
    return C

def main():
    A = list(map(int, input().split(' ')))
    B = list(map(int, input().split(' ')))
    C = somaOrdena(A, B)
    print(C)

main()