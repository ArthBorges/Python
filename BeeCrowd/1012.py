def triangulo(a, c):
    tri = a * c / 2
    return tri

def circulo(c):
    area = 3.14159 * c**2
    return area

def trapezio(a, b, c):
    trap = (a + b)* c / 2
    return trap

def quadrado(b):
    quad = b**2
    return quad

def retangulo(a, b):
    ret = a * b
    return ret

def main():
    a, b, c = map(float, input().split(" "))
    triret = triangulo(a, c)
    circ = circulo(c)
    trap = trapezio(a, b, c)
    quad = quadrado(b)
    ret = retangulo(a, b)
    print(f'TRIANGULO: {triret:.3f}')
    print(f'CIRCULO: {circ:.3f}')
    print(f'TRAPEZIO: {trap:.3f}')
    print(f'QUADRADO: {quad:.3f}')
    print(f'RETANGULO: {ret:.3f}')

main()