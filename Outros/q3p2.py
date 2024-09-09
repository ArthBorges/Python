def procuraPalavra(frase, palavra: str) -> bool:
    indices = []
    for i in range(len(frase) - len(palavra) + 1):
        if ver_PinF(frase, palavra, i):
            indices.append(i)
    return indices

def ver_PinF(frase, palavra: str, num: int) -> bool:
    for i in range(len(palavra)):
        if palavra[i] != frase[i + num]:
            return False
    return True

def main():
    frase = input()
    palavra = input()
    res = procuraPalavra(frase, palavra)
    if res == []:
        print('NOT FOUND!')
    else:
        for i in range(len(res)):
            print(res[i])

main()