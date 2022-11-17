import random


# Função que cria os tabuleiros

def criarTabuleiro(linhas, colunas):
    tabuleiro = []

    for i in range(linhas):
        listaLinhas = []
        for j in range(colunas):
            listaLinhas.append(0)

        tabuleiro.append(listaLinhas)

    return tabuleiro


# Função que imprime os tabuleiros

def imprimirTabuleiro(tabuleiro):
    for linha in range(len(tabuleiro)):
        print(tabuleiro[linha])


# Tabuleiros dos jogadores

tabuleiroJogadorCoord = criarTabuleiro(5, 10)  # Armazena as coordenadas das embarcações.
tabuleiroComputCoord = criarTabuleiro(5, 10)

tabuleiroJogadorFeed = criarTabuleiro(5, 10)
tabuleiroComputFeed = criarTabuleiro(5, 10)

# Coordenadas do computador
jogadasComputador = 0

while jogadasComputador < 5:

    linhasComput = random.randint(0, 4)
    colunasComput = random.randint(0, 9)

    for i in range(linhasComput):
        for j in range(colunasComput):
            if tabuleiroComputCoord[linhasComput][colunasComput] == 0:
                tabuleiroComputCoord[linhasComput][colunasComput] = 3
                jogadasComputador += 1
            else:
                jogadasComputador = jogadasComputador

# Coordenadas do jogador
jogadasJogador = 0

while jogadasJogador < 5:

    linhaJogad = int(input('Escolha uma posição vertical entre 0 e 4: '))
    colunaJogad = int(input('Escolha uma posição horizontal  entre 0 e 9: '))

    if linhaJogad < 0 or linhaJogad > 4:
        print("\nPosição inválida! Escolha uma posição entre 0 e 4 para linha e entre 0 e 9 para colunas:  \n")

    elif colunaJogad < 0 or colunaJogad > 9:
        print("\nPosição inválida! Escolha uma posição entre 0 e 4 para linha e entre 0 e 9 para colunas: \n")

    elif tabuleiroJogadorCoord[linhaJogad][colunaJogad] != 0:
        print("\nVocê já posicionou uma embarcação aqui! Tente novamente.\n")

    else:
        tabuleiroJogadorCoord[linhaJogad][colunaJogad] = 3
        print("\nEste é o seu tabuleiro:")
        imprimirTabuleiro(tabuleiroJogadorCoord)
        jogadasJogador += 1


embarcacoesJogad = 5
embarcacoesComput = 5

print('\nTabuleiro do Computador:')
imprimirTabuleiro(tabuleiroComputFeed)
print('=' * 30)
print(f"Embarcações restantes: {embarcacoesComput} \n")

print('Tabuleiro do Jogador: ')
imprimirTabuleiro(tabuleiroJogadorFeed)
print('=' * 30)
print(f"Embarcações restantes: {embarcacoesJogad} \n")



# Ataque do computador

ataquesComputador = 0

while ataquesComputador < 1:

    linhaJogad = random.randint(0, 4)  # 0
    colunaJogad = random.randint(0, 9)  # 0

    if tabuleiroJogadorCoord[linhaJogad][colunaJogad] != 0:
        print('Computador acertou! :(')
        tabuleiroJogadorCoord[linhaJogad][colunaJogad] = 1
        embarcacoesJogad -= 1
    elif tabuleiroJogadorCoord[linhaJogad][colunaJogad] == 0:
        print('Computador errou! :)')

    ataquesComputador = ataquesComputador + 1

    print(linhaJogad, colunaJogad)
    print(embarcacoesJogad)
    imprimirTabuleiro(tabuleiroJogadorCoord)




