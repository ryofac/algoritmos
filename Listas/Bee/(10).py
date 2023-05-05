def main():
    # entrada
    nome = str(input())
    salario = float(input())
    vendas = float(input())
    # processamento
    bonus = calcular_bonus(vendas)
    salario_final = salario + bonus
    # print(f'Olá, {nome}, seu salário foi:')
    # Saida
    print(f'TOTAL = R$ {salario_final:.2f}')
def porcentagem_de(numero):
    return numero / 100
def calcular_bonus(vendas):
    return vendas * porcentagem_de(15)
main()
    
    