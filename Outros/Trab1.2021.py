v, n, m = map(int, input().split(' '))

while v != 0 or n != 0 or m != 0:

    grupoN = (n - 1) % 100 // 4 + 1
    grupoM = (m - 1) % 100 // 4 + 1

    if n % 10000 == m % 10000:
         premio = v * 3000
    elif n % 1000 == m % 1000:
         premio = v * 500
    elif n % 100 == m % 100:
         premio = v * 50
    elif grupoN == grupoM:
         premio = v * 16
    else:
         premio = 0

    print("%d %dx100 %dx10 %dx1" % (premio, premio / 100, (premio / 10) % 10, premio % 10))
    print(f'{premio} {(premio/100)}x100 {(premio/10)%10}x10 {premio%10}x1')
    v, n, m = map(int, input().split(' '))