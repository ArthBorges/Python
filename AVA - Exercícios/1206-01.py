def ver_constante(m: list) -> bool:
    constante = 0
    for i in range(1):
        for j in range(len(m[0])):
            constante += m[i][j]

    soma = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            soma += m[i][j]
        if soma != constante:
            return False
        else:
            soma = 0
    
    for j in range(len(m[0])):
        for i in range(len(m)):
            soma += m[i][j]
        if soma != constante:
            return False
        else:
            soma = 0

    for i in range(len(m)):
        for j in range(len(m[0])):
            if i == j:
                soma += m[i][j]
    if soma != constante:
        return False
    else:
        soma = 0

    for i in range(len(m)):
        for j in range(len(m[0])):
            if j == len(m) - (i+1):
                soma += m[i][j]
    if soma != constante:
        return False
    else:
        soma = 0

    return True
    
def main():
    n = int(input())
    m = []
    for i in range(n):
        linha = list(map(int, input().split(' ')))
        m.append(linha)
    if ver_constante(m):
        print('SIM')
    else:
        print("NAO")

main()