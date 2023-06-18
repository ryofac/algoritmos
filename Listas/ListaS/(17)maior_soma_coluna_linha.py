from matrizes_utils import *
from vetor_utils import *
from io_utils import *

def main():
    ordem = obter_inteiro('Digite a ordem da matriz: ', tipo="+")
    matriz = obter_matriz_quadrada(ordem, inline=True)
    
    print(f'A maior coluna é {obter_coluna_maior_soma(matriz) + 1}')
    print(f'A maior linha é {obter_linha_maior_soma(matriz) + 1}')


def obter_coluna_maior_soma(matriz):
    maior_soma = reduzir(obter_colunas(matriz, 0), lambda x, y: x + y, atual= 0)
    maior_coluna = 0
    for i in range(len(matriz)):
        soma = reduzir(obter_colunas(matriz, i), lambda x, y: x + y, atual= 0)
        if soma > maior_soma:
            maior_soma = soma
            maior_coluna = i
    return maior_coluna

def obter_linha_maior_soma(matriz):
    maior_soma = reduzir(obter_linhas(matriz, 0), lambda x, y: x + y, atual= 0)
    maior_linha = 0
    for i in range(len(matriz)):
        soma = reduzir(obter_linhas(matriz, i), lambda x, y: x + y, atual= 0)
        if soma > maior_soma:
            maior_soma = soma
            maior_linha = i
    return maior_linha
    
main()