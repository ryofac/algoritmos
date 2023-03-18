def main():
    # Leia a idade de uma pessoa expressa em anos, meses e dias e escreva-a expressa apenas em dias.

    # Entrada
    print('Digite sua idade em: ')
    anos = int(input('Digite a quantidade de anos: \n>> '))
    meses = int(input('Digite a quantidade em meses: \n>> '))
    dias= int(input('Digite a quantidade em dias: \n>>'))

    # Processamento
    total = converter_dias(anos, meses, dias)


    # Saída
    print(f'A quantidade total de dias de vida que você tem é de {total} dias')


# Considerando o ano e o mês comercial (360 dias e 30 dias, respectivamente)
def converter_dias(anos, meses, dias):
    dias_meses = meses * 30
    dias_anos = (anos * 30) * 12
    total = dias + dias_meses + dias_anos
    return total
    
main()
