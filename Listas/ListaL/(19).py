def main():
    numero_limite = int(input('Digite o número limite: '))
    somador = 0

    for c in range(numero_limite, 0, -1):
        somador += 1/c
        print(f'1/{c} +')
        
    print('A soma de tudo é ', somador)
    
main()