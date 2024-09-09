def procura_palavra(frase, palavra: str) -> bool:
    for i in range(len(frase) - len(palavra) + 1):
        if verifica_palavra(frase, palavra, i):
            return True
    return False

def verifica_palavra(frase, palavra: str, indice: int) -> bool:
    for i in range(len(palavra)):
        if palavra[i] != frase[indice + i]:
            return False
    return True

def main():
    frase = input()
    palavra = input()
    if procura_palavra(frase, palavra):
        print('SIM')
    else:
        print('NAO')
main()