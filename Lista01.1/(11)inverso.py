# Entrada
num = int(input('Digite um número de 3 algarismos: '))

# Processamento
centena = num // 100
resto_centena = num % 100
dezena = resto_centena // 10
unidade = resto_centena % 10

# Saída
print(unidade,dezena,centena)

# Em próximos exercícios parecidos, eu utilizei outro método, o fatiamento de string