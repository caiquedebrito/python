matriz = [[],[],[]]
for i in range(3):
	for j in range(3):
		n = int(input(f'Digite um valor para a posição[{i,j}]: '))
		matriz[i].append(n)
		
for v in matriz:
	for c in range(3):
		print(f'[{v[c]}]', end=' ')
	print('\n')