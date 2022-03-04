def dobro(preço=0):
	res = preço * 2
	return res
	

def metade(preço=0):
	res = preço / 2
	return res
	
	
def aumentar(preço=0, taxa=0):
	res = preço + (taxa / 100 * preço)
	return res
	
	 
def diminuir(preço=0, taxa=0):
	res = preço - (taxa / 100 * preço)
	return res
	
	
def moeda(cash=0, moeda='R$'):
	cash = f'{cash:.2f}'
	cash = str(cash)
	tam = len(cash)
	formatação = moeda
	for l in range(tam):
		if cash[l] == '.':
			formatação += ','
		else:
			formatação += cash[l]
	return formatação