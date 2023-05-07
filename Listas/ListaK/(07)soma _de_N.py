from io_utils import *
def main():
    clear_screen()
    title('Somador de Números')
    numeroN = pedir_inteiro("Me diga um número natural: ", tipo="+")
    numero = 0
    soma_de_tudo = 0
    for c in range(numero, numeroN):
        soma_de_tudo += numero
        print(f'{numero}', end=" ")
        print('+', end=" ") if numero < numeroN-1 else print('')
        numero +=1
    printslow(f"\nA soma de todos os números antes dele é {soma_de_tudo}")
main()

