import io_utils as io
import str_utils as st
def main():
    texto = str(input('O que você quer que seja imprimido na diagonal? \n> '))
    
    print_diagonal(texto)

def print_diagonal(texto: str) -> None:
    for i in range(len(texto)):
        print(' ' * i + texto[i])

main()