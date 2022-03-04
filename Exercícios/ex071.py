from time import sleep

print('= '*30)
print(f'{"BANCO BRB":^60}')
print(' ='*30)

print('carregando...')
sleep(0.5)
valor = int(input('Valor a ser sacado (Somente valor inteiro): R$'))

if valor >= 50:
	if valor%50 == 0:
		cinquenta = valor//50
		print(f'Total de {cinquenta} notas de R$50')
	else:
		c
	