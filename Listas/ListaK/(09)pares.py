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

    for c in range(limite_inferior, limite_superior):
        if eh_par(c):
            print(f'>  {c}')

main()