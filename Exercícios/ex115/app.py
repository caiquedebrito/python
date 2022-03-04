from interface import *
from arquivo import *

arq = 'dados.txt'

if not arquivoExisti(arq):
	criarArquivo(arq)

while True:
	menu(['VER LISTA', 'CADASTRAR PESSOA', 'SAIR DO SISTEMA'])
	o = leiaInt('Opção: ')
	if o == 1:
		cabeçalho('Pessoas cadastradas')
		lerArquivo(arq)
	elif o == 2:
		cabeçalho('Novo cadastro')
		nome = str(input('Nome: '))
		idade = leiaInt('Idade: ')
		cadastrar(arq, nome, idade)
	elif o == 3:
		cabeçalho('Encerrando...')
		break
	else:
		print('Opção inválida.')
