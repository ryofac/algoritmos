def main():
    ficha = int(input('Digite o numero de fichas: '))
    cont = 0
    
    while cont <= ficha:
        codigo = int(input('Digite o código: '))
        horas_trabalhadas = int(input('Digite o número de horas trabalhadas: '))
        numero_dependentes = int(input('Digite o número de depententes: '))

        pagamento_hora = horas_trabalhadas * 12
        pagamento_dependente = numero_dependentes * 40
        salario = pagamento_hora + pagamento_dependente
    
        imposto_renda = verificar_ir(salario)
        inss = verificar_inss(salario)

        print()
        print(f'Salario: {salario}')
        print(f'Desconto do IR: {imposto_renda}')
        print(f'Desconto do INSS: {inss}')
        cont += 1

def verificar_ir(salario):
    return salario * (8.5 / 100)

def verificar_inss(salario):
    return salario * (5 / 100)


main()