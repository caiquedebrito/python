import moeda

p = float(input('Digite um preço: R$'))
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'Aumentando {p} em 10% temos {moeda.aumentar(p, 10)}')
print(f'Diminuindo {p} em 15% temos {moeda.diminuir(p, 15)}')