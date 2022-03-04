from random import randint
from time import sleep

palpites = list()
palpite = list()
print('='*60)
print(f'{"MEGA SENA":^60}')
print('='*60)

jogos = int(input('Quantas palpites você vai querer? '))
print('Gerando os valores...')
sleep(1)

for jogo in range(jogos):
	while len(palpite) != 6:
		n = randint(1, 60)
		if n not in palpite:
			palpite.append(n)
	palpites.append(palpite[:])
	palpite.clear()
	
for p, j in enumerate(palpites):
	print(f'Jogo {p+1} : {j}')
	sleep(1)