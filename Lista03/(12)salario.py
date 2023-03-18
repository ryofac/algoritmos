def main():
    # Entrada
    salario = float(input('Digite aqui o seu salário para calcular seu aumento:\n >> R$'))

    # Processamento
    aumento = calcular_aumento(salario)

    # Saída
    print(f'Seu aumento foi de R$ {(calcular_porcentagem(salario, 25)):.2f} e seu novo salário é de R$ {aumento}')

def calcular_porcentagem(num, porcento): # Calcula a porcentagem
    return num * porcento / 100

def calcular_aumento(sal): # Retorna o aumento do salário
    return sal + calcular_porcentagem(sal, 25) 
     
main()