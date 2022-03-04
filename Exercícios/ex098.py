from time import sleep


def text(i, f, p):
	print(f'\033[1;31mContagem de {i} até {f} de {p} em {p}')
	print('='*60, '\033[m')
	
	
def contador(i, f, p):
	if p == 0:
		p = 1
	elif p < 0:
		p *= -1
		
	if i < f:
		text(i, f, p)
		for c in range(i, f+1, p):
			sleep(0.5)
			print(c)
		print('\n')
	else:
		sleep(0.5)
		text(i, f, p)
		for c in range(i, f-1, -p):
			sleep(0.5)
			print(c)
		print('\n')


contador(1, 10, 1)
contador(10, 0, 2)
sleep(0.5)
print('Você pode personalizar uma contagem!')
i = int(input('ÍNICIO : '))
f = int(input('FINAL : '))
p = int(input('PASSO : '))
contador(i, f, p)