nome = str(input('Qual o seu nome ? '))
valor_casa = int(input('Qual o valor da casa que você quer comprar ? R$'))
salario = int(input(f'Sr(a). {nome} , quanto você recebe de salário ? R$'))
anos = int(input(f'{nome}, em quantos anos você vai pagar a casa ? '))
mensal = valor_casa / (anos*12)
print(f'\nUma casa que custa R${valor_casa:.2f}, paga em {anos} anos, terá uma mensalidade de R${mensal:.2f}')
if mensal > (30/100) * salario:
	print('Infelizmente você não pode financiar essa casa!')