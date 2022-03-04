def arquivoExisti(nome):
	try:
		a = open(nome, 'rt')
		a.close()
	except:
		return False
	else:
		return True
		

def criarArquivo(nome):
	try:
		a = open(nome, 'wt+')
		a.close()
	except:
		print('Falha ao criar o arquivo.')
	else:
		print('Arquivo criado com sucesso')
		
		
def lerArquivo(nome):
	try:
		a = open(nome, 'rt')
	except:
		print('Erro ao abrir o arquivo.')
	else:
		for linha in a:
			dado = linha.split(';')
			dado[1] = dado[1].replace('\n', '')
			print(f'{dado[0]:<30} {dado[1]:<2} anos')
	finally:
		a.close()
		

def cadastrar(arq, nome='desconhecido', idade=0):
		try:
			a = open(arq, 'at')
		except:
			print('Erro ao abrir o arquivo.')
		else:
			try:
				a.write(f'{nome};{idade}\n')
			finally:
				a.close()
				print('Novo cadastro salvo.')
		