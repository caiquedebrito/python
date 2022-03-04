expressão = list()
totP = 0
e = str(input('Digite a expressão : '))

for i in range(0,len(e)):
	expressão.append(e[i])

for letra in expressão:
	if letra == '(' or letra == ')':
		totP += 1
		
if totP % 2 == 0:
	print('A expressão esta correta.')
else: 
	print('A expressão esta errada.')