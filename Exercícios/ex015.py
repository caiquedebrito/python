km = float(input('Quantos Km foi percorrido ? '))
dias = int(input('Quantos dias foi alugado ? '))
aluguel = dias * 60 + km * 0.15
print(f'Aluguel : R${aluguel:.2f}')