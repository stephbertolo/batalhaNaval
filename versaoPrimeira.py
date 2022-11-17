import random

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


############################ Programa principal #################################


# Jogadas do computador, feitas previamente pelo programa e registradas no tabuleiro de coordenadas.

def jogadasComputador(linhas, colunas):
    tabuleiroComputCoord = [0]

    for i in range(linhas):
        linhasComput = []
        for j in range(colunas):
            linhasComput.append(i)

    tabuleiroComputCoord.append(linhasComput)

    return tabuleiroComputCoord

for jogadasComputador in range(5):

    contadorComput = 0

    while contadorComput < 1:
        posicaoLinhaComput = random.choice(linhasComput)
        posicaoColunaComput = random.choice(colunasComput)

        if tabuleiroComputCoord[posicaoLinhaComput][posicaoColunaComput] != 0:
            contadorComput = 0
        else:
            tabuleiroComputCoord[posicaoLinhaComput][posicaoColunaComput] = 3
            contadorComput += 1


print("Boas vindas ao jogo de Batalha Naval!\n"
      "Para começar, você deve escolher as posições de suas embarcações.\n"
      "As posições são definidas entre linhas e colunas. As linhas são horizontais (0 a 4) e as colunas verticais (0 a 9).\n \n"
      "Este é o seu tabuleiro: \n")

imprimirTabuleiro(tabuleiroPlayerCoord)

# Enquanto esse for rodar, o jogador escolherá as posições das embarcações.
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

print("\nAgora que você posicionou todas as suas embarcações, vamos começar.")
