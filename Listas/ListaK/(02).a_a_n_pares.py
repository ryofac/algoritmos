from io_utils import *
def main():
    clear_screen()
    # Entrada
    title('Sequência de Pares')
    # Processamento
    num = pedir_inteiro(tipo= "+")
    for c in range(2, num + 1, 2): # For 'numerico'
        print(c)
    # Saída
    printslow(f'\n...Esses são os números pares entre 1 e {num}')

main()