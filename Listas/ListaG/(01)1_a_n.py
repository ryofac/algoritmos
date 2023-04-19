import sys
sys.path.append("./utils")
from utils import *

def main():
    title('Contador de números')
    num = pedir_inteiro("Me diga um número:\n> ", tipo= '+')

    contar_ate(num)

    printslow('FIM!')


main()

