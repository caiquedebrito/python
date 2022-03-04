def leiaInt(msg):
	
	while True:
		try:
			inte = int(input(msg))
		except:
			print('\033[31mERRO: Digite um numero inteiro.\033[m')
		else:
			return inte
			break
			
			
def leiaFloat(msg):
			while True:
				try:
					real = float(input(msg))
				except:
					print('\033[31mErro. Digite um número real.\033[m')
				else:
					return real
					break
					
			
i = leiaInt('Digite um número inteiro: ')
r = leiaFloat('Digite um número real: ')
print(f'O valor inteiro foi {i} e o valor real foi {r}')