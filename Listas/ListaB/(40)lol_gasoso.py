# Entrada
tempoA = int(input('A quantos anos você fuma? '))
quant = int(input('Quantos cigarros você fuma por dia? '))
preco = int(input('Qual o preço da cartela? '))

# Processamento
preco_cigarro = preco / 20
tempoD = tempoA * (12 * 30)
gasto = preco_cigarro * tempoD

# Saída
print(preco_cigarro)
print(f'Você já gastou R${gasto} em cigarros')