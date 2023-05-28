from Utils.io_utils import *
from features import *
import sys
sys.path.append("/data/despedidas.txt")
sys.path.append("/data/word_data.txt")

def main():
    file = open("/home/ryan/Algoritmos/Listas/ListaN/data/word_data.txt")
    despedidas_file = open("/home/ryan/Algoritmos/Listas/ListaN/data/despedidas.txt")
    
    word_list = file.readlines()
    word_list = retirar_espacos(word_list)
    opcao = pedir_opcao()
    
    while opcao != 0:
        if opcao == 1:
            clear_screen()
            imprimir_todas(word_list)
            
            
        elif opcao == 2:
            clear_screen()
            N = obter_numero_positivo('N: ')
            imprimir_palavras_maiores_que_N(word_list, N)
            
        
        elif opcao == 3:
            clear_screen()
            letra = obter_texto_max('Letra: ', 1)
            imprimir_sem_char(word_list, letra)
            
        
        elif opcao == 4:
            clear_screen()
            letras_proibidas = [i for i in obter_texto('Digite as letras proibidas: ').split()]
            imprimir_sem_letras_proibidas(word_list, letras_proibidas)
            
        
        elif opcao == 5:
            clear_screen()
            Letras_somente = [i for i in obter_texto('Digite as letras: ').split()]
            imprimir_somente_contem_letras(word_list, Letras_somente)
            
            
        elif opcao == 6:
            clear_screen()
            letras_obrigatorias = [i for i in obter_texto('Digite as letras obrigatórias: ').split()]
            imprimir_contem_letras(word_list, letras_obrigatorias)
        
        
        elif opcao == 7:
            clear_screen()
            N = obter_numero_positivo('N: ')
            imprimir_letras_max(word_list, N)
        
        
        elif opcao == 8:
            clear_screen()
            imprimir_palavras_palindromas(word_list)
        
            
        enter_to_continue()
        opcao = pedir_opcao()
        
    elif opcao == 9:
        
    print('Programa encerrado... Tchau coração! <3\n')
    encerrar_programa(despedidas_file)
    
   
            
    
def menu():
    opcoes = '        =======  Escolha opção: ========'
    opcoes += '\n1- Mostrar todas as palavras'
    opcoes += '\n2 - Mostrar as palavras com mais de N caracteres'
    opcoes += '\n3 - Mostrar palavras que não contém um letra dada'
    opcoes += '\n4 - Mostrar palavras sem letras proibidas recebidas'
    opcoes += '\n5 - Mostrar palavras que SÓ CONTENHAM letras dadas'
    opcoes += '\n6 - Mostrar palavras que CONTENHAM as letras dadas'
    opcoes += '\n7 - Mostrar palavras com no máximo N caracteres'
    opcoes += '\n8 - Mostrar palavras palíndromas'
    opcoes += '\n0 - Sair do programa'
    opcoes += '\n >> '
    return opcoes


def pedir_opcao():
    # Resolver a indireção do limite
    return obter_numero_positivo(menu(), tem_limite=True, limite= 10)
main()

