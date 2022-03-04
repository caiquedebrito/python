n = int(input('Digite um número para ver sua tabuada: '))
for c in range(1,11):
	print(f'{"":<20}{n} x {c:<3} = {n*c:>2}')