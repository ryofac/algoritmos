from utils import *
from os import system

def main():
    label = 'Gerador de Tabuada'
    title(label)
    numero_inicial = 1
    contador_parcial = 0
    while numero_inicial <= 10:
        multiplicacao =  contador_parcial * numero_inicial
        print(f'{numero_inicial} x {contador_parcial} = {multiplicacao}'.center(len(label)))
        contador_parcial += 1
        if contador_parcial == 10:
            print('=' * len(label))
            enter = input('...<Enter>')
            system("clear")
            contador_parcial = 0
            numero_inicial += 1
    title('Obrigado por usar o tabuada.py!', estrelado= True)

main()