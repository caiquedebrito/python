flag = 'S'
total = maior = menor = soma = 0

while flag[0] != 'N':
	n = int(input('Digite um valor: '))
	total += 1
	soma += n
	if menor == 0:
		menor = n
	if n > maior:
		maior = n
	elif n < menor:
		menor = n
	flag = str(input('Quer continuar? [S/N] ')).upper().strip()
	
média = soma/total

print(f'Você digitou {total} números e a média entre eles foi {média}.')
print(f'O maior número foi {maior} e o menor foi {menor}.')
