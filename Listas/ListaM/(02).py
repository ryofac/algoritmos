def main():
    frase = input('Digite a frase a ser cortada em linhas: ')
    print_por_linha(frase)

def print_por_linha(texto):
    for char in texto:
        print(char)
main()