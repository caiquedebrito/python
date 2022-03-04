def leiaInt(msg):
	
	while True:
		try:
			inte = int(input(msg))
		except:
			print('\033[31mERRO: Digite uma opção válida.\033[m')
		else:
			return inte
			break


def linha():
	return '='*60
	
	
def cabeçalho(txt):
	print(linha())
	print(txt.center(60))
	print(linha())
	
	
def menu(lista):
	cabeçalho('Menu principal')
	c = 1
	for i in lista:
		print(f'{c} - {i}')
		c += 1
		