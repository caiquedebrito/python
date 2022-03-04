from datetime import datetime
print('~'*60)
print(f'{"ALISTAMENTO MILITAR 2021":^60}')
print('~'*60)
ano = int(input('Digite o seu ano de nascimento: '))
ano_atual = datetime.today().year
idade = ano_atual - ano
print(idade, 'Anos')
if idade < 18:
	print('Você ainda vai se alistar no exercito.')
	print('Falta ano(s) {} , para o alistamento.'.format(18 - idade))
elif idade == 18:
	print('Está na hora de você se alistar.')
else:
	print('Já passou o tempo de você se alistar.')
	print('Se param {} ano(s) do alistamento.'.format(idade-18))
