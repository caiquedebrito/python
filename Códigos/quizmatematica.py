import random
n1 = random.randint(0,100)
n2 = random.randint(0,100)
s = n1 + n2
p = int(input('Quanto é {} + {} ? '.format(n1,n2)))
if p == s:
	print('ACERTOU MISERAVI!!!')
else:
	print('O MISERAVI É UM... BURROO!!')