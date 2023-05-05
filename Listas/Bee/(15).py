# -*- coding: utf-8 -*-

def main():
    # Entrada
    distancia = float(input())
    consumo = float(input())
    # Processamento
    consumo_por_litro = calcular_km_l(distancia, consumo)
    # Saida
    print(f'{consumo_por_litro:.3f} km/l')
def calcular_km_l(distancia, consumo):
    return distancia / consumo
main()
