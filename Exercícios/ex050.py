total_pares = 0
for i in range(6):
	n = int(input(f'Digite o {i+1}° número: '))
	if n % 2 == 0:
		total_pares += n
print(f'A soma dos números pares foi {total_pares}.')