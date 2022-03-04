matriz = [[],[],[]]
somap = tot3c = maior2l = 0
for i in range(3):
	for j in range(3):
		n = int(input(f'Digite um valor para a posição[{i,j}]: '))
		matriz[i].append(n)
	
print('='*40)
for v in matriz:
	tot3c += v[2]
	for c in range(3):
		print(f'[{v[c]}]', end=' ')
		if v[c] % 2 == 0:
			somap += v[c]
		if matriz[1]:
			if v[c] > maior2l:
				maior2l = v[c]
			
	print('\n')
print('='*40)

print(f'A soma dos valores pares é {somap}.')
print(f'A soma dos valores da terceira coluna é {tot3c}.')
print(f'O maior valor da 2 linha foi {maior2l}')
