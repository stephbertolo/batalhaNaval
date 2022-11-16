import random
import time

tabuleiroPlayerCoord = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
tabuleiroComputCoord = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
tabuleiroPlayerFeed = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
tabuleiroComputFeed = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


# Função que imprime os tabuleiros.
def imprimirTabuleiro(tabuleiro):
    for coluna in range(5):
        print(tabuleiro[coluna])


# Jogadas do computador
colunasComput = []

for valor in range(10):
    colunasComput.append(valor)

linhasComput = []

for num in range(5):
    linhasComput.append(num)

for jogadasComputador in range(5):

    contadorComput = 0

    while contadorComput < 1:
        posicaoLinhaComput = random.choice(linhasComput)
        posicaoColunaComput = random.choice(colunasComput)

        if tabuleiroComputCoord[posicaoLinhaComput][posicaoColunaComput] != 0:
            print("")
        else:
            tabuleiroComputCoord[posicaoLinhaComput][posicaoColunaComput] = 3
            contadorComput += 1

imprimirTabuleiro(tabuleiroComputCoord)




# Enquanto esse for rodar, o jogador escolherá suas posições.
for posicionarJogadas in range(5):

    contador = 0

    while contador < 1:

        posicaoLinha = int(input("\nSelecione uma linha para posicionar sua embarcação (0, 4): "))
        posicaoColuna = int(input("\nSelecione uma coluna para posicionar sua embarcação (0, 9): "))

        if posicaoLinha < 0 or posicaoLinha > 4:
            print("\nPosição inválida! Escolha uma posição entre 0 e 4 para linha e entre 0 e 9 para colunas:  \n")

        elif posicaoColuna < 0 or posicaoColuna > 9:
            print("\nPosição inválida! Escolha uma posição entre 0 e 4 para linha e entre 0 e 9 para colunas: \n")

        elif tabuleiroPlayerCoord[posicaoLinha][posicaoColuna] != 0:
            print("\nVocê já posicionou uma embarcação aqui! Tente novamente.\n")

        else:
            tabuleiroPlayerCoord[posicaoLinha][posicaoColuna] = 3
            print("\nEste é o seu tabuleiro:")
            imprimirTabuleiro(tabuleiroPlayerCoord)
            contador += 1





print("\n Agora que você posicionou todas as suas embarcações, vamos começar.")
