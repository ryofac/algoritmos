def main():
    # Entrada:
    valor = int(input('Digite um valor desejado: '))

    # Processamento: 
    nota_50, nota_10, nota_5, resto_5 = conversao(valor) # Usando o desenpacotamento

    # Saída:
    print(f'Notas de 50: {nota_50}\nNotas de 10: {nota_10}\nNotas de 5: {nota_5}\nNotas de 1: {resto_5}')

    # Utilizei dessa forma porque o valor vai se modificando ao longo das divisões, fica mais condensado, sem muitas variáveis
def conversao(valor):
    nota50 = valor // 50
    valor = valor % 50
    nota10 = valor // 10
    valor = valor % 10
    nota5 = valor // 5
    valor = valor % 5
    return nota50, nota10, nota5, valor
main()
