def main():
    
    print('1/2 - 1/3 + 1/4 - 1/4 + ... 1/N')
    
    numero_final = int(input('Digite os números que você quer somar na sequência: '))
    
    contador = 0
    soma = 0
    
    while contador < numero_final:
        contador += 1
        soma += 1/contador if contador % 2 == 0 else soma - 1/contador
        print('1/',contador, '+' if contador % 2 == 0 else '-', end = ' ')
        
    print('\b\b = {:.2f}'.format(soma))
    
    
    
    
main()