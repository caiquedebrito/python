km = float(input('Quantos km(quilômetros) tem a sua viagem ? '))
if km <= 200:
	p = km * 0.45
	print('Viagem Curta.')
	print(f'A sua viagem vai custar R$ {p:.2f}')
else:
	p = km * 0.50
	print('Viagem Longa.')
	print(f'A sua viagem vai custar R$ {p:.2f}')