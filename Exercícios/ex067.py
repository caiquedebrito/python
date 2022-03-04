while True:
	print('-'*40)
	print('Quer ver a tabuada de qual valor? ')
	print('-'*40)
	n = int(input())
	if n <= 0:
		break
	else:
		for c in range(1,11):
			print(f'{"":>20}{n} x {c}  =  {n*c}')
print('Programa encerrado.')