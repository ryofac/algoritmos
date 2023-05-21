def main():
    try:
        quantas_vezes_rodar = int(input())
        for c in range(quantas_vezes_rodar):
            numero_desejado = input()
            
            qnt_leds = calcular_qnt_leds(numero_desejado)
            
            print(qnt_leds, 'leds')
    except EOFError:
        return 

def calcular_qnt_leds(numero_desejado):
    
    resultado_final = 0
    qnt_leds = (6,2,5,5,4,5,6,3,7,6)
    for i in numero_desejado:
        i = int(i)
        resultado_final += qnt_leds[i]
    return resultado_final

main()