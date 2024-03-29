def main():
    largura, altura, profundidade, raio_esfera = [float(x) for x in input().split()]
    
    print('S') if cabe_caixa(largura, altura, profundidade, raio_esfera) else print('N')


def cabe_caixa(largura, altura, profundidade, raio_esfera):
    diametro = raio_esfera * 2
    diagonal_caixa = (altura ** 2 + profundidade ** 2 + largura ** 2) ** 0.5
    return diagonal_caixa <= diametro
main()
