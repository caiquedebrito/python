total_idades = 0
maior_idade = 0
mulheres_menos20 = 0

for i in range(4):
	nome = str(input('NOME: '))
	sexo = str(input('Sexo[M/F]: ')).upper().strip()
	idade = int(input('IDADE: '))
	total_idades += idade
	if sexo[0] == 'M':
		if idade > maior_idade:
			maior_idade = idade
			Homem_V = nome   #Verifica quem é o nome do homem mais velho
	elif sexo[0] == 'F':
		if idade < 20:
			mulheres_menos20 += 1
		
media_idade = total_idades / 4
print(f'A média de idade é : {media_idade}.')
print(f'O homem mais velho é {Homem_V} com {maior_idade} anos.')
print(f'{mulheres_menos20} mulheres têm menos de 20 anos.')