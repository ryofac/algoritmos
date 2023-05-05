def main():
    # Entrada
    num_a = int(input())
    num_b = int(input())
    # Processamento
    sum = soma_de(num_a, num_b)
    # Saída
    print(f'X = {sum}')
    
def soma_de(a, b):
    return a + b
main()