from random import randint
from operator import itemgetter
from time import sleep

ranking = []
jogadores = {
'Jogador1' : randint(1,6),
'Jogador2' : randint(1,6),
'Jogador3' : randint(1,6),
'Jogador4' : randint(1,6)}

print('Valores sorteados: ')
for k, v in jogadores.items():
	sleep(1)
	print(f'{"":>5}O {k} tirou {v}.')
			
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print('RANKING')
for i, v in enumerate(ranking):
	sleep(1)
	print(f'{i+1}° Lugar: {v[0]} = {v[1]}')