def main():
    # Saida
    
    dias = int(input())

    # Processamento
    anos = dias // 360
    resto = dias % 360
    meses = resto // 30
    resto = resto % 30
    dias = resto

    # Saída
    print(f'{anos} ano(s)')
    print(f'{meses} mes(es)')
    print(f'{dias} dia(s)')

main()