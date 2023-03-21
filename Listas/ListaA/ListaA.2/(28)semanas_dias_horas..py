#Entrada
hora = int(input('Qual o número de horas \n >> '))

# Processamento
dias = hora // 24
hora_final = hora % 24
semanas = dias // 7
dias_final = dias % 7


# Saída: 
print(f'Isso equivale a {semanas} semanas, {dias_final} dias e {hora_final} horas')