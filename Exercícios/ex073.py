brasileirao = ('2021BR ', 'Bragantino', 'Bahia', 'Ceará SC', 'Fortaleza', 'Athletico-PR', 'Flamengo', 'Atlético-GO', 'Sport Recife', 'Juventude', 'Cuiabá', 'Internacional', 'São Paulo', 'Fluminense', 'Grêmio', 'Atlético-MG', 'América-MG', 'Palmeiras', 'Corinthians', 'Chapecoense', 'Santos')

for t in range(1,21):
	print(t,'° 	',brasileirao[t])
print('\n')
print('='*60)

print('Os cinco primeiros colocados são :')
for n in range(1,6):
	print(brasileirao[n],end='. ')
	
print('\n')
print('='*60)

print('\n Os quatros últimos colocados do Brasileirão são :')
for n in range(17,21):
	print(brasileirao[n], '.', end=' ')
	
print('\n')
print('='*60)

print('Os times em ordem alfabética :')
print(sorted(brasileirao))

print('\n')
print('='*60)
c = brasileirao.index('Chapecoense')
print(f'A Chapecoense está na {c}° posição')
	