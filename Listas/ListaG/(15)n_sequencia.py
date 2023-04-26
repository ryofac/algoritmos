from io_utils import *
from math_utils import *

def main():
    clear_screen()
    label = "Dada a sequência (1, 3, 6, 10, 15,...)"
    title(label)
    ultimo_termo = pedir_inteiro('Até qual termo n você quer a sequência?: ')
    resultado_anterior = 0
    contador = 1
    clear_screen()
    title((" Sequência: ").center(len(label), '-'), upper= True)
    while contador < ultimo_termo + 1:
        soma = resultado_anterior + contador # A soma sempre é na forma resultado anterior + contador_implementado
        contador +=1
        resultado_anterior = soma
        print(f'({contador-1})/({ultimo_termo}):  {soma}'.center(len(label)))
main()
