def leiaDinheiro(msg):
	while True:
		dado = input(msg).replace(',', '.').strip()
		if dado.isalpha() or dado == '' :
			print(f'\033[31mErro: "{dado}" é um preço inválido.\033[m')
		else:
			break
	return float(dado)