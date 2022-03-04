mais_dezoito = homens = mm_vinte = 0
print('-'*20, end='')
print('CADASTRANDO PESSOAS', end='')
print('-'*20)

while True:
	while True:
		idade = input('IDADE: ')
		if not idade.isnumeric():
			continue
		else:
			idade = int(idade)
			if idade > 18:
				mais_dezoito += 1
			break
			
	while True:
		sexo = input('Sexo [M/F]: ').upper().strip()[0]
		if sexo in 'FM':
			sexo = str(sexo)
			if sexo == 'M':
				homens += 1
			elif sexo == 'F' and idade < 20:
				mm_vinte += 1
			break
		else:
			continue
			
	while True:
		cont = str(input('Quer continuar? [S/N] ')).strip()
		if cont in 'SNsn':
			break
	if cont in 'nN':
		break
	
		
print(f'{mais_dezoito} pessoas têm mais de 18 anos.')
print(f'Foram cadastrado {homens} Homens.')
print(f'{mm_vinte} Mulheres tem menos de 20 anos.')