def voto(nasc):
	from datetime import date
	
	atual = date.today().year
	idade = atual - nasc
	
	if 65 > idade >= 18:
		return f'Com {idade} anos : VOTO OBRIGATÓRIO'
	elif 16 <= idade < 18 or idade > 65:
		return f'Com {idade} anos : VOTO OPICIONAL'
	else:
		return f'Com {idade} anos : NÃO VOTA'
		

#Programa principal
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))