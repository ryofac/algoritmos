# -*- coding: utf-8 -*-

def calcular_media(num1, num2):
    return (num1 * 3.5 + num2 * 7.5) / 11
    
def main():
    # Entrada
    numero_a = float(input())
    numero_b = float(input())
    # Processamento
    media = calcular_media(numero_a, numero_b)
    # Saida
    print(f'MEDIA = {media:.5f}')

main()
