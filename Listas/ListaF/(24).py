from math import sqrt
def main():
    
    a, b, c = [int(x) for x in input('Digite os coeficientes da equação: ').split()]
    print(a, b ,c)
    
    if a == 0:
        print('A não pode ser igual a 0!')
        return
    
    if calcular_raizes(a,b,c):
        raiz1, raiz2 = calcular_raizes(a, b, c)
    else:
        print('Raiz de delta deu negativo doido!')
        return
    
    print(f'Os coeficientes dessa equação são: {raiz1:.1f}, {raiz2:.1f}')
    
def calcular_raizes(a, b, c):
    delta = b ** 2 - (4 * a *c)
    if delta < 0:
        return 
    
    x1 = (b + sqrt(delta)) / 2 * a
    x2 = (b - sqrt(delta)) / 2 * a
    
    return x1, x2
    
main()