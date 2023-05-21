def main():
    frase = input('Digite uma frase para ter cada caractere seu caractere duplicado: ' )
    frase = duplicar_cada_caracter(frase)
    
    print(frase)
    
def duplicar_cada_caracter(texto):
    novo_texto = ''
    for char in texto:
        novo_texto += char * 2
    return novo_texto
main()