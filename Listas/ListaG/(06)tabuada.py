from io_utils import *
from os import system

def main():
    clear_screen()
    label = 'Gerador de Tabuada'
    title(label, upper=True)
    numero_inicial = 1
    contador_parcial = 0
    while numero_inicial <= 10:
        multiplicacao =  contador_parcial * numero_inicial
        print(f'{numero_inicial} x {contador_parcial} = {multiplicacao}'.center(len(label)))
        contador_parcial += 1
        if contador_parcial == 10:
            print('=' * len(label))
            input('...<Enter>')
            system("clear")
            print('=' * len(label))
            print(f'({numero_inicial + 1})/(10)'.center(len(label)))
            contador_parcial = 0
            numero_inicial += 1
    system("clear") 
    title('Obrigado por usar o tabuada.py!', estrelado= True)

main()