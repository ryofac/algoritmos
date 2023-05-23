def main():
    c = 0
    contador_impar = 0
    somador = 0
    
    for c in range(1, 100):
        if c % 2:
            contador_impar += 1
            somador += c / contador_impar
            print('{} / {} + '.format(c, contador_impar))
        c += 1
        
    print('--------\n', somador)
main() 