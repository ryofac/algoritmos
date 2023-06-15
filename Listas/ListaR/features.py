from utils.vetor_utils import *
from utils.str_utils import eh_numero
import utils.io_utils as io


def gerar_n_posicoes(posicoes, valor_padrao = None):
    out = [None] * posicoes
    out = mapear(out, lambda x: valor_padrao, lambda x: x == None)
    out = mapear(out, lambda x: float(x), eh_numero)
    return out


def substituir_valores_um_a_um(vetor):
    if obter_tamanho_vetor == 0:
        print('Vetor sem itens!')
        return
    for i in range(len(vetor)):
        item_substituido = input(f'O que você quer colocar na posição {i+1}? \n> ')
        if eh_numero(item_substituido):
            item_substituido = float(item_substituido)
        vetor[i] = item_substituido
        
        
def preencher_automaticamente_vetor(maximo, minimo):
    out = []
    while minimo <= maximo:
        adcionar_elemento(out, minimo)
        minimo += 1
    return out

def elevar_a_potencia_N(vetor):
    if obter_tamanho_vetor(vetor) == 0:
        print('Vetor não tem elementos, preencha o vetor antes!')
        return
    expoente = io.obter_numero('N: ')
    vetor = mapear(vetor, lambda x: float(x), eh_numero)
    return mapear(vetor, lambda x : x ** expoente, eh_numero)


def contar_positivos_negativos_zeros(vetor):
    opcoes = '\nObter...'
    opcoes = '\n1 - Quantidade de ZEROS'
    opcoes += '\n2 - Quantidade de POSITIVOS'
    opcoes += '\n3- Quantidade de NEGATIVOS\n > '
    
    escolha = io.obter_numero_intervalo(opcoes, 3, 1)
    
    if escolha == 1:
        zeros = reduzir(vetor, lambda x, y : x + y, 1, 0, lambda x: x == 0)
        print(f'ZEROS: {zeros}')
    elif escolha == 2:
        positivos = reduzir(vetor, lambda x, y: x + y, 1, 0, lambda x: x > 0)
        print(f'POSITIVOS: {positivos}')
    elif escolha == 3:
        negativos = reduzir(vetor, lambda x, y: x + y, 1, 0, lambda x: x < 0)
        print(f'NEGATIVOS: {negativos}')
    
    

## utils

def mostrar_vetor(vetor, quantidade_max_valores = 6):
    if obter_tamanho_vetor(vetor) == 0:
        print('Vetor sem itens ainda!')
    elif len(vetor) > quantidade_max_valores:
        print(f'VETOR: {vetor[0 : quantidade_max_valores - 1]}\b...({len(vetor) - quantidade_max_valores} itens)...{vetor[len(vetor) - 1]}]')
    else:
        print(vetor)
        
        
def tchauzinho(arquivo_incrivel_motivacional_supermassa):
    mensagens = arquivo_incrivel_motivacional_supermassa.readlines()
    print('\n' + escolher_item_aleatorio(mensagens))

    