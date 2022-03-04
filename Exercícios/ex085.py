valores = [[],[]]
for c in range(7):
	v = int(input(f'Digite o {c+1}° valor: '))
	if v % 2 ==0:
		valores[0].append(v)
	else:
		valores[1].append(v)
print('Os valores pares são: ', sorted(valores[0]))
print('Os valores ímpares são: ', sorted(valores[1]))