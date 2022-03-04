n = total = soma = 0
while n != 999:
	n = int(input('Digite um número: '))
	total += 1
	soma += n
soma -= 999
print(f'Foram digitados {total-1} números.')
print(f'A soma entre todos os números é {soma}')