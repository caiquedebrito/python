ano = int(input('Escolha qualquer ano : '))
if ano % 4 == 0:
	print(f'O ano de {ano} é um ano bissexto.')
else:
	print(f'{ano} não é bissexto.')