from config import *
from random import randint


t = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def x_ou_o():
	while True:
		#Escolha de X ou O
		op = str(input('Você escolhe X ou O? ')).upper()
		if op == 'X' or op == 'O':
			return op
		else:
			print('Escolha X ou O.')


def verificar_linhas(peça):
#	tab = [[1,2,3], [4,5,6], [7,8,9]]
	key = False
	#Adiciona cor a peça
	if peça == 'X':
		peça = f'\033[31;1m{peça}\033[m'
	else:
		peça = f'\033[32;1m{peça}\033[m'
	#Variáveis de controles
	v = n = 0
	for i in range(3):
		for j in range(3):
			if peça == t[i][j]:
				v += 1
			else:
				n += 1
		if v == 2 and n == 1:
			for i in range(3):
				for j in range(3):
					if t[i][j] != peça:
						t[i][j] = peça
						key = True
						break
				if key:
					break
			if key:
				break
		if key:
			break


def sorteio():
	n = randint(1, 21)
	if n % 2 == 0:
		return True
	else:
		return False
		
		
def boot(b, quem):
	from time import sleep
	print('Minha vez...')
	sleep(2)
	v = verificar_linhas(b)
	if v:
		return True
	else:
		while True:
			o = randint(1,9)
			key = opção(o, b)
			#tabuleiro()
			if key:
				break
	
	
#Jogador x Bot
def player_x_bot(jogador):
#	tabuleiro()
	while True:
		try:
			pos = int(input(f'{jogador} em qual posição? '))
		except:
			print('Opção inválida.')
		else:
			key = opção(pos, jogador)
			#tabuleiro()
			if key:
				break
			else:
				print('Espaço ocupado ou inexistente.')
						
			
def jogo():	
	jogador = x_ou_o()
	if jogador == 'X':
		b = 'O'
	elif jogador == 'O':
		b = 'X'
	vez = sorteio()
	Ganhador = Empate = False
	tabuleiro()
	if vez:
		while True:
			#tabuleiro()
			player_x_bot(jogador)
			Ganhador = ganhador()
			tabuleiro()
			if Ganhador:
				print('Você ganhou!')
				break
			Empate = empate()
			if Empate:
				print('Empate!')
				break
			boot(b, vez)
			tabuleiro()
			Ganhador = ganhador()
			if Ganhador:
				print('Você perdeu!')
				break
	else:
		while True:
			#tabuleiro()
			boot(b, vez)
			tabuleiro()
			Ganhador = ganhador()
			if Ganhador:
				print('Você perdeu!')
				break
			Empate = empate()
			if Empate:
				print('Empate!')
				break
			player_x_bot(jogador)
			tabuleiro()
			Ganhador = ganhador()
			if Ganhador:
				print('Você ganhou!')
				break
		
		
		
