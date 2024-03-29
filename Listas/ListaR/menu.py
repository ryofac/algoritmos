from utils.io_utils import *
from features import *

arquivo_bye = open('./data/bye.txt')

def main():
    vetor = []
    vetores = vetor
        
    while True:
        clear_screen()
        mostrar_vetor(vetores, center = True)
        opcao = obter_numero_intervalo(menu(), 20, 0)
            
        if opcao == 0:
            tchauzinho(arquivo_bye)
            break
        
        if opcao == 1:
            vetores = gerar_valores_padrao(vetores)
            
        elif opcao == 2:
            substituir_valores_um_a_um(vetores)
            
        elif opcao == 3:
            vetores = preencher_vetor_intervalo(vetores)
            
        elif opcao == 4:
            quantidade = obter_inteiro('Digite a quantidade máxima de elementos a ser exibida: ')
            mostrar_vetor(vetores, quantidade)
        
        elif opcao == 5:
            vetores = elevar_a_potencia_N(vetores)
        
        elif opcao == 6:
            mostrar_vetor(vetores)
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
            
        elif opcao == 12:
            pedir_novo_vetor_e_verificar_se_esta_no_vetor(vetores)
        
        elif opcao == 13:
            top_n_maiores(vetores)
        
        elif opcao == 14:
            top_n_menores(vetores)
        
        elif opcao == 15:
            analise_media(vetores)
        
        elif opcao == 16:
            print('Easter Egg ;)')
            
        elif opcao == 17:
            mostrar_questao_grande(vetores)
        
        elif opcao == 18:
            ordem_crescente(vetores)
        
        elif opcao == 19:
            ordem_decrescente(vetores)
        
        elif opcao == 20:
            vetores = obter_e_apagar_numero_multiplo_N_M(vetores)
            
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
    opcoes += '\n 12 - Obter vetor e ver se está 100% presente no outro (e na ordem)'
    opcoes += '\n 13 - Pedir N MAIORES'
    opcoes += '\n 14 - Pedir N MENORES'
    opcoes += '\n 15 - VALOR MÉDIO, MENORES QUE A MÉDIA e MAIORES QUE MÉDIA '
    opcoes += '\n 17 - Somatório da Média dos Números Positivos múltiplos dois COM o Produto acumulado dos números negativos pares reduzidos à metade'
    opcoes += '\n 18 - Ordenar os números em ordem crescente...'
    opcoes += '\n 19 - Ordenar os números em ordem decrescente... '
    opcoes += '\n 20 - Obter número múltiplo de N e M, simultaneamente'

    opcoes += '\n 0 - Sair'
    opcoes += '\n> '
    
    return opcoes

if __name__ == '__main__':
    main()