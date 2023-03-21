# Entrada
valor = float(input('Digite o valor da mercadoria: \n>> R$'))

# Processamento
prestacao = valor // 3
restante = valor % 3
entrada = restante + prestacao

# Saída
print(f'Vâo ser duas parcelas de R${prestacao:.2f} e uma entrada de R${entrada:.2f}')