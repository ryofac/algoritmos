# Leia um número inteiro de segundos, calcule e escreva quantas horas, quantos minutos e quantos segundos ele corresponde.

# Entrada:
seg = int(input('Digite um número inteiro de segundos \n >> '))

# Processamento:
min = seg // 60
seg_final = seg % 60
hora = min // 60
min_final = min % 60

# Saída
print(f'O valor informado equeivale a {hora}h {min_final}min {seg_final}s')
