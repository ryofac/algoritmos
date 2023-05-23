from str_utils import *

def main():
    # Entrada 
    frase = str(input('Os números dessa frase ficarão em extenso: '))
    
    # Processamento
    frase_nova = transformar_numeros_extenso(frase)
    
    # Saída
    print('> ', frase_nova)
    
    
    

def transformar_numeros_extenso(frase):
    numeros_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove')
    
    nova_frase = ''
   
    for char in frase:
        tem_num = False
        for num in range(10):
            if str(num) == char:
                nova_frase += numeros_extenso[num]
                tem_num = True
        if not tem_num:
            nova_frase += char
            
    return nova_frase
main()