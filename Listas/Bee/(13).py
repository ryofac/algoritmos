def main():
    # Entrada
    valor_a, valor_b, valor_c = list(map(float, input().split()))
    
    # Processamento
    triangulo = calcular_area_triangulo(valor_a, valor_c)
    circulo = calcular_area_circulo(valor_c)
    trapezio = calcular_area_trapezio(valor_a, valor_b, valor_c)
    quadrado = calcular_area_quadrado(valor_b)
    retangulo = calcular_area_retangulo(valor_a, valor_b)
    
    # Saida
    print(f'TRIANGULO: {triangulo:.3f}')
    print(f'CIRCULO: {circulo:.3f}')
    print(f'TRAPEZIO: {trapezio:.3f}')
    print(f'QUADRADO: {quadrado:.3f}')
    print(f'RETANGULO: {retangulo:.3f}')
    
def calcular_area_triangulo(base, altura):
    return (base * altura )/2
def calcular_area_circulo(raio):
    pi = 3.14159
    return pi * raio ** 2
def calcular_area_trapezio(baseMaior, baseMenor, altura):
    return ((baseMaior + baseMenor) * altura) / 2
def calcular_area_quadrado(lado):
    return lado ** 2
def calcular_area_retangulo(lado1, lado2):
    return lado1 * lado2
main()
