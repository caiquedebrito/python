def fatorial(n, show=False):
	"""-> Calcula o fatorial de um número
	:param n: O número a ser calculado
	:param show: (Opicional) Mostrar ou não a conta
	:return: O valor do fatorial de um número
	"""
	f = 1
	print('-'*30)
	if show == True:
		for v in range(n, 0, -1):
			if v < n:
				print('x',end=' ')
			print(v, end=' ')
			f *= v
		print(f'=', end=' ')
		return f
	else:
		for v in range(n, 0, -1):
			f *= v
		return f
		
	
print(fatorial(10, True))
print(help(fatorial))