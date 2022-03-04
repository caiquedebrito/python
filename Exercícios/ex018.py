import math
ang = int(input('Qual o ângulo ? '))
cos = math.cos(math.radians(ang))
sen = math.sin(math.radians(ang))
tan = math.tan(math.radians(ang))
print(f'O ângulo de {ang}° tem :')
print(f'Seno = {sen:.2f}')
print(f'Cosseno = {cos:.2f} ')
print(f'Tangente = {tan:.2f}')