def calcula(l: list, n: int):    
    
    for i in range(0, 10):
        l.append(n)   
        print(f'N[{i}] = {n}')
        n *= 2

def main():
    l = []
    n = int(input())
    calcula(l, n)

main()