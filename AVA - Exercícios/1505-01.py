def conta_faces(l, faces: list) -> list:
    for num in l:        
        faces[num-1] += 1

    return faces

def porcentagem(l: list, n: int) -> list:
    porcentagem = []
    mult = 100 / n
    for i in range(len(l)):        
        num = l[i]
        num *= mult
        porcentagem.append(num)

    return porcentagem

def formata_imprime(l: list):
    for i in range(13):
        print(f'Face {i+1}: {l[i]:.2f}%')

def main():
    n = int(input())
    l = list(map(int, input().split()))
    faces = [0] * 13
    resultado = conta_faces(l, faces)
    resultado = porcentagem(resultado, n)
    resultado = formata_imprime(resultado)

main()