def main(): 
    # Leia um número inteiro de segundos, calcule e escreva quantas horas, quantos minutos e quantos segundos ele corresponde.

    # Entrada:
    seg = int(input('Digite um número inteiro de segundos \n >> '))

    # Processamento
    min, seg_f = minutos(seg) # Desenpacotamento da tupla com minutos e segundos finais
    h, min_f = horas(min)
    
    
    # Saída
    print(f'O valor informado equivale a {h}h {min_f}min {seg_f}s')

def minutos(segundos):
    min = segundos // 60
    seg_f = segundos % 60
    return min, seg_f # Retorna os minutos e o resto da divisão, os segundos finais

def horas(minutos):
    h = minutos // 60
    minf = minutos % 60
    return h, minf 

main()
