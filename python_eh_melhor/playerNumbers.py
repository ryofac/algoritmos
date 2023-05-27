from features import multiplicar_cada_numero_por_n, localizar_posicoes, gerar_vetor, enter_limpar_tela
from utils import bye

# Implementar opcoes 6


def main():
    enter_limpar_tela()
    opcoes = menu() 
    numeros = []

    opcao = int(input(opcoes))

    while opcao != 0: 
        if opcao == 1:
            numeros = gerar_vetor()
        elif opcao == 2:
            print(f"Existem {len(numeros)} itens.")
        elif opcao == 3:
            print(numeros)
        elif opcao == 4:
            localizar_posicoes(numeros)
        elif opcao == 5:
            print("Vetores Anteriores: ")
            print(numeros)
            numeros = multiplicar_cada_numero_por_n(numeros)
            print("Vetores atuais: ")
            print(numeros)
            
        enter_limpar_tela()
        opcao = int(input(opcoes))

    bye()

def menu():
    opcoes = "======= PLAY NUMBERS ======"
    opcoes += "\n1 - Gerar Números"
    opcoes += "\n2 - Mostrar quantidade de números gerados"
    opcoes +="\n3 - Mostrar números"
    opcoes +="\n4 - Buscar número"
    opcoes += "\n5 - Multiplicar números por N"
    
    opcoes += "\n6 - Somar números por N"
    opcoes += "\n0 - Sair"
    opcoes += "\n\n<enter option...> "

    return opcoes

main()
