# Leia um limite superior e inferior e liste os multiplos de um número entre eles

from io_utils import title, printslow, pedir_inteiro
from math_utils import eh_multiplo

def main():
    title('DESCOBRIDOR DE MÚLTIPLOS')
    printslow('Digite os números do intervalo...')
    limite_inferior = pedir_inteiro('...O limite inferior: ', tipo= '+')
    limite_superior = pedir_inteiro('...O limite superior: ', tipo= '+')
    
    while limite_superior < limite_inferior or limite_inferior == limite_superior: # check_interval
        printslow('Intevalo inválido!')
        printslow('Vamos novamente...')
        limite_inferior = pedir_inteiro('...O limite inferior: ', tipo= '+')
        limite_superior = pedir_inteiro('...O limite superior: ', tipo= '+')
        
    numero = pedir_inteiro('Qual o número que você quer saber os múltiplos nesse intervalo? \n>> ', tipo= '+')
    candidato = limite_inferior
    
    title(f'Múltiplos de {numero} entre {limite_inferior} e {limite_superior}')

    for c in range(limite_superior):
        if eh_multiplo(candidato, numero):
            print(f'> {candidato}')
        
        candidato += 1


main()