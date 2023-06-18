from matrizes_utils import *
from vetor_utils import *
from io_utils import *


def main():
    # entrada
    ordem = obter_inteiro('Digite a ordem da matriz: ', tipo="+")
    
    # processamento
    matriz = obter_matriz_quadrada(ordem, inline=True)
    matriz_transposta = transpor_matriz_quadrada(matriz)
    
    # saída
    print('É simétrica') if matriz == matriz_transposta else print('Não é simétrica')
    
main()