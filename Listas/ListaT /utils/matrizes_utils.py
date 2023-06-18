import sys
sys.path.append("./utils")
from vetor_utils import *

def eh_matriz_quadrada(vetor):
    for i in range(len(vetor)):
        if type(vetor[i]) != list or len(vetor[i]) != len(vetor[0]) :
            return False
    return True


def obter_diagonal(matriz, diagonal='p'):
    out = []
    for i in range(len(matriz)):
        if diagonal == 'p':
            out.append(matriz[i][i])
        if diagonal == 's':
            out.append(matriz[len(matriz)- i - 1][i])
    return out


def obter_colunas(matriz, *indexes):
    out = []
    for index in indexes:
        coluna = []
        for i in range(len(matriz)):
            coluna.append(matriz[i][index])
        out.append(coluna)
    return out
            


def filtrar_matriz(matriz, funcao_filtro: lambda i, j : bool, regra = lambda x: x):
    out = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if funcao_filtro(regra(i), regra(j)):
                out.append(matriz[i][j])
    return out 
            

def transpor_matriz_quadrada(matriz):
    matriz_transposta = []
    for linha in range(len(matriz)):
        out = []
        for elemento in range(len(matriz[linha])):
            out.append(matriz[elemento][linha])
        matriz_transposta.append(out)
    return matriz_transposta


def obter_linhas(matriz, *indexes):
    out = []
    for index in indexes:
        out.append(matriz[index])
    return out

