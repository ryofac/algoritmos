from matrizes_utils import *
from vetor_utils import *
from io_utils import *

def main():
    ordem = obter_inteiro('Digite a ordem da matriz: ', tipo="+")
    matriz = obter_matriz_quadrada(ordem, inline=True)
    
    soma_postivos = reduzir(matriz, lambda x, y: x + y, atual= 0, regra=lambda x: x > 0)
    soma_negativos = reduzir(matriz, lambda x, y: x + y, atual=0, regra= lambda x: x < 0)
    
    print(f'A soma dos positivos é {soma_postivos}')
    print(f'A soma dos negativos é {soma_negativos}')
    
main()