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


embarcacoesJogad = 5  # Embarcações restantes
embarcacoesComput = 5

# Coordenadas do computador

jogadasComputador = 0

while jogadasComputador < 5:

    linhaComput = random.randint(0, 4)
    colunaComput = random.randint(0, 9)

    for i in range(linhaComput):
        for j in range(colunaComput):
            if tabuleiroComputCoord[linhaComput][colunaComput] == 0:
                tabuleiroComputCoord[linhaComput][colunaComput] = 3
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
        #imprimirTabuleiro(tabuleiroJogadorCoord)
        jogadasJogador += 1



print('\nTabuleiro do Computador:')
imprimirTabuleiro(tabuleiroComputFeed)
print('=' * 30)
print(f"Embarcações restantes: {embarcacoesComput} \n")

print('Tabuleiro do Jogador: ')
imprimirTabuleiro(tabuleiroJogadorFeed)
print('=' * 30)
print(f"Embarcações restantes: {embarcacoesJogad} \n")

# Ataques

while embarcacoesJogad and embarcacoesComput != 0:

    # Ataque do computador

    ataquesComputador = 0

    while ataquesComputador < 1:

        linhaJogad = random.randint(0, 4)  # 0
        colunaJogad = random.randint(0, 9)  # 0

        if tabuleiroJogadorCoord[linhaJogad][colunaJogad] != 0:
            print('Computador acertou! :(')
            tabuleiroJogadorCoord[linhaJogad][colunaJogad] = 'X'
            embarcacoesJogad -= 1
        elif tabuleiroJogadorCoord[linhaJogad][colunaJogad] == 0:
            print('Computador errou! :)')

        ataquesComputador += 1

        print(linhaJogad, colunaJogad)
        print(embarcacoesJogad)
        imprimirTabuleiro(tabuleiroJogadorCoord)


    imprimirTabuleiro(tabuleiroComputCoord)
    # Ataque do jogador

    ataquesJogador = 0

    while ataquesJogador < 1:

        linhaComput = int(input('Escolha qual posição horizontal deseja atacar (0, 4): '))
        colunaComput = int(input('Escolha qual posição vertical deseja atacar (0, 9): '))

        if linhaComput < 0 or linhaComput > 4:
            print("\nPosição inválida! Escolha uma posição entre 0 e 4 para linha e entre 0 e 9 para colunas:  \n")

        elif colunaComput < 0 or colunaComput > 9:
            print("\nPosição inválida! Escolha uma posição entre 0 e 4 para linha e entre 0 e 9 para colunas: \n")

        elif tabuleiroComputCoord[linhaComput][colunaComput] != 0:
            print('Você acertou! :)')
            tabuleiroComputCoord[linhaComput][colunaComput] = 'X'
            embarcacoesComput -= 1

        elif tabuleiroComputCoord[linhaComput][colunaComput] == 0:
            print('Você errou! :(')

        ataquesJogador += 1

        print(linhaComput, colunaComput)
        print(embarcacoesComput)
        imprimirTabuleiro(tabuleiroComputCoord)


