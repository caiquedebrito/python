def dobro(preço=0, key=False):
	res = preço * 2
	return res if key is False else moeda(res)
	

def metade(preço=0, key=False):
	res = preço / 2
	return res if key is False else moeda(res)
	
	
def aumentar(preço=0, taxa=0, key=False):
	res = preço + (taxa / 100 * preço)
	return res if key is False else moeda(res)
	
	 
def diminuir(preço=0, taxa=0, key=False):
	res = preço - (taxa / 100 * preço)
	return res if key is False else moeda(res)
	
	
def moeda(preço=0, moeda='R$'):
	return f'{moeda}{preço:.2f}'.replace('.', ',')
	

def resumo(preço, aum, dim):
	print('--'*30)
	print(f'{"Resumo do Valor":^60}')
	print('--'*30)
	print(f'''
	Preço analisado: \t{moeda(preço)}
	Dobro do preço:  \t{dobro(preço, True)}
	Metade do preço: \t{metade(preço, True)}
	{aum}% de Aumento:  \t{aumentar(preço, aum, True)}
	{dim}% de Desconto: \t{diminuir(preço, dim, True)}''')
	print('--'*30)