def main():
    num1 = int(input('Digite o primeiro valor: '))
    num2 = int(input('Digite o segundo valor'))
    while num1 == 0 or num2 == 0:
        print('Valores inválidos')
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor'))
    maior = valor_maximo_de(num1, num2)
    valor_minimo = num1 + num2 - maior
    cont = valor_minimo
    while True:
        if eh_multiplo(num1, cont) and eh_multiplo(num2, cont):
            return cont
        cont += 1


def valor_maximo_de(*valores: int):
    valor_grandao = float('-inf')
    for values in valores:
        if values > valor_grandao:
            valor_grandao = values
    return valor_grandao

def eh_multiplo(numero, candidato):
    return candidato % numero == 0


main()