k = int(input())

pos = 0
n = int(input())
menor = n

for i in range(1, k+1):
    n = int(input())   
    print(i, end=" ")
    if n < menor:
        menor = n
        pos = k

print(f"{menor}\n{pos}")

#não terminad
