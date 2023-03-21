# Leia a idade de uma pessoa expressa em anos, meses e dias e escreva-a expressa apenas em dias.

# Entrada
anos = int(input('Digite a quantidade de anos: '))
meses = int(input('Digite a quantidade em meses: '))
dias= int(input('Digite a quantidade em dias: '))

# Processamento
# Considerando o ano e o mês comercial (360 dias e 30 dias, respectivamente)
dias_meses = meses * 30
dias_anos = (anos * 30) * 12
total = dias + dias_meses + dias_anos

# Saída
print(f'O total de dias de vida que você tem é de {total}')

