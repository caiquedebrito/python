numeros = list()
pares = []
impares = []

while True:
	numeros.append(int(input('Digite um número : ')))
	r = str(input('Quer continuar ? [s/n] '))
	if r == 'n':
		break
		
for n in numeros:
	if n % 2 == 0:
		pares.append(n)
	else:
		impares.append(n)
		
print('<='*60)
print(f'A lista completa é {numeros}.')
print(f'A lista com pares é {pares}.')
print(f'A lista com ímpares é {impares}.')