from io_utils import *
from math_utils import contar_ate

def main():
    title('Contador de números', upper=True)
    num = pedir_inteiro("Até onde é pra contar? \n> ", tipo= '+')

    contar_ate(num)


    title('FIM!', estrelado= True)


main()

