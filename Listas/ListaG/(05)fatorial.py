from utils import *
def main():
    title('Máquina de Fatorial')
    num = pedir_inteiro(tipo="+")
    num_fatorial = factorial(num)
    
    printslow(f'{num}! = {num_fatorial}')
    
# def factorial(num): # Função interessante usando o conceito de recursividade!
#     if num == 1:
#         return 1
#     return num * factorial(num-1)

def factorial(num):
    multiplicador = 1
    contador = 0
    while contador < num:
        contador += 1
        multiplicador *= contador
    return multiplicador
        
main()