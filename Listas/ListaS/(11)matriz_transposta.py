import io_utils as io
def main():
    n = io.obter_inteiro('Qual o tamanho da matriz que você quer? \n> ')
    matriz = io.obter_matriz_quadrada(n, inline=True)
    print(matriz)
    matriz_transposta = transpor_matriz_quadrada(matriz)
    print('MATRIZ OBTIDA:')
    io.mostrar_matriz(matriz)
    print("TRANSPOSTA:")
    io.mostrar_matriz(matriz_transposta)
    
def transpor_matriz_quadrada(matriz):
    matriz_transposta = []
    for linha in range(len(matriz)):
        out = []
        for elemento in range(len(matriz[linha])):
            out.append(matriz[elemento][linha])
        matriz_transposta.append(out)
    return matriz_transposta
main()