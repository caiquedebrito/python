
numeros = (int(input('Digite o primeiro número : ')),
 				int(input('Digite outro : ')),
 				int(input('Digite mais um : ')), 					 int(input('Digite o último : ')))
		
print(f'Voce digitou os valores {numeros}.')
print(f'O número 9 foi digitado {numeros.count(9)} vezes.')

if 3 in numeros:
	print(f'O valor 3 foi digitado na {numeros.index(3)+1}° posição.')
else:
	print('O valor 3 não foi digitado em nenhuma posição.')
	
print(f'Os números pares foram :', end= ' ' )
for n in numeros:
	if n % 2 == 0:
		print(n, end=',')