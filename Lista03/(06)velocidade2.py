# Entrada

def main():
    vel_kh = float(input('Digite o número em km/h \n >> '))

    # Processamento
    vel_ms = velocidade_ms(vel_kh)

    # Saída
    print(f'A velocidade é de {vel_ms:.2f} m/s')

def velocidade_ms(vel_kh): # Recebe um valor em km/h e faz a conversão 
    return vel_kh / 3.6

main()