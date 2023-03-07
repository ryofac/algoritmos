# Leia um número inteiro de minutos, calcule e escreva quantos dias, quantas horas e quantos minutos ele corresponde.

# Entrada:
min = int(input('Me dê um número inteiro de minutos\n >> '))

# Processamento
horas = min // 60
min_final = min % 60
dias = horas // 24
horas_final = horas % 24

# Saída
print(f'Isso equivale a {dias} dias, {horas_final} horas e {min_final} minutos')
