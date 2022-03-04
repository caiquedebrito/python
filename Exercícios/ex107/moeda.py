def dobro(preço):
	res = preço * 2
	return res
	

def metade(preço):
	res = preço / 2
	return res
	
	
def aumentar(preço, taxa):
	res = preço + (taxa / 100 * preço)
	return res
	
	 
def diminuir(preço, taxa):
	res = preço - (taxa / 100 * preço)
	return res