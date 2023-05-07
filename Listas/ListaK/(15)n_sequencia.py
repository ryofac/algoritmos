from io_utils import *
from math_utils import *

def main():
    clear_screen()
    label = "Dada a sequência (1, 3, 6, 10, 15,...)"
    title(label)
    # Entrada
    ultimo_termo = pedir_inteiro('Até qual termo n você quer a sequência?: ')
    clear_screen()
    
    # Processamento
    title((" Sequência: ").center(len(label), '-'), upper= True)
    resultado_anterior = 0
    
    for c in range(1, ultimo_termo + 1):
        soma = resultado_anterior + c # A soma sempre é na forma resultado anterior + contador_implementado
        resultado_anterior = soma
        # Saída
        print(f'({c})/({ultimo_termo}):  {soma}'.center(len(label)))
main()
