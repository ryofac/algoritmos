def main():
    # Entrada
    raio = int(input())
    # Processamento
    volume = calcular_volume(raio)
    # Saida
    print(f'VOLUME = {volume:.3f}')
    
def calcular_volume(raio):
    pi = 3.14159
    return  (4/3) * pi * raio ** 3
main()