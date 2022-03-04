import random
import time
a1 = str(input('Nome do primeiro aluno: '))
a2 = str(input('Nome do segundo aluno: '))
a3 = str(input('Nome do terceiro aluno: '))
a4 = str(input('Nome do quarto aluno: '))
lista = a1, a2, a3, a4
print('Quem vai apagar o quadro é...')
time.sleep(2)
# O random.choice escolhe um item de uma lista.
print(random.choice(lista))
#print(random.sample(lista, k=4))
#print(random.shuffle(lista))