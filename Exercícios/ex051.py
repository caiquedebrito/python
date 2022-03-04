print(f'{"POGRESSÃO ARITMÉTICA":^60}\n')
a1 = float(input('Digite o primeiro termo da PA: '))
razão = float(input('Agora digite a razão: '))
for c in range(10):
	print(f'{a1}', end=' ')
	a1 += razão