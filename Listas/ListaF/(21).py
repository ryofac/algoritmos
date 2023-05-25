def main():
    
    numero = float(input('Digite um número quebrado: '))
    
    if numero - int(numero) >= 0.5:
        numero = int(numero) + 1
        
    else:
        numero = int(numero)
        
    print(numero)
    
        
    
main()