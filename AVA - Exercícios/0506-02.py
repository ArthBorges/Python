def achaNum(m: list):
    nums = [0] * 31
    for i in range(len(m)):
        for j in range(len(m[0])):
            nums[m[i][j]] += 1
                
    maiores = []
    maior = nums[0]
    for n in range(1, len(nums)):        
        if nums[n] > maior:
            maior = n
            qtd = nums[n]

    for i in range(len(nums)):
        if nums[i] == qtd:
            maiores.append(i)
    
    for i in range(len(maiores)):
        print(maiores[i])

def main():
    n = int(input())
    matriz = []
    for i in range(n):
        linha = list(map(int, input().split(' ')))
        matriz.append(linha)
    achaNum(matriz)

main()