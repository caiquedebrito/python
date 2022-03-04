from random import randint
cpu = randint(1,10)
print('PENSEI NUM NÚMERO ENTRE 1 E 10. TENTE ADIVINHA-LO')
n = erros = 0
while n == 0:
	player = int(input('\nEm que número eu pensei : '))
	if player == cpu:
		n = 1
	else:
		print('ERROU!! TENTE OUTRO!')
		print(f'Não é o número {player}')
	erros += 1
print(f'''\nPARABÉNS VOCÊ ACERTOU!
Pensei no número {cpu}.
Você acertou em {erros} tentativas.''')