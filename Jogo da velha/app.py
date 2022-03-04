from config import *
from bot import *
from os import system

resp = ''
#Modo de Jogo
print('''JOGO DA VELHA

[1] - Jogar Com Um Amigo
[2] - Jogar Com Um Bot
[3] - Sair
	''')
	
#Escolha da Opção 
while True:
	try:
		Opção = int(input('Opção: '))
	except:
		print('Opção inválida.')
	else:
		if Opção == 1:
			um_x_um()
			break
		elif Opção == 2:
			jogo()
			break
		elif Opção == 3:
			print('Fim!')
			break
		else:
			print('Opção inválida.')
	

					