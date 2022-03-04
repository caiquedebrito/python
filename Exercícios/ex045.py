from random import randint
cpu = randint(1,3)
if cpu == 1:
	cpu = 'pedra'
elif cpu == 2:
	cpu = 'papel'
elif cpu == 3:
	cpu = 'tesoura'
print('=-'*30)
print(f'{"PEDRA, PAPEL E TESOURA":^60}')
print('-='*30)
player = input('Voce escolhe pedra, papel ou tesoura? ').lower().strip()

print(f'CPU:  {cpu}')
print(f'VOCE: {player}')

if cpu == player:
	print('EMPATE')
elif 'pedra' in player:
	if 'tesoura' in cpu:
		print('VOCE GANHOU')
	elif 'papel' in cpu:
		print('VOCE PERDEU')
elif 'papel' in player:
	if 'pedra' in cpu:
		print('VOCE GANHOU')
	elif 'tesoura' in cpu:
		print('VOCE PERDEU')
elif 'tesoura' in player:
	if 'pedra' in cpu:
		print('VOCE PERDEU')
	elif 'papel' in cpu:
		print('VOCE GANHOU')
else:
	print('OPCAO INVALIDA. TENTE NOVAMENTE.')