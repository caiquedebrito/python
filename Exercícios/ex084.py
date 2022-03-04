pessoas = []
dados = []
mai = men = 0

while True:
	pessoas.append(str(input('Nome: ')))
	pessoas.append(float(input('Peso: ')))
	if len(dados) == 0:
		mai = men = pessoas[1]
	else:
		if pessoas[1] > mai:
			mai = pessoas[1]
		if pessoas[1] < men:
			men = pessoas[1]
	dados.append(pessoas[:])
	pessoas.clear()
	
	resp = str(input('Quer continuar? '))
	if resp in 'nN':
		break
		
print(f'Os dados foram: {dados}')
print(f'Ao todo, foram cadastrada {len(dados)} pessoas.')
print(f'O maior peso foi {mai}. Peso de ', end='')
for p in dados:
	if p[1] == mai:
		print(p[0])
print(f'O menor peso foi {men}. Peso de ', end='')
for p in dados:
	if p[1] == men:
		print(p[0])
