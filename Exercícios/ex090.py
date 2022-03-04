media = dict()
media['Nome'] = str(input('Nome : '))
media['Media'] = float(input(f'Média de {media["Nome"]}: '))

if media['Media'] >= 7.0:
	media['Situação'] = 'Aprovado'
else:
	media['Situação'] = 'Reprovado'
	
print(f'Nome é igual a {media["Nome"]}.')
print(f'Média é igual a {media["Media"]}.')
print(f'Situação igual a {media["Situação"]}.')

