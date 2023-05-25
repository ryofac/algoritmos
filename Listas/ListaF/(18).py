def main():
    opcao = int(input(menu()))
    
    valor_a = int(input('Digite o valor a: '))
    valor_b = int(input('Digite o valor b: '))
    
    if opcao == 1:
        print(valor_a + valor_b)
    if opcao == 2:
        print(valor_a - valor_b)
    if opcao == 3:
        print(valor_a * valor_b)
    if opcao == 4:
        print(valor_a/valor_b)
        
def menu():
    opcoes = '|||MENU DE OPÇÕES|||'
    opcoes += '\n1 - Somar valores'
    opcoes += '\n2 - Subtrair valores'
    opcoes += '\n3 - Multiplicar valores'
    opcoes += '\n3 - Dividir valores'
    opcoes += '\n> '
    return opcoes

main()