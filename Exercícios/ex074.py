from random import randint

maior = 0
n_sorteados = (randint(1,20), randint(1,20), randint(1,20), randint(1,20), randint(1,20))

print(f'Os números sorteados foram {n_sorteados}')

for n in range(0,5):
	if n_sorteados[n] > maior:
		maior = n_sorteados[n]
		
print(f'O maior valor sorteado foi {maior}')
menor = maior

for n in range(0,5):
	if n_sorteados[n] < menor:
		menor = n_sorteados[n]
		
print(f'O menor valor sorteado foi {menor}')