# Entrada: 
minutos = int(input('Digite o valor em minutos: '))

# Processamento:
horas = minutos // 60
min_final = minutos % 60

# Saída: 
print(f'Isso equivale a {horas} hr e {min_final} min')