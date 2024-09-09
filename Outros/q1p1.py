n = int(input())
num = int(input())

maior = num
menor = num

for i in range(1, n):
    num = int(input())
    if num > maior:
        maior = num
    elif num < menor:
        menor = num       

print(f"Maior: {maior}")
print(f"Menor: {menor}")