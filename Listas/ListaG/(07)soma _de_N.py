from utils import *
def main():
    title('Somador de Números', upper=True)
    numeroN = pedir_inteiro("Me diga um número natural: ", tipo='+')
    numero = 0
    soma_de_tudo = 0
    while numero < numeroN:
        soma_de_tudo += numero
        print(f'{numero}', end= ' + ')
        numero +=1
    printslow(f"\nA soma de todos os números antes dele é {soma_de_tudo}")
main()