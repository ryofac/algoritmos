import io_utils as io
import str_utils as st
def main():
    texto = str(input('O que você quer que seja imprimido na vertical? \n> '))
    deslocamento = io.obter_inteiro('Qual é a coluna que você quer colocar? => ')
    
    print_vertical(deslocamento, texto)

def print_vertical(deslocamento: int, texto: str) -> None:
    for caracter in texto:
        print(' '  * deslocamento + caracter)

main()