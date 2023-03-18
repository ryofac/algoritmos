def main():
    
    # Entrada
    raio = float(input('Digite o valor do raio da circunferência: '))

    # Processamento
    comp = calcular_circunferencia(raio)

    # Saída
    print(f'O comprimento da circunferência é de {comp:.2f} unidades')

def calcular_circunferencia(raio):
    return raio * 3.14 * 2

main()
