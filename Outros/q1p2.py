def balanca(l: list) -> bool:
    ultimo = -1
    soma = l[0] + l[ultimo]
    for i in range(1, len(l)//2):
        ultimo -= 1
        soma2 = l[i] + l[ultimo]   
        if soma != soma2:
            return False
    return True

def main():
    l = list(map(int, input().split(' ')))
    if balanca(l):
        print('SIM')
    else:
        print('NAO')

main()