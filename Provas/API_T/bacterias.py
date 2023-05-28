# -*- coding: utf-8 -*-
def main():
    quantidade = int(input())
    maior_base = -1
    menor_expoente = float('inf')
    for i in range(quantidade):
        bacteria = [int(x) for x in input().split()]
         
        if bacteria[0] < menor_expoente:
            menor_expoente = bacteria[0]
        
        if bacteria[1] ** bacteria[0] > maior_base or maior_base == -1:
            maior_base = bacteria[1]
            
        potencia_maior = maior_base ** menor_expoente
        
        

    
main()