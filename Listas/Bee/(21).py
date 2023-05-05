def main():
    # Entrada
    
    value = int(input())
    not_int_value = value - int(value)
    # Processamento
    notas_100 = value // 100
    resto = value % 100
    notas_50 = resto // 50
    resto = resto % 50
    notas_20 = resto // 20
    resto = resto % 20
    notas_10 = resto // 10
    resto = resto % 10
    notas_5 = resto // 5
    resto = resto % 5
    notas_2 = resto // 2
    resto = resto % 2
    notas_1 = resto
    
    # Saída
    print(f'{notas_100} nota(s) de R$ 100,00')
    print(f'{notas_50} nota(s) de R$ 50,00')
    print(f'{notas_20} nota(s) de R$ 20,00')
    print(f'{notas_10} nota(s) de R$ 10,00')
    print(f'{notas_5} nota(s) de R$ 5,00')
    print(f'{notas_2} nota(s) de R$ 2,00')
    print(f'{notas_1} nota(s) de R$ 1,00')
main()