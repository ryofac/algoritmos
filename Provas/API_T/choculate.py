def main():
    pedaco_inicial = int(input())
    
    fatias = [int(x) for x in input().split()]
    
    resto = calcular_resto(fatias)
    
    print(resto)

def calcular_resto(fatias):
    total = 0
    for fatia in fatias:
        total += fatia -1
    return total
main()