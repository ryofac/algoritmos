# Entrada
salario = float(input('Digite aqui o seu salário para calcular seu aumento:\n >> R$'))

# Processamento
aumento = salario + 0.25 * salario

# Saída
print(f'Seu aumento foi de R$ {(0.25 * salario):.2f} e seu novo salário é de R$ {aumento}')