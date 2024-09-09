n = int(input())
A = [[1]]
for i in range(1, n):
    A.append([1])
    for j in range(1, i):
        A[i].append(A[i - 1][j] + A[i - 1][j - 1])
    A[i].append(1)

for linha in A:
    print(linha)

n = int(input())
L = [1]
print(L)
for i in range(1, n):
    ant = 1
    for j in range(1, i):
        L[j], ant = ant + L[j], L[j]
    L.append(1)
    print(L)

n = int(input())
L = [1]
print(L)
for i in range(1, n):
    L.append(1)
    for j in range(i - 1, 0, -1):
        L[j] = L[j - 1] + L[j]
    print(L)
