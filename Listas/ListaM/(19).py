import io_utils as io
import str_utils as st

def main():
    numero_binario = input('Digite um numero binario: ').strip()
    
    while not (st.contem_caracter(numero_binario, '1') and st.contar_caractere(numero_binario, '0')):
        print('Valor não binário!')
        numero_binario = input('Digite um numero binario:').strip()
        
    decimal = binario_decimal(numero_binario)
    
    print(f'O valor decimal é de: {decimal}')


def binario_decimal(num):
    decimal = 0
    num = str(num)
    
    for n in range(len(num)):
        decimal += int(num[n]) * 2 ** (len(num)- n - 1)
        
    return decimal
        
        
    

main()