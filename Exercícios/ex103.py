def ficha(jogador='<desconhecido>', gol=0):	
	print(f'O jogador {jogador} fez {gol} gol(s) no campeonato.')
	
	
j = str(input('Nome do jogador: '))
g = str(input('Gols : '))
if g.isnumeric():
	g = int(g)
else:
	g = 0
if j.strip() == '':
	ficha(gol=g)
else:
	ficha(j,g)