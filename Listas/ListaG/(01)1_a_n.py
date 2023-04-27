from io_utils import *
from math_utils import contar_ate

def main():
    clear_screen()
    title('Contador de números', upper=True)
    num = pedir_inteiro("Até onde é pra contar? \n> ", tipo= '+')

    contar_ate(num)

    clear_screen()
    title('FIM!', estrelado= True)


main()

