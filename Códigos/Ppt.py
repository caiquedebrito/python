from emoji import emojize
from random import randint


def Jogo(a):
	playr = a

while True:
	print(emojize(f'''{'Pedra :punch: , Papel :wave: e Tesoura :v:':^60}\n
Você esvolhe pedra , papel ou tesoura !? 
Tecle:
[1] para escolher pedra. :punch:
[2] para papel. :wave:
[3] para tesoura. :v:
[4] para sair''', use_aliases=True))
	player = int(input())
	cpu = randint(1,3)

	print(f'Player: ', end='')
	if player == 1:
		print(emojize(':punch:', use_aliases=True))
	elif player == 2:
		print(emojize(':wave:', use_aliases=True))
	elif player == 3:
		print(emojize(':v:', use_aliases=True))
	elif player == 4:
		break
	else:
		print('Jogada invalida.')

	print(f'Cpu: ', end='')
	if cpu == 1:
		print(emojize(':punch:', use_aliases=True))
	elif cpu == 2:
		print(emojize(':wave:', use_aliases=True))
	elif cpu == 3:
		print(emojize(':v:', use_aliases=True))