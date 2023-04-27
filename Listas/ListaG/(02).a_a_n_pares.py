from io_utils import *
def main():
    clear_screen()
    title('Sequência de Pares')
    num = pedir_inteiro(tipo= "+")
    contador = 0

    while contador != num:
            contador += 1
            if not contador % 2:
                print(contador, end=', ')
    printslow(f'\n...Esses são os números pares entre 1 e {num}')

main()