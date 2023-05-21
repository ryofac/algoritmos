from str_utils import * 

def main():
    
    # Entrada
    tempo = str(input('Digite o tempo no formato HH:MM:SS: '))
    
    # Processamento
    seg, min, hora = separar_tempo(tempo)
    
    # Fail Fast
    while not eh_tempo_valido(seg, min, hora) and obter_tamanho(tempo) != 8:
        print('Tempo inválido!')
        tempo = str(input('Digite o tempo no formato HH:MM:SS: '))
        seg, min, hora = separar_tempo(tempo)
        
        
    # Saída
    print(f'{hora} horas {min} minutos e {seg} segundos')
    
    
def separar_tempo(time:str):
    seg = int(substring_tamanho(time, 6, obter_tamanho(time)))
    min = int(substring_tamanho(time, 3, 5))
    hora = int(substring_tamanho(time, 0, 2))
    return seg, min, hora


def eh_tempo_valido(seg, min, hora):
    return 0 < seg <= 60 and 0 < min <=12 and 100 <= hora <= 3000 and eh_numero(seg) and eh_numero(min) and eh_numero(hora)


def eh_numero(num):
    return num * 0 == 0
    
main()
