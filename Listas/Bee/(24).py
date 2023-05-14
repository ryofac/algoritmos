
# -*- coding: utf-8 -*-
def main():
    # Entrada
    numero_check = float(input())
    # Processamento e Saída:
    if 0 <= numero_check <= 25:
        print('Intervalo [0,25]')
    if 25 < numero_check <= 50:
        print('Intervalo (25,50]')
    if 50 < numero_check <= 75:
        print('Intervalo (50,75]')
    if 75 < numero_check <= 100:
        print('Intervalo (75,100]')
    if numero_check < 0 or numero_check > 100:
        print('Fora de intervalo')
main()