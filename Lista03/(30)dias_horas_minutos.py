def main():
    # Leia um número inteiro de minutos, calcule e escreva quantos dias, quantas horas e quantos minutos ele corresponde.

    # Entrada:
    min = int(input('Me dê um número inteiro de minutos\n >> '))

    # Processamento
    h, min_final = horas(min)
    dia, horas_final = dias(h)
    
    
    # Saída
    print(f'Isso equivale a {dia} dias, {horas_final} horas e {min_final} minutos')


# Recebe o número de minutos e retorna as horas e min finais
def horas(minutos):
    h = minutos // 60
    minf = minutos % 60
    return h, minf

# Recebe o número de horas e retorna os dias e as horas finais
def dias(horas):
    d = horas // 24
    hf = horas % 24
    return d, hf

main()
