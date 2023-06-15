def main():
    numero_analisado = int(input('Digite o número que você quer analisar: '))
    
    while numero_analisado != 0:
        contador = 0
        while contador < numero_analisado:
            contador +=1
            if numero_analisado % contador == 0:
                print('>', contador, f'é divisor de {numero_analisado}')
        numero_analisado = int(input('Digite o número que você quer analisar: '))
    
main()