import random

random.seed() # inicializa o gerador de números

for i in range(int(input())):
	# gera um float entre -50 e 50 e arredonda com 1 casa decimal
	print(round(random.uniform(-50, 50), 1))
	
	# gera um int entre -50 e 50
	#print(random.randint(-50, 50))
