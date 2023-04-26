from io_utils import printslow, pedir_inteiro, title
from math_utils import eh_par

def main():
    title('Buscador de números pares', upper= True)

    printslow('Digite os limites do intervalo...')
    limite_inferior = pedir_inteiro('... Início: ')
    limite_superior = pedir_inteiro('... Final: ')
    
    if limite_superior < limite_inferior or limite_inferior == limite_superior: # check_interval
        printslow('Intevalo inválido!')
        printslow('Vamos novamente...')
        limite_inferior = pedir_inteiro('...O Início: ', tipo= '+')
        limite_superior = pedir_inteiro('...O Final: ', tipo= '+')

    title(f"Números pares entre {limite_inferior} e {limite_superior}:")

    while limite_inferior <= limite_superior:
        limite_inferior += 1 # O Limite "cresce" até chegar ao valor do limite superior
        if eh_par(limite_inferior):
            print(f'>  {limite_inferior}')

main()