numeros = list()
while True:
	n = int(input('Digite um valor : '))
	if n not in numeros:
		numeros.append(n)
		print('Valor adicionado com sucesso.')
	else:
		print('Valor duplicado. Não vou adicionar.')
	r = input('Digite qualquer tecla para continuar ou digite (n) para finalizar : ')
	if r == 'n':
		break
		
print('='*50)
numeros.sort()
print(f'Voce digitou os valores {numeros}.')
