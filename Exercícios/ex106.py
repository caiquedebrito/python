cores = [
'\033[m',
'\033[35m',
'\033[41m',
'\033[42m',
'\033[44m'
]


def ajuda(com):
	título(f'Acessando a Função/Biblioteca \'{com}\' ', 4)
	print(cores[1])
	help(com)
	print(cores[0])


def título(msg, cor=0):
	tam = len(msg) + 4
	print(cores[cor])
	print('~'* tam)
	print(f'  {msg}  ')
	print('~' * tam)
	print(cores[0])


while True:
	título('Sistema de ajuda Pyhelp', 3)
	comando = str(input('Função ou Biblioteca > '))
	if comando.upper() == 'FIM':
		break
	else:
		ajuda(comando)
título('Até logo...', 2)