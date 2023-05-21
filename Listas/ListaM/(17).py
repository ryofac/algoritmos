import str_utils as st
import io_utils as io

def main():
    frase = str(input('Digite uma frase para ser extraida a substring: '))
    inicio = io.obter_inteiro('Digite o início da substring: ')
    final = io.obter_inteiro('Digite o final do intevalo da substring: ')
    
    
    while inicio > final:
        print('Valor inválido, o início é maior que o final!')
        inicio = io.obter_inteiro('Digite o início da substring: ')
        final = io.obter_inteiro('Digite o final do intevalo da substring: ')
        
        
    while inicio > st.obter_tamanho(frase) or final > st.obter_tamanho(frase):
        print('A string é menor que isso! ')
        inicio = io.obter_inteiro('Digite o início da substring: ')
        final = io.obter_inteiro('Digite o final do intevalo da substring: ')
        
    
    substring = st.substring_tamanho(frase, inicio, final)
    
    print(f'>> {substring} << ')
    
    
main()