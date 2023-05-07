from io_utils import *
from math_utils import *

def main():
    clear_screen()
    title('Buscador de números primos', upper= True)

    printslow('Digite os limites do intervalo...')
    # Entrada
    limite_inferior = pedir_inteiro('... Início: ')
    limite_superior = pedir_inteiro('... Final: ')
    
    # Processamento:
    
    # Check
    while limite_superior < limite_inferior or limite_inferior == limite_superior: 
        printslow('Intevalo inválido!')
        printslow('Vamos novamente...')
        limite_inferior = pedir_inteiro('...O Início: ', tipo= '+')
        limite_superior = pedir_inteiro('...O Final: ', tipo= '+')

    # Saída
    title(f"Números primos entre {limite_inferior} e {limite_superior}:") 

    for c in range(limite_inferior, limite_superior): # Percorre o intervalo, for numérico
        if eh_primo(c):
            print(f'>  {c}')

            
main()