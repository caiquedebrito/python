dict = dict()
lista = list()
while True:
	dict['Nome'] = str(input('Nome: '))
	dict['Idade'] = int(input('Idade: '))
	dict['Sexo'] = str(input('Sexo: ')).upper()[0]
	lista.append(dict.copy())
	
	resp = str(input('Quer continuar? [s/n] '))
	if resp in 'nN':
		break

t = m = 0
mulher = []
ame = []
for p in lista:
	t += p['Idade']
	if p['Sexo'] == 'F':
		mulher.append(p['Nome'])
m = t / len(lista)
for p in lista:
	if p['Idade'] > m:
		ame.append(p['Nome'])

print(f'Foram cadastradas {len(lista)} pessoas.')
print(f'A média de idade foi {m:.2f} anos.')
print(f'As mulheres cadastradas: ', end='' )
for m in mulher:
	print(m)
print(f'As pessoas acima da média: ', end='')
for p in ame:
	print(p)
