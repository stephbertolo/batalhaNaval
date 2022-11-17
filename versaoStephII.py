import random


# Função que cria um tabuleiro.

def criarTabuleiro(linhas, colunas):
    tabuleiro = []

    for i in range(linhas):
        listaLinhas = []
        for j in range(colunas):
            listaLinhas.append(0)

        tabuleiro.append(listaLinhas)

    return tabuleiro


# Função que imprime um tabuleiro.

def imprimirTabuleiro(tabuleiro):
    for linha in range(len(tabuleiro)):
        print(tabuleiro[linha])


# Tabuleiros dos jogadores

tabuleiroJogadorCoord = criarTabuleiro(5, 10)
tabuleiroJogadorFeed = criarTabuleiro(5, 10)
tabuleiroComputCoord = criarTabuleiro(5, 10)
tabuleiroComputFeed = criarTabuleiro(5, 10)


# Jogada do computador
contador = 0

while contador < 5:

    posLinhas = random.randint(0, 4)
    posColunas = random.randint(0, 9)

    for i in range(posLinhas):
        for j in range(posColunas):
            if tabuleiroComputCoord[posLinhas][posColunas] == 0:
                tabuleiroComputCoord[posLinhas][posColunas] = 3
                contador += 1
            else:
                contador = contador


imprimirTabuleiro(tabuleiroComputCoord)

print(posLinhas, posColunas)