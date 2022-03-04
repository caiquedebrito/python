from time import sleep

def sorteia(lista):
	from random import randint
	print('Sorteando 5 números:', end=' ')
	for v in range(0,5):
		lista.append(randint(1, 11))
		print(lista[v], end=' ', flush=True)
		sleep(0.5)


def somaPar(lista):
	totP = 0
	for n in lista:
		if n % 2 == 0:
			totP += n
	print(f'\nSomando os valores pares em {números} temos {totP}')
	

números = list()
input('Tecle enter: ')
sorteia(números)
somaPar(números)
