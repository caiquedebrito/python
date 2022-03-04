def notas(*n, sit=False):
	quanN = 0
	soma = 0
	maior = 0
	dicionario = {}
	
	for N in n:
		quanN += 1
		dicionario['Total de notas'] = quanN
		if N > maior:
			maior = N
			dicionario['Maior nota'] = maior
		soma += N
		
	for N in n:
		if N < maior:
			maior = N
			dicionario['Menor nota'] = N
		
	media = soma / quanN
	dicionario['Média'] = media
	
	if sit == True:
		if media > 7:
			dicionario['Situação'] = 'Boa'
		elif 5 <= media < 7:
			dicionario['Situação'] = 'Razoável'
		elif media < 5:
			dicionario['Situação'] = 'Ruim'
	
	return dicionario	
	
	
resp = notas(5.5, 2.5, 10, 6.5)
print(resp)