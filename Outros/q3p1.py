decimal = int(input())

ternario = 0
pos = 1

while decimal > 0:
    resto = decimal % 3
    ternario += resto * pos
    pos *= 10
    decimal //= 3

print(ternario)