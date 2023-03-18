def main():
    # Entrada
    base = float(input('Digite o valor base de um triângulo: '))
    altura = float(input('Digite o valor da altura desse mesmo triângulo: '))

    # Processamento
    area = calcular_area(base, altura)

    # Saída
    print(f'A área desse triângulo é de {area} unidades de área')

def calcular_area(base, altura):
    area = base * altura / 2
    return area

main()