def main():
    # Entrada
    num_a = int(input())
    num_b = int(input())
    # Processamento
    produto = produto_de(num_a, num_b)
    # Saída
    print(f'PROD = {produto}')
    
def produto_de(a,b):
    return a * b
    
main()