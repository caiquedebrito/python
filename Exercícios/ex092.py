from datetime import datetime

ano = datetime.today().year
dados = dict()
dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
idade = ano - nasc
dados['Idade'] = idade

if idade >= 18:
	dados['CTPS'] = int(input('Carteira de trabalho (0 não tem) : '))
	if dados['CTPS'] > 0:
		dados['Contratação'] = int(input('Ano de contratação : '))
		dados['Sálario'] = float(input('Sálario: R$'))
		aposen = idade + (35 - ( ano - dados['Contratação']))
		dados['Aposentadoria'] = aposen
		
for k, v in dados.items():
	print(f'{k} = {v}')