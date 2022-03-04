chave = 'não'
while chave != 'ok':
	sexo = input('SEXO [M/F]: ').upper().strip()
	if sexo[0] == 'M' or sexo[0] == 'F':
		chave = 'ok'
	else:
		print('Por favor, digite o seu sexo.')
	
	