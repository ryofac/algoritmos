from utils.io_utils import *
from features import *

arquivo_bye = open('./data/bye.txt')

def main():
    vetor = []
    vetores = vetor
        
    while True:
        clear_screen()
        mostrar_vetor(vetores)
        opcao = obter_numero_intervalo(menu(), 20, 0)
            
        if opcao == 0:
            tchauzinho(arquivo_bye)
            break
        
        if opcao == 1:
            posicoes = obter_inteiro('Quantas posições? \n> ', tipo= "+")
            valor_padrao = input('Qual o valor padrão? \n> ')
            vetores = gerar_n_posicoes(posicoes, valor_padrao)
            mostrar_vetor(vetores, 10)
            
        elif opcao == 2:
            substituir_valores_um_a_um(vetores)
            
        elif opcao == 3:
            minimo = obter_inteiro('Digite o valor mínimo: ')
            maximo = obter_inteiro('Digite o valor máximo: ')
            vetores = preencher_automaticamente_vetor(maximo, minimo)
            mostrar_vetor(vetores, 10)
            
        elif opcao == 4:
            quantidade = obter_inteiro('Digite a quantidade máxima de elementos a ser exibida: ')
            mostrar_vetor(vetores, quantidade)
        
        elif opcao == 5:
            vetores = elevar_a_potencia_N(vetores)
        
        elif opcao == 6:
            contar_positivos_negativos_zeros(vetores)
        
        elif opcao == 7:
            exibir_somatorio_todos_negativos_positivos(vetores)
        
        elif opcao == 8:
           vetores = remover_texto(vetores)
            
        elif opcao == 9:
            exibir_maior_menor_numero_vetor(vetores)
        
        elif opcao == 10:
            sortear_positivo_e_negativo(vetores)
            
        elif opcao == 11:
            vetores = adcionar_grupos_n_grupos_t_tamanho(vetores)
            mostrar_vetor(vetores)
        
        enter_to_continue()
    
    
    
def menu():
    opcoes =  '\n ---------------  O P Ç Õ E S  ---------------'
    opcoes += '\n 1 - Gerar Vetor com X posições e valor Y padrão'
    opcoes += '\n 2 - Substituir Itens do vetor um a um'
    opcoes += '\n 3 - Gerar vetor automaticamente com intervalo'
    opcoes += '\n 4 - Mostrar itens do vetor'
    opcoes += '\n 5 - Elevar a potência N'
    opcoes += '\n 6 - Número de POSITIVOS, NEGATIVOS e ZEROS'
    opcoes += '\n 7 - Somatório do TOTAL, POSITIVOS E NEGATIVOS'
    opcoes += '\n 8 - Remover não números'
    opcoes += '\n 9 - Obter maior e menor número vetor'
    opcoes += '\n 10 - Obter POSITIVO e NEGATIVO aleatório'
    opcoes += '\n 11 - Adcionar N grupos, tamanho T (Vetor de Vetores)'


    opcoes += '\n 0 - Sair'
    opcoes += '\n> '
    
    return opcoes

if __name__ == '__main__':
    main()