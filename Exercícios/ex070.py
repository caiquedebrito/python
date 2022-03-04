print('-'*60)
print(f'{"LOJA DE PRODUTOS":^60}')
print('-'*60)

total = mais_mil = 0
mais_barato = 0
produto_barato = ''
while True:
	produto = str(input('Nome do produto: '))
	preço = float(input('Preço: R$'))
	
	#Verifica o produto mais barato
	if total == 0:
		mais_barato = preço
		produto_barato = produto
	elif preço < mais_barato:
		mais_barato = preço
		produto_barato = produto
		
	#Verifica o total da compra e quantos produtos custam mais de 1000
	total += preço
	if preço > 1000:
		mais_mil += 1
		
	r = str(input('Quer continuar ? [s/n] '))
	if r == 'n':
		break
		
print(f'O preço total da compra foi de R${total:.2f}')
print(f'{mais_mil} produtos custam mais de R$1000')
print(f'O produto mais barato foi o/a {produto_barato}')
