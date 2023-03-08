# Entrada
num = int(input('Digite um número de 3 algarismos: '))

# Processamento
centena = num // 100
resto_centena = num % 100
dezena = resto_centena // 10
unidade = resto_centena % 10

# Saída
print(f'O número é divido dessa forma: {centena} centenas {dezena} dezenas e {unidade} unidades')