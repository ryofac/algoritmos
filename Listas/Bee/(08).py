def main():
    # Entrada
    numero_a = int(input())
    numero_b = int(input())
    numero_c = int(input())
    numero_d = int(input())
    # Processamento
    diferenca = calcular_diferenca_de_produtos_de(numero_a, numero_b, numero_c, numero_d)
    # Saida
    print(f'DIFERENCA = {diferenca}')
def calcular_diferenca_de_produtos_de(a, b, c, d):
        return (a * b) - (c * d)
main()