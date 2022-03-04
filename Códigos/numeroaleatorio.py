import random
v = int(input('Quantas vezes voce quer tentar ?'))
for c in range(1,v+1):
	ale = random.randint(1,10)
	res = int(input('Digite um numero entre 1 e 10 : '))
	if res == ale:
		print('PARABENS!! Voce acertou o numero.')
	else:
		print('Nao foi dessa vez tente outra.')
	print('Numero sorteado foi \033[31m{}\033[m'.format(ale))
	print('Sua resposta :  {}'.format(res))