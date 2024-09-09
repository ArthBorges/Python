def troca_num(l: list):
	lista_contraria = []
	for i in range(len(l)):
		num = l.pop()
		lista_contraria.append(num)
		print(f'N[{i}] = {lista_contraria[i]}')


def main():
	l = [] 
	cont = 0
	while cont < 20:
		num = int(input())
		l.append(num)
		cont += 1

	troca_num(l)

main()