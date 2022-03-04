ma_peso = 0 	#maior peso
me_peso = 0	 #menor peso
n_ma = n_me = 0 #Posição da pessoa mais pesada e a menos pesada

for c in range(5):
	peso = float(input(f'Peso da {c+1}° pessoa (Kg): '))
	if me_peso == 0:
		me_peso = peso
	if peso > ma_peso:
		ma_peso = peso
		n_ma = c
	elif peso < me_peso:
		me_peso = peso
		n_me = c
	
print(f'O maior peso foi {ma_peso} da {n_ma+1}° pessoa.')
print(f'O menor peso foi {me_peso} da {n_me+1}° pessoa.')