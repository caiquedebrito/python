lista = list()
pos5 = list()
while True:
	n = int(input('Digite um valor : '))
	lista.append(n)
	c = str(input('Quer continuar ? s/n '))
	if c == 'n':
		break
lista.sort(reverse = True)
for p,v in enumerate(lista):
	if v == 5 :
		pos5.append(p)
print(f'Foram digitados {len(lista)} valores')
print(f'Os valores em ordem decrescente são {lista}')
for p,v in enumerate(lista):
	if v == 5:
		print(f'O valor 5 faz parte da lista na(s) posição(ões) {pos5}.')
		break
else:
	print('O valor 5 não faz parte da lista.')
