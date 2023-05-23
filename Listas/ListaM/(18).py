import str_utils as st
import io_utils as io

def main():
    texto = input('Digite a frase a ser analisada: ')

    substtr = input('Digite a substring a ser retirada da frase: ')
    
    while not st.contem_substring(texto, substtr):
        print('Substring inválida!')
        substtr = input('Digite a substring a ser retirada da frase: ')
    
    substituto = input('Substituir por qual substring? \n > ')
    
    print(texto, '>>', st.substituir_substr(texto, substtr, substituto))
   
    
main()