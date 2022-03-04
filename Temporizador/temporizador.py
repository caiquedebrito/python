from time import sleep

def temporizador(m=0, s=0):
	#Temporizador para minutos
	if m > 0:
		if s > 0:
			for tempo in range(s, -1, -1):
				print('\n')
				print(f"{m:>28} : {tempo}")
				sleep(1)
		while m > 0:
			m -= 1
			for tempo in range(59, -1, -1):
				print('\n')
				print(f"{m:>28} : {tempo}")
				sleep(1)
	#Temporizador para segundos
	else:
		for tempo in range(s, -1, -1):
			print('\n')
			print(f"{'':>28}0 : {tempo}")
			sleep(1)


#Temporizador
while True:
	try:
		minutos = int(input('Minutos: '))
	except:
		print('ERRO!')
	else:
		while True:
			try:
				segundos = int(input('Segundos: '))
			except:
				print('ERRO!')
			else:
				temporizador(minutos, segundos)
				break
		break
	
	