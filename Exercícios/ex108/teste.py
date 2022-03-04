import moeda

n = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}')
print(f'O dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}')
print(f'Aumentando 2%, temos {moeda.moeda(moeda.aumentar(n, 2))}')
print(f'Diminuindo 5%, temos {moeda.moeda(moeda.diminuir(n, 5))}')