def main():
    # Entrada: 
    minutos = int(input('Digite o valor em minutos: '))

    # Processamento:
    min_final = restoMin(minutos)
    min_inteiros = minutos = min_final
    horas = converterHora(min_inteiros)
    
    # Saída: 
    print(f'Isso equivale a {horas} hr e {min_final} min')
    
def restoMin(min): # Calcula o resto da divisão em minuto
    min_f = min % 60
    return min_f

def converterHora(min): # Converte minutos inteiros em horas
    hora = min / 60
    return hora

main()