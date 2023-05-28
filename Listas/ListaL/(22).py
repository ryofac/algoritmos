def main():
    #Entrada
    numero_fichas = int(input('Digite o numero de fichas: '))
    
    id_maior = 0
    id_menor = 0

    peso_maior = -float('inf')
    peso_menor = float('inf')
    
    #Processamento
    for i in range(numero_fichas):
        peso_boi = float(input('Digite o peso do boi: '))
        if peso_boi > peso_maior:
            peso_maior = peso_boi
            id_maior = i
           
        if peso_boi < peso_menor:
            peso_menor = peso_boi
            id_menor = i

    #Saída
    print(f'Boi com maior peso: {peso_maior} ID: {id_maior}')
    print(f'Boi com menor peso: {peso_menor} ID: {id_menor}')

main()