salario = float(input('Qual o salário do funcionário ? '))
if salario > 1250:
	aumento = 110 / 100 * salario
	print(f'O novo salário do funcionário será de R$ {aumento:.2f}')
if salario <= 1250:
	aumento = 115 / 100 * salario
	print(f'O novo salário do funcionário será de R$ {aumento:.2f}')