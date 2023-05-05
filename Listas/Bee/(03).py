def main():
    # Entrada
    raio = float(input())
    # Processamento
    area = calcular_area(raio)
    # Saída
    print(f'A={area:.4f}')

def calcular_area(raio):
    pi = 3.14159
    return pi * raio ** 2

main()

