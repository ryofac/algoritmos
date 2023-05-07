from io_utils import *
from math_utils import contar_ate

def main():
    clear_screen()
    # Entrada
    title('Contador de números', upper=True)
    # Processamento
    num = pedir_inteiro("Até onde é pra contar? \n> ", tipo= '+')
    for num in range(1, num+1):
        print(num, '...')
        
    # Saída
    title('FIM!', estrelado= True)


main()

