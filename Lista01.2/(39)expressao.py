# Entrada
A = int(input('Digite o número a: '))
B = int(input('Digite o número b: '))
C = int(input('Digite o número c: '))

# Processamento
R = (A + B) ** 2
S = (B + C) ** 2

# Saída
D = (R + S) / 2
print(f'R = ({A} + {B})²\nS = ({B} + {C})²')
print(f'D = ({R} + {S}) / 2')
print(f'O valor da expressão D dada, com esses valores é de: {D}')