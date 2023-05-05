import os
# -*- coding: utf-8 -*-

def calcular_media(num1, num2, num3):
    return (num1 * 2 + num2 * 3 + num3 * 5) / 10
    
def main():
    # Entrada
    numero_a = float(input())
    numero_b = float(input())
    numero_c = float(input())
    # Processamento
    media = calcular_media(numero_a, numero_b, numero_c)
    # Saida
    print(f'MEDIA = {media:.1f}')

main()