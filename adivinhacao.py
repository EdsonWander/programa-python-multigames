import random
import os

def mensagem_abertura():
    print("*********************************")
    print("Bem-vindo ao jogo de Adivinhação!")
    print("*********************************", end="\n\n")

def exibe_menu():
    print("Qual o nível de dificuldade?")
    print(" (1) Fácil")
    print(" (2) Médio")
    print(" (3) Difícil", end="\n\n")

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def jogar():

    # limpa a tela
    limpar_tela()

    #exibe mensagem de boas-vindas
    mensagem_abertura()

    #exibe menu de dificuldade
    exibe_menu()

    var_nivel = int(input("Digite o nível: "))
    var_num_secreto = random.randint(1,100)
    var_rodada = 1
    var_pontos = 1000
    var_fator_dificuldade = 1
    var_tentativas = 1

    while(True):
        if(var_nivel == 1):
            var_tentativas = 8
            var_fator_dificuldade = 3
            break
        elif(var_nivel == 2):
            var_tentativas = 5
            var_fator_dificuldade = 2
            break
        elif (var_nivel == 3):
            var_tentativas = 3
            var_fator_dificuldade = 1
            break
        else:
            print("Opção inválida!", end="\n\n")
            var_nivel = int(input("Digite o nível: "))

    print("", end="\n")

    while(var_rodada <= var_tentativas and var_pontos > 0):

        print("Tentativa {} de {}".format(var_rodada, var_tentativas), end="\n\n")
        numero_usuario = int(input("Digite um número entre 1 e 100: "))

        if (numero_usuario >= 1 and numero_usuario<=100):

            if (var_num_secreto == numero_usuario):
                print("Você acertou!", end="\n\n")
                break
            else:
                if(var_num_secreto < numero_usuario):
                    print("Você errou! Seu número é maior!", end="\n\n")
                    var_pontos = var_pontos - ((numero_usuario - var_num_secreto) * var_fator_dificuldade)
                elif(var_num_secreto > numero_usuario):
                    print("Você errou! Seu número é menor!", end="\n\n")
                    var_pontos = var_pontos - ((var_num_secreto - numero_usuario) * var_fator_dificuldade)

            var_rodada = var_rodada + 1

            if (var_rodada > var_tentativas or var_pontos <= 0):
                var_pontos = 0

        else:
            print("Número inválido!", end="\n\n")
            continue

    print("O número secreto era: {}".format(var_num_secreto))
    print("Sua pontuação é {}".format(var_pontos), end="\n\n")
    print("Fim do jogo!")

    print("", end="\n")

    input("Digite <ENTER> para sair...")

if (__name__ == '__main__'):
    jogar()