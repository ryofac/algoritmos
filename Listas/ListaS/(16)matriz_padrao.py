from matrizes_utils import *
from vetor_utils import *
from io_utils import *

def main():
    ordem = obter_inteiro('Digite a ordem da matriz: ', tipo="+")
    valor_padrao = obter_inteiro('Digite o valor padrão:')
    matriz = obter_matriz_padrao(ordem, valor_padrao)
    mostrar_matriz(matriz)
    
def obter_matriz_padrao(ordem, valor_padrao):
    out = []
    for i in range(ordem):
        linha = []
        for i in range(ordem):
            linha.append(valor_padrao)
        out.append(linha)
    return out

main()