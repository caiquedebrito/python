print(f'{" CAIXA ":=^60}')
preco = float(input('Qual o preco do produto? R$'))
print('''FORMAS DE PAGAMENTO
[1] A vista dinheiro/cheque: 10% de desconto
[2] A vista no cartao: 5% de desconto
[3] Em ate 2x no cartao: preco normal
[4] 3x ou mais no cartao: 20% de juros''')
o = int(input('SUA OPCAO: '))
if o == 1:
	valor = preco * 90/100
elif o == 2:
	valor = preco * 95/100
elif o == 3:
	valor = preco
	parcela = valor/2
	print(f'Sua compra sera parcelada em 2x de R${parcela:.2f} SEM JUROS')
elif o == 4:
	vezes = int(input('Em quantas a parcelas? '))
	valor = 120/100*preco
	parcela = valor/vezes
	print(f'Sua compra sera parcelada em {vezes}x de R${parcela:.2f} COM JUROS')
	
print(f'Sua compra de R${preco:.2f} vai custar R${valor:.2f}')