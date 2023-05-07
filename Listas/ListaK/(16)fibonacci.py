from io_utils import *
from math_utils import fib

def main():
    title('Formador de Sequência de Fibonacci', upper= True)
    
    n = pedir_inteiro('Qual o termo n da sequência você quer?: ')
    termo = 1
    
    for c in range(1, n+1):
        print('>', fib(termo))
        termo += 1
        

    
main()