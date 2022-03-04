while True:
	n = int(input('Quer ver a tabuada de qual numero ? '))
	if n <= 0:
		break
	for c in range(1,11):
		t = c * n
		print(f'{n} x {c} = {t}')