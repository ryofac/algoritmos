def main():
    # Entrada
    velocidade = int(input())
    tempo = int(input())
    # Processamento
    distancia = velocidade * tempo
    consumo = calcular_consumo(distancia)
    # Saida
    print(f'{consumo:.3f}')
def calcular_consumo(distancia):
    return distancia / 12
main()