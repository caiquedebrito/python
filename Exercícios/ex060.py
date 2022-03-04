n = int(input('Digite um número: '))
fatorial = 1
print(f'O fatorial de {n} é :')
while n > 0:
	print(n,end=' ')
	if n > 1:
		print('x', end=' ')
	n -= 1
	fatorial *= n
print('=', fatorial)