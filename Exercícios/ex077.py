palavras = ('Carro', 'Moto', 'Programacao', 'Matematica', 'Caique', 'Flamengo')
vogais = ('a', 'e', 'i', 'o', 'u')

for p in palavras:
	t = len(p)
	print('\n Na palavra {}{}{} temos as vogais '.format('\033[34m',p.upper(), '\033[m'), end='')
	for l in range(0,t):
		for v in range(0,5):
			if p[l] == vogais[v]:
				print('\033[32m', vogais[v],'\033[m', end=' ')