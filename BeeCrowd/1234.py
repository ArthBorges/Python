def seq_dancante(sentenca: str) -> list:
    seq = []
    maiuscula = True

    for letra in sentenca:
        if letra != ' ':
            cod = ord(letra)
            if maiuscula:
                if cod > 64 and cod < 91:
                    seq.append(letra)
                else:
                    caracter = chr(cod - 32)
                    seq.append(caracter)
            else:
                if cod > 96 and cod < 123:
                    seq.append(letra)
                else:
                    caracter = chr(cod + 32)
                    seq.append(caracter)
            maiuscula = not maiuscula

        else:
            seq.append(' ')

    return seq

def main():
    while True:
        try:
            sentenca = input()
            l = seq_dancante(sentenca)
            resposta = "".join(l)
            print(resposta)
        except EOFError:
            break

main()