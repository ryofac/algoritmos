def main():
    horas = int(input('Quantas horas duraram o jogo? \n> '))
    minutos = int(input('Quantos minutos duraram o jogo? \n> '))
    
    hora_atual = int(input('Qual a hora atual? '))
    minutos_atuais = int(input('Qual o minuto atual? '))
    
    horas_totais = horas + hora_atual
    minutos_totais = minutos + minutos_atuais
    
    if minutos_totais % 60 > 0:
        minutos_totais = minutos_totais - 60  * (minutos_totais // 60)
        horas_totais += 1
    if horas % 24 > 0:
        horas_totais = horas_totais - 24 * (horas_totais // 24)
        
    print(f'Final do jogo: {horas_totais}h e  {minutos_totais}min')
    
main()