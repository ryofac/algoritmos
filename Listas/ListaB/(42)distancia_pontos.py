from math import sqrt
# Entrada:
x1 = float(input('x1: '))
x2 = float(input('x2: '))
y1 = float(input('y1: '))
y2 = float(input('y2: '))

# Processamento:
dist = sqrt((x2-x1)**2 + (y2-y1)**2)

# Saída:
print(f'A distância entre os pontos dados é de : {dist} unidades')
