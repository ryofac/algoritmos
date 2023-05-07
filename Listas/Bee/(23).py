def main():
    # entrada
    valor_a, valor_b, valor_c = list(map(float, input().split()))
    # processamento
    delta = calcular_delta(valor_a, valor_b, valor_c)
    if delta < 0 or valor_a == 0:
        print('Impossivel calcular')
        return 
    x1 = (-valor_b + (delta ** (1/2)))/(2 * valor_a)
    x2 = (-valor_b - (delta ** (1/2)))/(2 * valor_a)
    # saida
    print(f'R1 = {x1:.5f}')
    print(f'R2 = {x2:.5f}')
def calcular_delta(a, b ,c):
    return (b ** 2) - (4 * a * c)

main()
