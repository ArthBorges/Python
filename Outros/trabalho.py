# =============== Para N ÍMPAR =============== #
def caso1(n: int) -> list:
    m = [[0] * n for i in range(n)]
    i = 0
    j = n // 2
    for k in range(1, (n ** 2) + 1):
        m[i][j] = k
        i -= 1
        j += 1
        if k % n == 0:
            i += 2
            j -= 1
        elif i < 0:
            i = n - 1
        elif j == n:
            j = 0
    return m
# ============================================ #

# =============== Para N = 4m ================ #
def caso2(n: int) -> list:
    m = [[0] * n for i in range(n)]
    cont = 1
    for i in range(len(m)):
        for j in range(len(m[0])):
            m[i][j] = cont
            cont += 1

    for i in range(0, len(m), 4):
        for j in range(0, len(m[0]), 4):
            m4x4 = matriz4x4(m, n, i, j)
            m4x4 = mudaDiagonal(m4x4, n)
            for k in range(len(m4x4)):
                for l in range(len(m4x4[0])):
                    if m[k+i][l+j] != m4x4[k][l]:
                        m[k+i][l+j] = m4x4[k][l]
    return m

def matriz4x4(m: list, n, k, l: int) -> list:
    matriz4x4 = [[0] * 4 for i in range(4)]
    for i in range(len(matriz4x4)):
        for j in range(len(matriz4x4[0])):
            matriz4x4[i][j] = m[k+i][l+j]
    return matriz4x4

def mudaDiagonal(matriz4x4: list, n: int) -> list:
    for i in range(len(matriz4x4)):
        for j in range(len(matriz4x4[0])):
            if i == j or j == len(matriz4x4) - (1+i):
                matriz4x4[i][j] = (n ** 2 + 1) - matriz4x4[i][j]
    return matriz4x4
# ============================================ #

# ============= Para N = 4m + 2 ============== #
def caso3(n, m: int) -> list:
    aux = (2 * m + 1)
    m_aux = [[0] * aux for i in range(aux)]
    for i in range(len(m_aux)):
        for j in range(len(m_aux[0])):
            if i < m+1:
                m_aux[i][j] = "L"
            elif i == m+1:
                m_aux[i][j] = "U"
            elif i > m-1:
                m_aux[i][j] = "X"
    m_aux[len(m_aux)//2][len(m_aux)//2] = 'U'
    m_aux[len(m_aux)//2+1][len(m_aux)//2] = 'L'
    matriz = preencheM(m_aux, n)
    return matriz

def preencheM(m_aux: list, n: int) -> list:
    m = [[0] * n for i in range(n)]
    pos = len(m_aux)
    i = 0
    j = pos // 2
    num = 0
    for k in range(len(m_aux)**2):
        num += 1
        if m_aux[i][j] == "L":
            m[i*2+0][j*2+1] = num
            num+=1
            m[i*2+1][j*2+0] = num
            num+=1
            m[i*2+1][j*2+1] = num
            num+=1
            m[i*2+0][j*2+0] = num                
        elif m_aux[i][j] == "U":
            m[i*2+0][j*2+0] = num
            num+=1
            m[i*2+1][j*2+0] = num
            num+=1
            m[i*2+1][j*2+1] = num
            num+=1
            m[i*2+0][j*2+1] = num
        elif m_aux[i][j] == "X":
            m[i*2+0][j*2+0] = num
            num+=1
            m[i*2+1][j*2+1] = num
            num+=1
            m[i*2+1][j*2+0] = num
            num+=1
            m[i*2+0][j*2+1] = num        
        i -= 1
        j += 1
        if num % pos == 0:
            i += 2
            j -= 1
        elif i < 0:
            i = pos - 1
        elif j == pos:
            j = 0
    return m
# ============================================ #
def imprimeMatriz(M: list):
    n = len(M)
    for i in range(n):
        for j in range(n):
            print(M[i][j], end="\t")
        print("")

def main():
    n = int(input())
    if n % 2 == 1:
        m_constante = caso1(n)
        print("Caso 1:")
        imprimeMatriz(m_constante)
    elif n % 4 == 0:
        m_constante = caso2(n)
        print("Caso 2:")
        imprimeMatriz(m_constante)
    elif n % 4 == 2:
        m = n // 4
        m_constante = caso3(n, m)
        print("Caso 3:")
        imprimeMatriz(m_constante)

main()