# Leia um número inteiro de dias, calcule e escreva quantas semanas e quantos dias ele corresponde.

# Entrada:
dia = int(input('Qual o número de dias? \n >> '))

# Processamento:
semana = dia // 7
dia_final = dia % 7

# Saída: 
print(f'Isso equivale a {semana} Semanas e {dia_final} dias')

