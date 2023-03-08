# Leia a idade de uma pessoa expressa em dias e escreva-a expressa em anos, meses e dias

# Entrada
dias = int(input('Digite quantos dias você tem de vida'))

# Processamento
meses = dias // 30
dias_final = dias % 30
anos = meses // 12
meses_final = meses % 12

# Saída
print(f'{anos} anos {meses_final} meses {dias_final} dias')
