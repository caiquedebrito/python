n = int(input('Digite um numero inteiro: '))
print('''Escolha uma opcao:
[1] Converter para BINARIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
e = int(input('SUA OPCAO: '))
if e == 1:
	print(f'{n} convertido para binario e {bin(n)[2:]}')
elif e == 2:
	print(f'{n} convertido para octal e {oct(n)[2:]}')
elif e == 3:
	print(f'{n} convertido para hexadecimal e {hex(n)[2:]}')
else:
	print('Opcao invalida')