def lista():
    nome = str(input("Digite o nome da nova lista: "))



def criar_lista():
    nome = 'animais'
    arquivo = f"{nome}.txt"
    try:
        a = open(arquivo, 'wt+')
    except:
        print("Erro!")
    else:
        print("Arquivo criado com sucesso")


def escolha_lista(opcao):
    listas = list()
    arq = open('listas.txt', 'rt')
    for lista in arq:
        listas.append(lista)
    #lista escolhida pelo o usuário
    nome_lista = listas[opcao-1].replace('\n', '')
    lista = ler_lista(nome_lista)
    return lista



#Ler os itens da lista escolhida pelo usuário
def ler_lista(nome_lista):
    #Abre a lista selecionada
    arq = open(nome_lista, 'rt')
    lista = list()
    #Guarda cada item em uma lista
    for linha in arq:
        lista.append(linha)
    arq.close()
    return lista

#Sorteia uma palavra da lista escolhida
def sortear_palavra(lista):
    from random import randint
    #Tamanho da lista
    t = len(lista)
    #Número sorteado
    n = randint(0, t-1)
    #Palavra sorteada
    palavra = lista[n].replace('\n', '')
    return palavra


