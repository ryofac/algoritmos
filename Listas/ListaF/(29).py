def main():
    num = input('Digite o número de 4 dígitos a ser verificado: ')
    
    if eh_quadrado_perfeito(num):
        print('É um quadrado perfeito!')
    else:
        print('Não é um quadrado perfeito :(')
    


def eh_quadrado_perfeito(num):
    dezenas = int(num[:2])
    unidades = int(num[2:])
    
    return dezenas + unidades == int(num) ** 0.5
    
main()