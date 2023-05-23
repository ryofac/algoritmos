def main():
    try:
        valores = list(map(int, input().split()))
        for c in range(len(valores)):
            if eh_triangulo(valores[0], valores[1], valores[2]) or \
                eh_triangulo(valores[1], valores[2], valores[3]) or \
                eh_triangulo(valores[0], valores[1], valores[3]) or \
                eh_triangulo(valores[0], valores[2], valores[3]):
                print('S')
                return
        print('N')
                    
    except EOFError:
        return 
    

def eh_triangulo(l1,l2,l3):
    return l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2
        
main()