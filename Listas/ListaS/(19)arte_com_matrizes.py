from matrizes_utils import *
from vetor_utils import *
from io_utils import *

def main():
    matriz = []
    cont = 1
    n = 5
    for i in range(n):
        linha = []
        for j in range(n):
            if j == n-1 or j == 0 or i == 0 or i == 4:
                linha.append(1)
            elif j == 3 or j == 1 or i == 1 or i == 3:
                linha.append(2)
            else:
                linha.append(3)
        matriz.append(linha)
    mostrar_vetor(matriz)
main()