tot3 = 0
for c in range(1,501):
	if c % 2 == 1 and c % 3 == 0:
		tot3 += c
print(f'O total dos múltiplos de 3 que são ímpares é {tot3}')