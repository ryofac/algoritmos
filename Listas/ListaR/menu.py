from utils.io_utils import *
from features import *

arquivo_bye = open('./data/bye.txt')

def main():
    vetor = []
        
    while True:
        clear_screen()
        mostrar_vetor(vetor)
        opcao = obter_numero_intervalo(menu(), 20, 0)
            
        if opcao == 0:
            tchauzinho(arquivo_bye)
            break
        
        if opcao == 1:
            posicoes = obter_inteiro('Quantas posições? \n> ', tipo= "+")
            valor_padrao = input('Qual o valor padrão? \n> ')
            vetor = gerar_n_posicoes(posicoes, valor_padrao)
            mostrar_vetor(vetor, 10)
            
        elif opcao == 2:
            substituir_valores_um_a_um(vetor)
            
        elif opcao == 3:
            minimo = obter_inteiro('Digite o valor mínimo: ')
            maximo = obter_inteiro('Digite o valor máximo: ')
            vetor = preencher_automaticamente_vetor(maximo, minimo)
            mostrar_vetor(vetor, 10)
            
        elif opcao == 4:
            quantidade = obter_inteiro('Digite a quantidade máxima de elementos a ser exibida: ')
            mostrar_vetor(vetor, quantidade)
        
        elif opcao == 5:
            vetor = elevar_a_potencia_N(vetor)
        
        elif opcao == 6:
            contar_positivos_negativos_zeros(vetor)
        
        elif opcao == 7:
            print('tente outra funcionalidade, por enquanto')
            pass
        
        enter_to_continue()
    
    
    
def menu():
    opcoes =  '\n ---------------  O P Ç Õ E S  ---------------'
    opcoes += '\n 1 - Gerar Vetor com X posições e valor Y padrão'
    opcoes += '\n 2 - Substituir Itens do vetor um a um'
    opcoes += '\n 3 - Gerar vetor automaticamente com intervalo'
    opcoes += '\n 4 - Mostrar itens do vetor'
    opcoes += '\n 5 - Elevar a potência N'
    opcoes += '\n 6 - Número de POSITIVOS, NEGATIVOS e ZEROS'
    opcoes += '\n 7 - Work in Progress'


    opcoes += '\n 0 - Sair'
    opcoes += '\n> '
    
    return opcoes

if __name__ == '__main__':
    main()