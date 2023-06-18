import io_utils as io
from matrizes_utils import *
import vetor_utils as vt
# Leia uma matriz quadrada de ordem N, calcule e escreva a soma dos elementos da diagonal principal,
# a soma dos elementos da diagonal secundária e a soma dos elementos que não estão na diagonal
# principal nem na diagonal secundária

def main():
    n = io.obter_inteiro('Qual o tamanho da matriz que você quer? \n> ')
    matriz = io.obter_matriz_quadrada(n, inline=True)
    io.mostrar_matriz(matriz)
    principal = filtrar_matriz(matriz, lambda x, y: x == y)
    secundaria = filtrar_matriz(matriz, lambda i, j: j == len(matriz) - i - 1)
    demais = filtrar_matriz(matriz, lambda i, j: not(i == j or j == len(matriz) - i - 1))
    
    print('PRINCIPAL: ', somatorio(principal))
    print('SECUNDARIA: ', somatorio(secundaria))
    print('DEMAIS: ', somatorio(demais))
    
def somatorio(vetor):
    return reduzir(vetor, lambda x, y: x + y, atual=0)

main()