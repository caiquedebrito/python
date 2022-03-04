try:
	a = int(input('Numerador: '))
except ValueError:
	print('Digite apenas números inteiros.')
else:
	try:
		b = int(input('Denominador: '))
		r = a / b
#except Exception as erro:
#	print(f'O problema encontrado foi {erro.__class__}')
	except ValueError:
		print('Digite apenas números inteiros.')
	except ZeroDivisionError:
		print('Divisão por Zero não é possível.')
	else:
		print(f'O resultado é {r:.1f}')
finally:
	print('Volte sempre :)')