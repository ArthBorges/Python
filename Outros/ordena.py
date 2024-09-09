# ordenação por inserção ou insertion sort
def ordena(l: list):
	for i in range(1, len(l)):
		pivo = l[i]
		j = i - 1
		while j >= 0 and l[j] > pivo:
			l[j + 1] = l[j]
			j -= 1
		l[j + 1] = pivo
		#print(l)

def main():
	l = list(map(int, input().split()))

	print(l)
	ordena(l)
	print(l)

main()