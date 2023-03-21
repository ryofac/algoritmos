# Entrada: 
num = str(input('Digite o número a ser decomposto: '))
acumular = 0

#Processamento:
print('Componentes:')
for c in num:
    c = int(c)
    acumular += c
    print(c, end =' ')

# Saída:
print(f'\nA soma dos componentes do número é {acumular}')