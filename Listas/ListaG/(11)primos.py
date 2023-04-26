from io_utils import *
from math_utils import *

def main():
    clear_screen()
    title('Buscador de números primos', upper= True)

    printslow('Digite os limites do intervalo...')
    limite_inferior = pedir_inteiro('... Início: ')
    limite_superior = pedir_inteiro('... Final: ')
    
    while limite_superior < limite_inferior or limite_inferior == limite_superior: # check_interval
        printslow('Intevalo inválido!')
        printslow('Vamos novamente...')
        limite_inferior = pedir_inteiro('...O Início: ', tipo= '+')
        limite_superior = pedir_inteiro('...O Final: ', tipo= '+')

    title(f"Números ímpares entre {limite_inferior} e {limite_superior}:") 

    while limite_inferior <= limite_superior: # Percorre o intervalo
        limite_inferior += 1 # O Limite "cresce" até chegar ao valor do limite superior
        if eh_primo(limite_inferior):
            print(f'>  {limite_inferior}')

            
main()