from io_utils import *
from math_utils import *

def main():
    title("Dada a sequência (1, 3, 6, 10, 15,...)")
    ultimo_termo = pedir_inteiro('Até qual termo n você quer a sequência?: ')
    resultado_anterior = 0
    contador = 1
    while contador < ultimo_termo + 1:
        soma = resultado_anterior + contador # A soma sempre é na forma resultado anterior + contador_implementado
        contador +=1
        resultado_anterior = soma
        print('>', soma)
main()
