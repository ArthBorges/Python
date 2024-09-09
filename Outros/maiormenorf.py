def encontraMaiorMenor(l: list) -> int:
	maior = menor = l[0]

	for i in range(1, len(l)):
		if l[i] > maior:
			maior = l[i]

		if l[i] < menor:
			menor = l[i]

	return maior, menor

def main():
	n = int(input())

	l = [] # lista vazia
	for i in range(n):
		num = int(input())
		l.append(num)          # adiciona no final da lista

	maior, menor = encontraMaiorMenor(l)

	print(f"Maior = {maior}\nMenor = {menor}")

main()