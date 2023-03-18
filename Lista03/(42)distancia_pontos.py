 # Programa que calcula a distância entre dois pontos fornecidos: 
from math import sqrt

def main():
    # Entrada:
    x1 = float(input('x1: '))
    x2 = float(input('x2: '))
    y1 = float(input('y1: '))
    y2 = float(input('y2: '))
    
    #Processamento:
    distancia = distanciaPontos(x1,x2,y1,y2)
    
    # Saída:
    print(f'A distância entre os pontos dados é de : {distancia} unidades')

# Função que calcula a distância entre dois pontos
def distanciaPontos(x1,x2,y1,y2):
    dist = sqrt((x2-x1)**2 + (y2-y1)**2)
    return dist
    

