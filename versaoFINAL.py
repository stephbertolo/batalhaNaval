import random
import time


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


# Função que imprime o status atual dos tabuleiros
def tabuleirosStatus():
    print('\nTabuleiro do Computador:')
    imprimirTabuleiro(tabuleiroComputFeed)
    print('-' * 30)
    print(f"Embarcações restantes: {embarcacoesComput}\n")

    time.sleep(2)

    print('\nTabuleiro do Jogador: ')
    imprimirTabuleiro(tabuleiroJogadorFeed)
    print('=' * 30)
    print(f"Embarcações restantes: {embarcacoesJogad}\n")


# Tabuleiros dos jogadores e quantidades de embarcações
tabuleiroJogadorCoord = criarTabuleiro(5, 10)  # Armazena as coordenadas das embarcações
tabuleiroComputCoord = criarTabuleiro(5, 10)

tabuleiroJogadorFeed = criarTabuleiro(5, 10)  # Feedback do status dos tabuleiros
tabuleiroComputFeed = criarTabuleiro(5, 10)

embarcacoesJogad = 5  # Embarcações restantes
embarcacoesComput = 5

# Coordenadas do computador definidas previamente pelo programa, de forma aleatória
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

# Boas vindas ao jogo
print('\nBoas vindas a Batalha Naval! Antes de tudo, escolha as coordenadas para colocar suas embarcações.\n')
time.sleep(2)

# Coordenadas definidas pelo jogador para posicionar as suas embarcações
jogadasJogador = 0

while jogadasJogador < 5:

    linhaJogad = int(input('\nEscolha uma posição vertical entre 0 e 4: '))
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

time.sleep(2)

# Jogatina
while embarcacoesJogad and embarcacoesComput != 0:

    # Ataque do computador
    print('\nAgora é a vez do Computador de jogar!')
    time.sleep(2)

    ataquesComputador = 1

    while ataquesComputador == 1:

        linhaJogad = random.randint(0, 4)  # 0
        colunaJogad = random.randint(0, 9)  # 0

        if tabuleiroJogadorCoord[linhaJogad][colunaJogad] == 3:
            print('\nComputador acertou! :(\n')
            tabuleiroJogadorFeed[linhaJogad][colunaJogad] = 'X'
            embarcacoesJogad -= 1
        elif tabuleiroJogadorCoord[linhaJogad][colunaJogad] == 0:
            print('\nComputador errou! :)\n')
            tabuleiroJogadorFeed[linhaJogad][colunaJogad] = 'O'

        ataquesComputador -= 1
        time.sleep(2)
        tabuleirosStatus()
        time.sleep(2)

    # Ataque do jogador
    print('\nAgora é a sua vez de jogar!\n')
    time.sleep(2)

    ataquesJogador = 1

    while ataquesJogador == 1:

        linhaComput = int(input('Escolha qual posição horizontal deseja atacar (0, 4): '))
        colunaComput = int(input('Escolha qual posição vertical deseja atacar (0, 9): '))

        if linhaComput < 0 or linhaComput > 4:
            print("\nPosição inválida! Escolha uma posição entre 0 e 4 para linha e entre 0 e 9 para colunas:  \n")

        elif colunaComput < 0 or colunaComput > 9:
            print("\nPosição inválida! Escolha uma posição entre 0 e 4 para linha e entre 0 e 9 para colunas: \n")

        elif tabuleiroComputCoord[linhaComput][colunaComput] == 1:
            print('\nVocê já acertou essa embarcação!\n')

        elif tabuleiroComputCoord[linhaComput][colunaComput] == 3:
            print('\nVocê acertou! :)\n')
            tabuleiroComputCoord[linhaComput][colunaComput] = 1
            tabuleiroComputFeed[linhaComput][colunaComput] = 'X'
            embarcacoesComput -= 1
            ataquesJogador -= 1

        else:
            print('\nVocê errou! :(\n')
            tabuleiroComputFeed[linhaComput][colunaComput] = 'O'
            ataquesJogador -= 1

        time.sleep(2)
        tabuleirosStatus()
        time.sleep(2)


# Condições de vitória e de derrota

if embarcacoesComput == 0:
    print(f'Você venceu com {embarcacoesJogad} restantes! PARABÉNS!!')

else:
    print(f'Computador venceu com {embarcacoesComput} restantes! Fica para a próxima! :)')

print('\nObrigada por jogar BATALHA NAVAL! \nEste jogo foi desenvolvido por Stephanie, Melyça e Gabriel!')