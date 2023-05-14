def main():
    try:
        while True:
            r1, x1, y1, r2, x2, y2 = list(map(int, input().split()))
            
            distancia = calcular_distancia(x1,x2,y1,y2)
            
            
            if distancia <= r1 - r2:
                if distancia < 0:
                    print('MORTO')
                print('RICO')
            else:
                print('MORTO')
        
    except EOFError:
        exit()

def calcular_distancia(x1, x2, y1, y2):
    return ((x2 - x1)** 2 + (y2-y1) ** 2) ** 0.5  
  
    
main()