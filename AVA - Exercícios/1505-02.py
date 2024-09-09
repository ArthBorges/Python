def junta_frase(l: list) -> list:
    for letra in l:
        if letra == ' ':
            l.remove(' ')

    return l

def ver_palindromo(l: list) -> list:
    frase_original = ''.join(l)
    frase_palindromo = []
    for i in range(len(l)):
        letra = l.pop()
        frase_palindromo.append(letra)

    resultado = ''.join(frase_palindromo)
    if resultado == frase_original:
        palindromo = True
    else:
        palindromo = False
    
    return palindromo

def main():
    frase = list(input())
    l = junta_frase(frase)
    palindromo = ver_palindromo(l)

    if palindromo:
        print("SIM")
    else:
        print("NAO")

main()