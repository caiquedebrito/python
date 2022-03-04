from math import pow
peso = float(input('Qual o seu peso(kg)? '))
altura = float(input('Qual a sua altura(m)? '))
imc = peso/pow(altura,2)
print(f'IMC: {imc:.2f}')
if 18.5 >= imc:
	print('Abaixo do peso')
elif 18.5 < imc <= 25:
	print('Peso ideal')
elif 25 < imc <= 30:
	print('Sobrepeso')
elif 30 < imc <= 40:
	print('Obesidade')
else:
	print('Obesidade Morbida')
	