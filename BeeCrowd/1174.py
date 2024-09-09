def encontra_null(l: list):

	for i in range(len(l)):
		if l[i] <= 10:
			print(f'A[{i}] = {l[i]:.1f}')

def main():
	l = [] 
	cont = 0
	while cont < 100:
		num = float(input())
		l.append(num)
		cont += 1

	encontra_null(l)

main()