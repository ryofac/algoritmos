def main():
    # Entrada
    valor_a, valor_b, valor_c = list(map(int, input().split()))
    # Processamento
    maior = maior_entre(valor_a, valor_b, valor_c)
    # Saida
    print(f'{maior} eh o maior')
    
def maior_entre(a,b,c):
    maior_entre_a_e_b = (a+b + abs(a-b)) / 2
    return (maior_entre_a_e_b + c + abs(maior_entre_a_e_b -c)) /2
main()