from str_utils import * 

def main():
    # Entrada
    data = str(input('Digite a data no formato DD/MM/AAAA: '))
    
    # Processamento
    dia, mes, ano = separar_data(data)
    
    # Fail Fast
    while not eh_data_valida(dia, mes, ano) and obter_tamanho(data) != 10:
        print('Data inválida! ')
        data = str(input('Digite a data no formato DD/MM/AAAA: '))
        dia, mes, ano = separar_data(data)
        
    mes_verboso = mes_extenso(mes)
        
    # Saída
    print(f'{dia} de {mes_verboso} de {ano}')
    
    
def separar_data(date:str):
    dia = int(substring_tamanho(date, 0, 2))
    mes = int(substring_tamanho(date, 3, 5))
    ano = int(substring_tamanho(date, 6, obter_tamanho(date)))
    return dia, mes, ano


def eh_data_valida(dia, mes, ano):
    return 0 < dia <= 30 and 0 < mes <=12 and 100 <= ano <= 3000 and eh_numero(dia) and eh_numero(mes) and eh_numero(ano)


def eh_numero(num):
    return num * 0 == 0
    
    
def mes_extenso(num_mes):
    meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
    return meses[num_mes-1]


main()
