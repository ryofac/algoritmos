# Entrada:
valor_dolar = float(input('Qual o valor atual do dolar?\n >> '))
real = float(input('Qual o valor a ser convertido em real (R$)?\n >> '))

# Processamento:
valor_final = valor_dolar * real

# Saída: 
print(f'O valor dessa conversão é de R$ {valor_final:.2f}')
