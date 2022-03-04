from datetime import datetime
ano = datetime.today().year
nasc = int(input('Digite o seu ano de nascimento? '))
idade = ano - nasc
print(f'Idade: {idade}')
print('Categoria: ')
if idade <= 9:
	print('MIRIM')
elif 9 < idade <= 14:
	print('INFANTIL')
elif 14 < idade <= 19:
	print('JUNIOR')
elif idade == 20:
	print('SÊNIOR')
else:
	print('MASTER')