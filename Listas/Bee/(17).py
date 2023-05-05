def main():
    # Entrada
    distancia = int(input())
    # Processamento
    tempo = calcular_tempo(distancia)
    # Saída
    print(f'{tempo} minutos')
    
def calcular_tempo(distancia):
    return distancia * 2  # a cada 2 minutos, ele aumenta a distancia em 1km
main()