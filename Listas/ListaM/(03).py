from str_utils import remover_caracter
def main():
    # Entrada
    frase = input('Digite a frase para a remoção de espaços: ')
    # Processamento
    frase = remover_caracter(frase, " ")
    print('Frase nova: ' + frase)
    
main()