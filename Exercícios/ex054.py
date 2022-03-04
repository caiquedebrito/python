from datetime import datetime
ano_atual = datetime.today().year
maior = menor = 0
for c in range(7):
	ano = int(input(f'Ano de nascimento da {c+1}°: '))
	idade = ano_atual - ano
	if idade >= 21:
		maior += 1
	else:
		menor += 1
print(f'{maior} pessoas são maiores de idade.')
print(f'{menor} pessoas são menores de idade.')