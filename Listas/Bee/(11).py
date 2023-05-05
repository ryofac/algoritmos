def main():
    # Entrada
    codigo1, valor1, preco1 = list(map(float, input().split()))
    codigo2, valor2, preco2 = list(map(float, input().split()))
    # Processamento
    compra_1 = valor_compra(valor1, preco1)
    compra_2 = valor_compra(valor2, preco2)
    total = compra_1 + compra_2
    # Saida
    print(f'VALOR A PAGAR: R$ {total:.2f}')

def valor_compra(quantidade, preco):
    return quantidade * preco

main()