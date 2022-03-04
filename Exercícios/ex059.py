n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
key = 0
while key == 0:
	print('''\nO Que você quer fazer agora:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa ''')
	opção = int(input('Opção: '))
	if opção == 1:
		print(f'A soma entre {n1} e {n2} é {n1+n2}.')
	elif opção == 2:
		print(f'O produto entre {n1} e {n2} é {n1*n2}.')
	elif opção == 3:
		if n1 > n2:
			print(f'O maior número é o {n1}.')
		else:
			print(f'O maior número é o {n2}.')
	elif opção == 4:
		n1 = int(input('Digite um número: '))
		n2 = int(input('Digite outro número: '))
	elif opção == 5:
		key = 1
		