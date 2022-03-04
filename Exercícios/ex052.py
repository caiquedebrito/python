num = int(input('Número: '))
t = 0
for c in range(1,num+1):
	if num % c == 0:
		t += 1

if t == 2:
	print(f'{num} é um número primo')
else:
	print(f'{num} não é um número primo')