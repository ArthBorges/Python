def media(x, y):
    x *= 3.5
    y *= 7.5
    med = (x + y) / 11
    return med

def main():
    a = float(input())
    b = float(input())
    med = media(a, b)
    print(f'MEDIA = {med:.5f}')

main()