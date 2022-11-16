import random

tabuleiroComput = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

def printTabuleiro(num1):
    for coluna in range(5):
        print(num1[coluna])

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