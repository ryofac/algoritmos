from Utils.io_utils import *
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
            letra = obter_texto_max('Letra: ', 1)
            imprimir_sem_char(word_list, letra)
        
        elif opcao == 3:
            clear_screen()
            letras_proibidas = [i for i in obter_texto('Digite as letras proibidas: ').split()]
            imprimir_sem_letras_proibidas(word_list, letras_proibidas)
        
        # Função com IN (tentar fazer sem)
        elif opcao == 4:
            clear_screen()
            letras_obrigatorias = [i for i in obter_texto('Digite as letras obrigatórias: ').split()]
            imprimir_somente_letras_obrigatorias(word_list, letras_obrigatorias)
            
        
            
        enter_to_continue()
        opcao = pedir_opcao()
            
    
def menu():
    opcoes = '        =======  Escolha opção: ========'
    opcoes += '\n1- Mostrar palavras que tem mais de 20 caracteres'
    opcoes += '\n2 - Mostrar palavras que não contém um letra dada'
    opcoes += '\n3 - Mostrar palavras sem letras proibidas recebidas'
    opcoes += '\n4 - Mostrar palavras que só contenham letras dadas'
    opcoes += '\n >> '
    return opcoes

def pedir_opcao():
    # Resolver a indireção do limite
    return obter_numero_positivo(menu(), tem_limite=True, limite= 10)
main()

