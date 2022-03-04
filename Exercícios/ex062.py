a1 = float(input('Primeiro termo: '))
r = float(input('Razão: '))
cont = 0
while cont < 10:
	print(a1, end=' ')
	a1 += r
	cont += 1
cont = 0
v = int(input('\nVocê quer ver mais quantos termos? '))
while cont < v:
	print(a1)
	a1 += r
	cont += 1