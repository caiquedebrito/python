t = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def tabuleiro():
	print(f'''
	  {t[0][0]}  ||  {t[0][1]}  ||  {t[0][2]}
	===================
	  {t[1][0]}  ||  {t[1][1]}  ||  {t[1][2]}
	===================
	  {t[2][0]}  ||  {t[2][1]}  ||  {t[2][2]}
''')


#Verifica se a opção do usuário é válida 
def opção(posição, xo):
	for linha in t:
		for c in range(3):
			if linha[c] == posição:
				#X em vermelho 
				if xo == 'X':
					linha[c] = f'\033[31;1m{xo}\033[m'
				#O em verde
				elif xo == 'O':
					linha[c] = f'\033[32;1m{xo}\033[m'
				return True
				

def ganhador():
	#Linhas
	for linha in t:
		if linha[0] == linha[1] and linha[1] == linha[2]:
			return True
	#Colunas
	for c in range(3):
		if t[0][c] == t[1][c] and t[1][c] == t[2][c]:
			return True
	#Diagonais
	if t[0][0] == t[1][1] and t[1][1] == t[2][2]:
		return True
	elif t[0][2] == t[1][1] and t[1][1] == t[2][0]:
		return True
		

def empate():
	total = 0
	t1 = [[1,2,3],[4,5,6],[7,8,9]]
	#Empate quando os dois tabuleiros são totalmente difirente
	for c in range(3):
		for l in range(3):
			#Verifica se as casas são diferentes
			if t1[c][l] != t[c][l]:
				total += 1
	#Se for verdade o jogo empata
	if total == 9:
		return True
		
		
def um_x_um():
	#Escolha de X ou O
	while True:
		jogador1 = str(input('Jogador1 X ou O: ')).upper()
		if jogador1 == 'X':
			jogador2 = 'O'
			print('Jogador2: O')
			break
		elif jogador1 == 'O':
			jogador2 = 'X'
			print('Jogador2 X')
			break
	tabuleiro()
	
	#Jogo	
	while True:
		#Jogador1
		key = Ganhador = Empate = False
		while True:
			try:
				posição = int(input(f'Jogador1 [{jogador1}]: '))
			except:
				print('Opção inválida.')
			else:
				key = opção(posição, jogador1)
				tabuleiro()
				Empate = empate()
				if key:
					Ganhador = ganhador()
					break
				else:
					print('Espaço já ocupado.')
		if Ganhador:
			print('O jogador1 venceu!')
			break
		if Empate:
			print('Empate!')
			break	
		#Jogador2	
		key = False
		while True:
			try:
				posição = int(input(f'Jogador2 [{jogador2}]: '))
			except:
				print('Opção inválida.')
			else:
				key = opção(posição, jogador2)
				tabuleiro()
				if key:
					Ganhador = ganhador()
					break
				else:
					print('Espaço já ocupado.')
		if Ganhador:
			print('O jogador2 venceu!')
			break
				
		