import random
import time


def printTabuleiro(num1):
    for coluna in range(5):
        print(num1[coluna])

tabuleiroPlayer = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]
tabuleiroComput = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]
tabuleiroMarcplayer = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]
tabuleiroMarcComput = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]


colunas = []
for valor in range(10):
    colunas.append(valor)

linhas = []
for num in range(5):
    linhas.append(num)

for quant in range(5):

    cont3 = 0

    while cont3 < 1:
        posColunas = random.choice(colunas)
        posLinhas = random.choice(linhas)
        if tabuleiroComput[posLinhas][posColunas] != 0:
            print("")
        else:
            tabuleiroComput[posLinhas][posColunas] = 3
            cont3 += 1

printTabuleiro(tabuleiroComput)



print("Bem vindos ao Batalha Naval!")
print("\n")
time.sleep(3)
print("=================================")
print("\n")
print("Você precisará inicialmente definir as posições dos seus navios.")
print("As posições são definidas entre linhas e colunas. As linhas são horizontais(0 a 4) e as colunas verticais(0 a 9).")
time.sleep(5)
print("\n")
print("Este é o seu tabuleiro:")
printTabuleiro(tabuleiroPlayer)
print("\n")
for cont in range(5):
    whileCont = 0
    while whileCont < 1:
        linhasChoose = int(input("Digite o número de uma linha(0 a 4):"))
        print("\n")
        colunasChoose = int(input("Digite o número de uma coluna(0 a 9)"))
        print("\n")
        if (linhasChoose < 0 or linhasChoose > 4):
            print("Por favor, digite um valor válido para as linhas. Entre 0 e 4:")
            print("\n")
            time.sleep(2)
        elif (colunasChoose < 0 or colunasChoose > 9):
            print("Por favor, digite um valor válido para as colunas. Entre 0 e 9")
            print("\n")
            time.sleep(2)
        elif (tabuleiroPlayer[linhasChoose][colunasChoose] != 0):
            print("Você já colocou um navio nesta posição. Por favor, selecione outra!")
            print("\n")
            time.sleep(3)
            print("Este é o seu tabuleiro:")
            printTabuleiro(tabuleiroPlayer)
        else:
            tabuleiroPlayer[linhasChoose][colunasChoose] = 3
            print("Este é o seu tabuleiro:")
            printTabuleiro(tabuleiroPlayer)
            print("\n")
            whileCont += 1
            time.sleep(2)
time.sleep(4)
print("Agora que posicionou todas as embarcações, vamos começar:")
print("\n")
time.sleep(3)
print("=================================")
print("\n")
print("Este é o seu tabuleiro:")
printTabuleiro(tabuleiroMarcplayer)
print("\n")
time.sleep(3)
print("Este é o tabuleiro inimigo:")
printTabuleiro(tabuleiroMarcComput)
print("\n")
whileCont = 0
whileContsupreme = 0
embarcMe = 5
embarcEnemy = 5

# Ataque
while whileContsupreme < 1:

    whileCont = 0

    while whileCont < 1:


        linhasChoose = int(input("Qual linha inimiga deseja atacar? (0 a 4):"))
        colunasChoose = int(input("Qual Coluna inimiga deseja atacar? (0 a 9):"))


        if tabuleiroComput[linhasChoose][colunasChoose] != 0:
            print("Parabéns, você acertou!")


            tabuleiroMarcComput[linhasChoose][colunasChoose] = 3

            print("Este é o tabuleiro inimigo:")

            printTabuleiro(tabuleiroMarcComput)

            embarcEnemy -= 1

            print("Restaram " + str(embarcEnemy) + " embarcações.")

            whileCont += 1

        elif tabuleiroMarcComput[linhasChoose][colunasChoose] != 0:

            print("Você já escolheu essa posição. Tente novamente!")

            time.sleep(2)

        elif (linhasChoose < 0 or linhasChoose > 4):
            print("Por favor, digite um valor válido para as linhas. Entre 0 e 4:")
            print("\n")
            time.sleep(2)

        elif (colunasChoose < 0 or colunasChoose > 9):
            print("Por favor, digite um valor válido para as colunas. Entre 0 e 9")
            print("\n")
            time.sleep(2)

        else:
            print("Você errou :(")
            print("\n")
            time.sleep(2)
            tabuleiroMarcComput[linhasChoose][colunasChoose] = 6
            print("Este é o tabuleiro inimigo:")
            printTabuleiro(tabuleiroMarcComput)
            print("Restaram " + str(embarcEnemy) + " embarcações.")
            whileCont += 1

        if embarcMe < 1:
            time.sleep(2)
            print("Parabéns! Você afundou todas as embarcações inimigas!")
            print("Jogo desenvolvido por Gabs, Steph e Melyça")
            print("Obrigado por jogar!!")
            whileContsupreme += 2
        else:
            print("\n")


    whileCont -= 1
    while whileCont < 1:


        posColunas = random.choice(colunas)
        posLinhas = random.choice(linhas)


        if tabuleiroPlayer[posLinhas][posColunas] != 0:
            tabuleiroMarcplayer[posLinhas][posColunas] = 3
            embarcMe -= 1
            whileCont += 1

        elif tabuleiroMarcplayer[posLinhas][posColunas] != 0:
            print("")

        elif (posLinhas < 0 or posLinhas > 4):
            print("")

        elif (posColunas < 0 or posColunas > 9):
            print("")

        else:
            print("\n")
            print("O inimigo errou :)")
            time.sleep(3)
            tabuleiroMarcplayer[posLinhas][posColunas] = 6
            print("Este é o seu tabuleiro:")
            printTabuleiro(tabuleiroMarcplayer)
            print("Restaram " + str(embarcMe) + " embarcações.")
            whileCont += 1
        if embarcEnemy < 1:
            print("Droga! O inimigo afundou todas suas embarcações :(")
            time.sleep(1)
            print("Jogo desenvolvido por Gabs, Steph e Melyça")
            time.sleep(1)
            print("Obrigado por jogar!!")
            whileContsupreme += 2
        else:
            print("\n")