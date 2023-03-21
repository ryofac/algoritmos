def main():
    # Entrada
    tempF = float(input('Digite a temperatura em Farenheit: '))

    # Processamento
    tempC = converterCelsius(tempF)

    # Saída
    print(f'A temperatura em Farenheit é de {tempC:.2f}°C')
    

def converterCelsius(tempF):
    celcius = (5 * tempF - 160) / 9
    return celcius

main()