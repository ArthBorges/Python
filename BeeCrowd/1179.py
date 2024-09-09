def pares_impares() -> list:
    l_pares = []
    resto_pares = []
    l_impar = []
    resto_impar = []
    for i in range(15):
        n = int(input())
        if n % 2 == 0:
            l_pares.append(n)
            resto_pares.append(n)
            if len(l_pares) == 5:
                for i in range(len(l_pares)):
                    print(f'par[{i}] = {l_pares[i]}')
                l_pares = []
                resto_pares = []
        if n % 2 == 1:
            l_impar.append(n)
            resto_impar.append(n)
            if len(l_impar) == 5:
                for i in range(len(l_impar)):
                    print(f'impar[{i}] = {l_impar[i]}')
                l_impar = []
                resto_impar = []
    return resto_impar, resto_pares

def main():
    impar, par = pares_impares()
    for i in range(len(impar)):
        print(f'impar[{i}] = {impar[i]}')
    for i in range(len(par)):
        print(f'par[{i}] = {par[i]}')

main()