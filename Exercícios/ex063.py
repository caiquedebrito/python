n = int(input('Digite um número inteiro: '))
a, b = 0, 1
cont = 0
while cont < n:
	print(a)
	a, b = b, a+b
	cont += 1