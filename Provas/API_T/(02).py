def main():
    entrada = int(input())
    cont_teste = 0
    while entrada > -1:
        print('Teste ' , cont_teste)
        cont_teste += 1
        print(calcular_dobradura(entrada))
    

def calcular_dobradura(vezes):
        
main()