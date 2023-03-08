# Entrada
a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))
d = float(input('d: '))
e = float(input('e: '))
f = float(input('f: '))

# Processamento
x = ((c * e - b * f) / (a * e - b * d))
y = (a * f - c * d) / (a * e - b * d)

# Saída
print(f'O valor de x é: {x}\nO valor de y é {y}')
