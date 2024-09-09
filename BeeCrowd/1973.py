def rouba_carneiros(n, carneiros):
    sitios = 0
    c_roubados = 0
    
    for i in range(n):
        if carneiros[i] % 2 == 1:
            if carneiros[i] > 0:
                carneiros[i] -= 1
                c_roubados += 1
                sitios += 1
                if i < n - 1:
                    i += 1
            else:
                break
        else:
            if carneiros[i] > 0:
                carneiros[i] -= 1
                c_roubados += 1
                sitios += 1
                if i > 0:
                    i -= 1
            else:
                break
    
    c_restantes = 0
    for i in range(len(carneiros)):
        c_restantes += carneiros[i]
    
    return sitios, c_restantes

def main():
    n = int(input())
    carneiros = list(map(int, input().split()))
    sitios, c_restantes = rouba_carneiros(n, carneiros)
    print(sitios, c_restantes)

main()