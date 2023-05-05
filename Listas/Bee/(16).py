def main():
    # Entrada
     valor_x, valor_y = list(map(float, input().split()))
     valor_x2, valor_y2 = list(map(float, input().split()))
     # Processamento
     distancia = distance(valor_x, valor_y, valor_x2, valor_y2)
     # Saida
     print(f'{distancia:.4f}')
def distance(x, y, x2, y2):
    return ((x-x2) ** 2 + (y - y2) ** 2) ** 0.5
main()