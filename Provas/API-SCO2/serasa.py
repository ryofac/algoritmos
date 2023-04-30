from math_utils import *
from io_utils import *

def main():
   title('CATEGORIAS: ')
   criterio_a = pedir_inteiro('A: ')
   criterio_b = pedir_inteiro('B: ')
   criterio_c = pedir_inteiro('C: ')
   
   totala = criterio_a_total(criterio_a)
   totalb = criterio_b_total(criterio_b)
   totalc = criterio_c_total(criterio_c)
   
   totala2 = criterio_a_total(criterio_a, tipo=2)
   totalb2 = criterio_b_total(criterio_b, tipo=2)
   totalc2 = criterio_c_total(criterio_c, tipo=2)
   
   pontos_totais_1 = obter_pontos_totais(totala, totalb, totalc)
   pontos_totais_2 = obter_pontos_totais(totala2, totalb2, totalc2)
   
   title('Classificação:')
   print(f'SERASA.1: {pontos_totais_1:.0f} --> {definir_classificacao(pontos_totais_1, tipo=1)}')
   print(f'SERASA.2: {pontos_totais_2:.0f} --> {definir_classificacao(pontos_totais_2, tipo=2)}')

def obter_pontos_totais(a, b, c):
    soma = a + b + c
    return soma * 10


def criterio_a_total(a, tipo = None):
    if tipo == 2:
        return a * 0.62
    return a * 0.26


def criterio_b_total(b, tipo = None):
    if tipo == 2:
        return b * 0.19
    return b * 0.57


def criterio_c_total(c, tipo = None):
    if tipo == 2:
        return c * 0.19
    return c * 0.17


def definir_classificacao(pontos, tipo = None):
    if tipo == 1:
        if pontos <= 400:
            return 'Baixo'
        elif pontos <= 600:
            return 'Regular'
        elif pontos <= 800:
            return 'Bom'
        else:
            return 'Muito bom!'
    if tipo == 2:
        if pontos <= 300:
            return 'Baixo'
        if pontos <= 500:
            return 'Regular'
        if pontos <= 700:
            return 'Bom'
        else:
            return 'Muito bom!'
    


    
main()