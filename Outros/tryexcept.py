# Beecrowd 1234 - Sentença Dançante

def main():
	while True:
		# Python, tente ler a entrada, se acabar o arquivo de entrada
		# (EOFError), sai do while com um break:
		try:
			sentenca = input()
			print(sentenca)
		except EOFError:
			break

main()