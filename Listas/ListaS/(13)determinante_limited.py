from io_utils import *
from matrizes_utils import *
from vetor_utils import *

def main():
    matriz = obter_matriz_quadrada(2, True)
    
    produto_secundaria = reduzir(obter_diagonal(matriz, 's'), lambda x, y: x * y, atual= 1)
    produto_principal = reduzir(obter_diagonal(matriz, 'p'), lambda x, y: x * y, atual = 1)
    
    print(f'A determinante dessa 2x2 é {produto_secundaria - produto_principal}')

    
main()