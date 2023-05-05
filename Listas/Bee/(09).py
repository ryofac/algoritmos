def main():
    # Entrada
    numero = int(input())
    horas_trabalho = int(input())
    quantidade_por_hora = float(input())
    # Processsamento
    salario = calcular_salario(horas_trabalho, quantidade_por_hora)
    # Saida
    print(f'NUMBER = {numero}')
    print(f'SALARY = U$ {salario:.2f}')
def calcular_salario(preco_hora, quantidade_hora):
    return preco_hora * quantidade_hora
main()