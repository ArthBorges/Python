def criptografa(l: list) -> list:
    l_invertida = []
    for i in range(len(l)):
        if ord(l[i]) > 64 and ord(l[i]) < 91 or ord(l[i]) > 96 and ord(l[i]) < 123:
            num = ord(l[i])
            num += 3
            letra = chr(num)
            l[i] = letra

    for i in range(len(l)):
        caracter = l.pop()
        l_invertida.append(caracter)

    metade = len(l_invertida) // 2
    for i in range(metade, len(l_invertida)):
        caracter = ord(l_invertida[i])
        caracter -= 1
        letra = chr(caracter)
        l_invertida[i] = letra

    return l_invertida

def main():
    casos = int(input())
    for i in range(casos):
        msg = input()
        l = list(msg)
        criptografia = criptografa(l)
        resposta = "".join(criptografia)
        print(resposta)

main()