from random import randint
from time import sleep
cpu = randint(0,5)
print('\033[1;31m-=-'*20)
print(f'{"ADIVINHE O NÚMERO":^60}')
print('-=-'*20)
n = int(input('\033[m \033[1;32mEntre 0 e 5. Em que número eu pensei ? \033[m'))
if n == cpu:
	print('\033[1;33mParabéns!! Você acertou!!')
else:
	print('\033[1;34mTente outra vez!!!\033[m')
print(f'\033[1;35mEu pensei no número {cpu}\033[m')