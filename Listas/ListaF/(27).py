def main():
    dia = int(input('Digite o dia que você nasceu \n >> '))
    mes = int(input('Digite o mês que você nasceu \n >> '))
    ano = int(input('Digite o ano que você nasceu \n >> '))

    if not is_valid(dia, mes, ano):  # fail fast
        print('Dados Inválidos !!')
        return

    ano_atual = 2023
    mes_atual = 4
    dia_atual = 24

    idade = ano_atual - ano

    if mes > mes_atual or (mes == mes_atual and dia < dia_atual):
        idade = idade - 1
    elif dia == dia_atual:
        print('Feliz aniversário!!!')

    print(f'DATA ATUAL: {formatar(dia_atual, mes_atual, ano_atual)}')
    print(f'Você tem {idade} anos de idade! Pois você nasceu na data {formatar(dia, mes, ano)}')


def is_valid(d, m, a):
    if not (d > 0 and m > 0 and a > 0):  # Fail Fast
        return False
    if m == 2:
        return d <= 28 and m <= 12 and a < 2023
    return d <= 31 and m <= 12 and a < 2023


def formatar(d, m, a):
    return f'{d}/{m}/{a}'


main()