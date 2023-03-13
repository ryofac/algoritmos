# Entrada:
valor = int(input('Digite um valor desejado: '))

# Processamento: 
nota50 = valor // 50
resto_50 = valor % 50
nota_10 = resto_50 // 10
resto_10 = resto_50 % 10
nota_5 = resto_10 // 5
resto_5 = resto_10 % 5

# Saída:
print(f'Notas de 50: {nota50}\nNotas de 10: {nota_10}\nNotas de 5: {nota_5}\nNotas de 1: {resto_5}')