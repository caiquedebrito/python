lista_numeros = list()
for n in range(0,5):
	valor = int(input('Digite um valor : '))
	lista_numeros.append(valor)
aux = 0
for v in range(0,5):
	for c in range(v+1,5):
		if lista_numeros[v] > lista_numeros[c]:
			aux = lista_numeros[v]
			lista_numeros[v] = lista_numeros[c]
			lista_numeros[c] = aux

print(lista_numeros)