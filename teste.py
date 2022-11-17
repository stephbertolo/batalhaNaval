def criarTabuleiroComputador(linhas, colunas):
    tabuleiroComput = []

    for i in range(linhas):
        linhasComput = []
        for j in range(colunas):
            linhasComput.append(0)

        tabuleiroComput.append(linhasComput)

    return tabuleiroComput


print(criarTabuleiroComputador(5, 10))



def criarTabuleiroJogador(linhas, colunas):
    tabuleiroJogador = []

    for i in range(linhas):
        linhasJogador = []
        for j in range(colunas):
            linhasJogador.append(0)

        tabuleiroJogador.append(linhasJogador)

    return tabuleiroJogador

print(criarTabuleiroJogador(5, 10))