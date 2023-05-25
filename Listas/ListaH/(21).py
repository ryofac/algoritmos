def main():
    contador = 0
    contador_impar = 0
    somador = 0
    
    while contador <= 99:
        if contador % 2:
            contador_impar += 1
            somador += contador / contador_impar
            print('{} / {} + '.format(contador, contador_impar))
        contador += 1
        
    print('--------\n',somador)
main() 