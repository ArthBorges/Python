n = int(input())

pi = 4
sinal = -1

for i in range(3, n+1, 2):
    num = (4/i)
    pi += num * sinal
    sinal *= -1

print(f"{pi:.4f}")