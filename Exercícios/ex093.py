info = dict()
gols = []
totG = 0
info['Nome'] = str(input('Nome: '))
p = int(input(f'Quantas partidas {info["Nome"]} jogou? '))
for c in range(p):
	gols.append(int(input(f'Quantos gols foi marcado na {c+1}° partida? ')))

for g in gols:
	totG += g
	
info['Gols'] = gols
info['Total'] = totG

print(info)
for k, v in info.items():
	print(f'O campo {k} tem valor {v}.')
	
print(f'O jogador {info["Nome"]} jogou {p} partidas')
for c in range(p):
	print(f'{"":>5}=> Na partida {c+1}, fez {info["Gols"][c]} gols')
	
print(f'Foi um total de {info["Total"]}.')