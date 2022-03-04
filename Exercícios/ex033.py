n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
n3 = int(input('Digite mais um: '))
print(f'Entre {n1}, {n2}, {n3}')
if n1 > n2 and n1 > n3:
	print(f'O maior número foi {n1}')
if n2 > n1 and n2 > n3:
	print(f'O maior número foi {n2}')
if n3 > n1 and n3 > n2:
	print(f'O maior número foi {n3}')
if n1 < n2 and n1 < n3:
	print(f'O menor número foi {n1}')
if n2 < n1 and n2 < n3:
	print(f'O menor número foi {n2}')
if n3 < n1 and n3 < n2:
	print(f'O menor número foi {n3}')