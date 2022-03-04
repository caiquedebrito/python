n = list()
num = int(input('Digite um valor : '))
n.append(num)
#print('Valor adicionado no final da lista...')
for v in range(0,3):
	num = int(input('Digite um valor : '))
	n.append
	for v in range(0,len(n)):
		for i in range(0,len(n)):
			if n[v] > n[i]:
				n.insert(i,n[v])
				break
			
print(len(n))
print(n)