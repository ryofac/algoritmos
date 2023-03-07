# Leia um número inteiro de meses, calcule e escreva quantos anos e quantos meses ele corresponde.

# Entrada:
meses = int(input('Digite um número de meses inteiro\n >> '))

# Processamento
anos = meses // 12
meses_final = meses % 12

# Saída
print(f'Isso equivale a {anos} anos e {meses_final} meses ')