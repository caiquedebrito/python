frase = str(input('Escreva uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for l in range(len(junto)-1, -1, -1):
	inverso += junto[l]
print(junto, inverso)
if junto == inverso:
	print('Temos palíndromo.')
else:
	print('Não temos um palíndromo.')