from random import randint

print('-='*13)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*13)

vitorias = 0
while True:
	cpu = randint(1,10)
	n = int(input('Digite um número: '))
	escolha = str(input('Você escolhe Par ou Ímpar: ')).upper().strip()
	soma = cpu + n
	
	print('-='*20)
	print(f'Você jogou {n} e o robô, {cpu} e a soma é {soma}.')
	print('-='*20)
	
	if escolha[0] in 'pP':
		if soma % 2 == 0:
			print('Você ganhou! Vamos jogar novamente...')
			vitorias += 1
		else:
			break
	elif escolha[0] in 'iIíÍ':
		if soma % 2 == 1:
			print('Você ganhou! Vamos jogar novamente...')
			vitorias += 1
		else:
			break
	else:
		print('Opção Inválida...')
		print('Escolha Par ou Ímpar.')

print(f'GAMER OVER!!! VOCÊ VENCEU {vitorias} VEZES.')
	