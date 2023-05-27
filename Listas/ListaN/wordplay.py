from Utils.io_utils import enter_to_continue, obter_numero_positivo, clear_screen
from features import *

def main():
    file = open("/home/ryan/Algoritmos/Listas/ListaN/data/word_data.txt")
    word_list = file.readlines()
    word_list = retirar_espacos(word_list)
    opcao = pedir_opcao()
    
    while opcao != 0:
        if opcao == 1:
            clear_screen()
            imprimir_palavras_maiores_20_caracteres(word_list)
        elif opcao == 2:
            clear_screen()
            imprimir_palavras_com_e(word_list)
            
        enter_to_continue()
        opcao = pedir_opcao()
            
    
def menu():
    opcoes = '*** ESCOLHA SUA OPCAO ***'
    opcoes += '\n1- Mostrar palavras que tem mais de 20 caracteres'
    opcoes += '\n> '
    return opcoes

def pedir_opcao():
    # Resolver a indireção do limite
    return obter_numero_positivo(menu(), tem_limite=True, limite= 10)
main()

