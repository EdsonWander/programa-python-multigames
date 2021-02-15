import random
import os

def mensagem_abertura():
    print("*********************************")
    print("***Bem-vindo ao jogo da Forca!***")
    print("*********************************", end="\n\n")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")

    lista_palavras_secretas = []

    for linha in arquivo:
        linha = linha.strip()
        linha = linha.upper()
        lista_palavras_secretas.append(linha)

    arquivo.close()

    return lista_palavras_secretas[random.randrange(0, len(lista_palavras_secretas))]

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def desenha(escolha):

    if(escolha == 0):
        print("________")
        print("|      |")
        print("|       ")
        print("|       ")
        print("|       ")
        print("_       ")

    elif(escolha == 1):
        print("________")
        print("|      |")
        print("|      0")
        print("|       ")
        print("|       ")
        print("_       ")

    elif(escolha == 2):
        print("________")
        print("|      |")
        print("|      0")
        print("|      |")
        print("|       ")
        print("_       ")

    elif(escolha == 3):
        print("________")
        print("|      |")
        print("|      0")
        print("|     /|")
        print("|       ")
        print("_       ")

    elif(escolha == 4):
        print("________")
        print("|      |")
        print("|      0")
        print("|     /|\ ")
        print("|       ")
        print("_       ")

    elif(escolha == 5):
        print("________")
        print("|      |")
        print("|      0")
        print("|     /|\ ")
        print("|     / ")
        print("_       ")

    else:
        print("________")
        print("|      |")
        print("|      0")
        print("|     /|\ ")
        print("|     / \ ")
        print("_       ")


def jogar():

    #limpa a tela
    limpar_tela()

    #exibe mensagem de boas-vindas
    mensagem_abertura()

    #carrega a palavra secreta vinda do arquivo
    var_palavra_secreta = carrega_palavra_secreta()
    #var_palavra_secreta = "banana".upper()

    var_enforcou = False
    var_acertou = False
    var_letra = ""
    lista_letra_acertadas = []
    lista_letra_usadas = []
    var_index = 0
    var_tamanho = len(var_palavra_secreta)
    var_erros = 0

    while (var_index < var_tamanho):
        lista_letra_acertadas.append("_")
        var_index = var_index + 1

    while(not var_enforcou and not var_acertou):

        var_letra = input("Escolha uma letra: ")
        var_letra = var_letra.strip()
        var_letra = var_letra.upper()

        var_index = 0

        if(var_letra not in lista_letra_usadas):

            lista_letra_usadas.append(var_letra)

            print("", end="\n")
            print("Palavra: ", end="")

            if var_letra in var_palavra_secreta:
                for letra in var_palavra_secreta:

                    if(var_letra == letra):
                        lista_letra_acertadas[var_index] = letra

                    var_index = var_index + 1
            else:
                var_erros = var_erros + 1

            var_index = 0

            while (var_index < var_tamanho):
                print(lista_letra_acertadas[var_index] + " ", end="")
                var_index = var_index + 1

            if("_" not in lista_letra_acertadas):
                var_acertou = True
                print("", end="\n")
                print("Você venceu!")

            print("", end="\n")

            if(var_erros > 5):
                var_enforcou = True
                print("", end="\n")
                print("Você perdeu!")
                print("A palavra secreta era: {}".format(var_palavra_secreta), end="\n\n")

            #desenha a forca
            desenha(var_erros)

            print("", end="\n")

        else:
            print("Essa letra já foi utilizada!", end="\n\n")

    print("Fim do jogo!")

    print("", end="\n")

    input("Digite <ENTER> para sair...")

if (__name__ == '__main__'):
    jogar()