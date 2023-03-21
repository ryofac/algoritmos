# Leia um valor de 4 números em binário e retorne decimal:

# Entrada: 
numero = int(input('Digite o valor em binário (Com 4 dígitos): \n>> '))

# Processamento:
pos4 = (numero // 1000) * 2 ** 3
resto_pos4 = (numero % 1000) 
pos3 = (resto_pos4 // 100) * 2 ** 2
resto_pos3 = (resto_pos4 % 100)
pos2 = (resto_pos3 // 10) * 2
pos1 = (resto_pos3 % 10)

# Saída:
print(f'O número em decimal é {pos4 + pos3 + pos2 + pos1}')
