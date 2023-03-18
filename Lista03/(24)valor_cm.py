def main():
    # Entrada
    valorCm = float(input('Digite o valor equivalente em centímetro \n >> '))

    #Processamento
    valorM = converter_m(valorCm)

    #Saída
    print(f'O valor total é de {valorM:.2f} m')

def converter_m(cm):
    return cm / 1000

main()