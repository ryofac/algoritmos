# Escreva o maior quadrado antes de um número N dado:

from math_utils import *
from io_utils import *
def main():
    label = 'Buscador de quadrado menor que o número digitado'
    title('Buscador de quadrado menor que o número digitado', upper=True)
    printslow('(Nem um pouco específico)'.center(len(label)),speed= 0.03)
    num_verificar = pedir_inteiro()
    inicial = 1
    ao_quadrado = float('inf')
    
    while True:
        inicial += 1
        ao_quadrado = (inicial) ** 2
        if ao_quadrado > num_verificar:
            ao_quadrado = (inicial-1) ** 2
            break        
    if ao_quadrado == num_verificar:
        title(f'O quadrado mais próximo achado foi ele mesmo, {ao_quadrado}')
    else:   
        title(f'O quadrado mais próximo achado foi {ao_quadrado}')

main()