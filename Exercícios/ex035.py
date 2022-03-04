print('-=-'*20)
print(f'{"CONDIÇÃO DE EXISTÊNCIA DE UM TRIÂNGULO":^60}')
print('-=-'*20)
r1 = int(input('Qual o tamanho da primeira reta ? '))
r2 = int(input('Qual o tamanho da segunda reta ? '))
r3 = int(input('Qual o tamanho da terceira reta ? '))
if r1 + r2 > r3 and r3 + r1 > r2 and r2 + r3 > r1:
	print('Sim! As retas formam um triângulo.')
else: 
	print('Não! As retas não formam um triângulo.')