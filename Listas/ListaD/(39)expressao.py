def main():
    # Entrada
    A = int(input('Digite o número a: '))
    B = int(input('Digite o número b: '))
    C = int(input('Digite o número c: '))

    # Processamento
    R = calcularR(A,B)
    S = calcularS(B,C)
    D = calcularD(R,S)
    
    # Saída
    print(f'R = ({A} + {B})²\nS = ({B} + {C})²')
    print(f'D = ({R} + {S}) / 2')
    print(f'O valor da expressão D dada, com esses valores é de: {D}')

def calcularR(A,B):
    R = (A + B) ** 2 
    return R

def calcularS(B,C):
    S = (B + C) ** 2
    return S
    
def calcularD(R,S):
    D = (R + S) / 2
    return D

main()