import moeda

n = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.moeda(n)} é {moeda.metade(n, True)}')
print(f'O dobro de {moeda.moeda(n)} é {moeda.dobro(n, True)}')
print(f'Aumentando 2%, temos {moeda.aumentar(n, 2, True)}')
print(f'Diminuindo 5%, temos {moeda.diminuir(n, 5, True)}')