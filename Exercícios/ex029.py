v = int(input('Qual a velocidade do carro [km/h]? '))
if v > 80:
	print('LIMITE DE VELOCIDADE : 80 Km/h')
	print('Você foi multado por excesso de velocidade.')
	m = (v - 80) * 7
	print(f'Valor da multa : R$ {m:.2f}')
	