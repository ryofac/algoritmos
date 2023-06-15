def main():
    print('1/2 - 1/3 + 1/4 - 1/4 + ... 1/N')
    
    numero_final = int(input('Digite os números que você quer somar na sequência: '))
    
    soma = 0
    
    for i in range(1, numero_final + 1):
        soma += 1/i if i % 2 == 0 else soma - 1/i
        print('1/', i , '+' if i % 2 == 0 else '-', end = ' ')
        
    print('\b\b = {:.2f}'.format(soma))
    
main()