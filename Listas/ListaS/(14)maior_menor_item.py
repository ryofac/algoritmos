from matrizes_utils import *
from vetor_utils import *
from io_utils import *

def main():
    ordem = obter_inteiro('Digite a ordem da matriz: ', tipo="+")
    matriz = obter_matriz_quadrada(ordem, inline=True)
    print(buscar_maior_item(matriz))
    print(buscar_menor_item(matriz))
    
def buscar_maior_item(matriz):
    maior_item = matriz[0][0]
    maior_i = 0
    maior_j = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] >= maior_item:
                maior_item = matriz[i][j]
                maior_i = i
                maior_j = j
    return f'MAIOR: {maior_item} linha = {maior_i+1}, coluna = {maior_j+1}'
    

def buscar_menor_item(matriz):
    menor_item = matriz[0][0]
    menor_i = 0
    menor_j = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] <= menor_item:
                menor_item = matriz[i][j]
                menor_i = i
                menor_j = j
    return f'MENOR: {menor_item} linha = {menor_i+1}, coluna = {menor_j+1}'


            
main()