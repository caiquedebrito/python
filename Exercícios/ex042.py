l1 = float(input('Comprimento do lado 1: '))
l2 = float(input('Comprimento do lado 2: '))
l3 = float(input('Comprimento do lado 3: '))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
	print('E possivel formar um triangulo: ')
	if l1 == l2 and l2 == l3:
		print('EQUILATERO')
	elif l1 == l2 or l1 == l3 or l2 == l3:
		print('ISOSCELES')
	else:
		print('ESCALENO')
else:
	print('Nao e possivel formar um triangulo: ')
	
