def encontra_null(l: list):

	for i in range(len(l)):
		if l[i] <= 0:
			l[i] = 1
			print(f'X[{i}] = {l[i]}')
		else:
			print(f'X[{i}] = {l[i]}')

def main():
	l = [] 
	cont = 0
	while cont < 10:
		num = int(input())
		l.append(num)
		cont += 1

	encontra_null(l)

main()