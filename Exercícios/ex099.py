from time import sleep


def maior(* num):
	print('Analisando os valores...')
	print('=-'*30)
	t = maior = 0
	for v in num:
		print(v)
		if v > maior:
			maior = v
		t += 1
		sleep(0.5)
	print(f'Foram informados {t} valores ao todo.')
	print(f'O maior valor foi {maior}')
	print('\n')


maior(7,6,4,7,9)
maior(9,2,8)
maior(90,100,7,9)
maior(0)