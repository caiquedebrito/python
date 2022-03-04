jogadores = []
jogador = {}
gols = []

while True:
	Gols = Total = 0
	print('--'*10)
	jogador['Nome'] = str(input('Nome: '))
	partidas = int(input('Quantas partidas jogadas? '))
	for p in range(partidas):
		Gols = int(input(f'    Quantos gols na {p+1}° partida? '))
		Total += Gols
		gols.append(Gols)
	jogador['Gols'] = gols[:]
	jogador['Total'] = Total
	gols.clear()
	jogadores.append(jogador.copy())
	resp = str(input('Quer continuar?[S/N] ')).upper()
	if resp == 'N':
		break
		
print('=-'*30)
print('Cod', end=' ')
for i in jogador.keys():
	print(f'{i:<15}', end=' ')
print()
print('-='*30)
for k, v in enumerate(jogadores):
	print(f'{k:>3} ', end=' ')
	for d in v.values():
		print(f'{str(d):<15}', end=' ')
	print()
print('=-'* 30)

while True:
	print('\n')
	cod = int(input('Mostrar informaçoes de qual jogador? (999 para parar) Cod: '))
	if cod == 999:
		break
	elif cod >= len(jogadores) or cod < 0:
		print(f'Erro! Não existe jogador com o código {cod} !')
	else:
		print(f'Acessando informações do jogador {jogadores[cod]["Nome"]}...')
		print(f' Total de {jogadores[cod]["Total"]} gols.')
		for p, g in enumerate(jogadores[cod]['Gols']):
			print(f'  Na {p+1}° partida fez {g} gols.')
		
print('>>> Finalizando...')