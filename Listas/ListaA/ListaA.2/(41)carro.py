# Entrada
custo_fab = float(input('Qual o custo de fábrica? '))

# Processamento
custo_novo = (custo_fab * 1.28) + (custo_fab * 0.45)

# Saída
print(f'O custo desse carro como preco de fábrica de R${custo_fab:.2f} é de R${custo_novo:.2f}')
