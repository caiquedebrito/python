lista = []
while True:
	lista.append(int(input('Digite um valor : ')))
	r = input('Quer continuar ? [s/n] ')
	if r == 'n':
		break
#print('Os valores digitados foram :')
#print(lista)
for c, v in enumerate(lista):
	print(f'Na posição {c} foi digitado o valor {v}!')