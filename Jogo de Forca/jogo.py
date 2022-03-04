from lista import  *

while True:
    print('''
1 - Jogar
2 - Sair
3 - Criar uma lista
    ''')
    opcao = int(input("Opção: "))
    if opcao == 1:
        print('''
1 - Frutas
2 - Animais
        ''')
        opcao = int(input("Opção: "))
        #ARMAZENA a lista escolhida pelo o usuário
        lista_escolhida = escolha_lista(opcao)
        palavra = sortear_palavra(lista_escolhida)
        word = list()
        lista = list()

        # Oculta as letras
        for letra in palavra:
            word.append(letra)
            lista.append("_")

        #print(lista)
        #Tentativas disponíveis
        x = 5
        while True:
            print(f"Você tem {x} tentativas.")
            print(lista)
            letra = str(input("Letra: ")).upper()

            #Verifica a letra digitada pelo jogador
            if letra in palavra:
                for index, let in enumerate(palavra):
                    if let == letra:
                        lista[index] = letra
            else:
                #Caso erre, o jogador perde uma tentativa
                x -= 1

            #O jogador vence
            if lista == word:
                print("Você acertou!")
                break
            #O jogo Encerra e o jogador perde
            if x == 0:
                print("Você perdeu!")
                print(f"A palavra era {palavra}")
                break
    elif opcao == 2:
        break
    elif opcao == 3:
        nome_lista = str(input("Qual o nome da lista? "))
        if '.txt' not in nome_lista: #Caso o usuário não coluque a extensão (.txt)
            nome_lista += '.txt'
        print(nome_lista)

        #criar_lista()
    else:
        print("Erro!")

