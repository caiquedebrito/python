frase = str(input('Escreva uma FRASE : ')).strip().lower()
print(f'A letra A apareceu {frase.count("a")} vezes' )
print(f'A letra A apareceu primeiramente na posicao {frase.find("a")+1}')
print(f'A letra A apareceu pela ultima vez na posicao {frase.rfind("a")+1}')