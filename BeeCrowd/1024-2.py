def criptografa_1(l: list) -> list:    
    for i in range(len(l)):
        if ord(l[i]) > 64 and ord(l[i]) < 91 or ord(l[i]) > 96 and ord(l[i]) < 123:
            num = ord(l[i])
            num += 3
            letra = chr(num)
            l[i] = letra
    return l

def criptografa_2(l: list) -> list:
    l_invertida = []
    for i in range(len(l)):
        caracter = l.pop()
        l_invertida.append(caracter)
    return l_invertida

def criptografa_3(l: list) -> list:
    metade = len(l) // 2
    for i in range(metade, len(l)):
        caracter = ord(l[i])
        caracter -= 1
        letra = chr(caracter)
        l[i] = letra
    return l

def leitura_e_saida():
    msg = input()
    l = list(msg)
    criptografia = criptografa_1(l)
    criptografia = criptografa_2(criptografia)
    criptografia = criptografa_3(criptografia)
    resposta = "".join(criptografia)
    print(resposta)

def main():
    casos = int(input())
    for i in range(casos):
        leitura_e_saida()

main()