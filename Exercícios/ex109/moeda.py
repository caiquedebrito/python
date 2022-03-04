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
	