import adivinhacao
import forca

print("*********************************")
print("***Bem-vindo ao menu de jogos!***")
print("*********************************", end="\n\n")

print("Escolha o jogo de sua preferência:")
print(" (1) Adivinhação")
print(" (2) Forca", end="\n\n")

while(True):

    var_opcao = int(input("Digite a sua opção de jogo: "))

    if(var_opcao >= 1 and var_opcao <=2):
        break
    else:
        print("Opção inválida!", end="\n\n")


if(var_opcao == 1):
    adivinhacao.jogar()
elif(var_opcao == 2):
    forca.jogar()