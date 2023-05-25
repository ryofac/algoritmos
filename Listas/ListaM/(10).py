def main():
    # Entrada
    palavra = str(input('Digite a palavra a ser analisada: '))
    
    # Processamento
    palavra_inversa = inverter_palavra(palavra)
    
    # Saida
    if palavra == palavra_inversa:
        print('Essa palavra é palíndroma!!')
        print(f'{palavra} = {palavra_inversa}')
    else:
        print('Essa palavra não é palíndroma!!')
        print(f'{palavra} diferente de {palavra_inversa}')
    
def inverter_palavra(palavra):
    palavra_inversa = ''
    for i in range(len(palavra)):
        palavra_inversa += palavra[len(palavra) - i - 1]
    return palavra_inversa
        
main()