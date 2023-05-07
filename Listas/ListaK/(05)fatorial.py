from io_utils import *
from math_utils import *
def main():
    title('Máquina de Fatorial')
    num = pedir_inteiro(tipo="+")
    num_fatorial = fatorial(num)
    printslow(f'{num}! = {num_fatorial}')
    
def factorial(num): # Função interessante usando o conceito de recursividade!
    if num == 1:
        return 1
    return num * factorial(num-1)

main()