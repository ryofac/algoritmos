from utils.vetor_utils import *
from utils.str_utils import eh_numero
import utils.io_utils as io
import time


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
    menu = gerar_menu('Quantidade de ZEROS', 
                      'Quantidade de POSITIVOS', 
                      'Quantidade de NEGATIVOS', titulo= 'Obter..')
    
    escolha = io.obter_numero_intervalo(menu, 3, 1)
    todos = obter_tamanho_vetor(vetor)
    
    if escolha == 1:
        zeros = reduzir(vetor, lambda x, y : x + 1, atual= 0, regra=lambda x: x == 0)
        print(f'ZEROS: {zeros}')
        print(io.barra_porcentagem(zeros, todos))
        print('... do valor total')
    
        
    elif escolha == 2:
        positivos = reduzir(vetor, lambda x, y: x + 1, atual= 0, regra= lambda x: x > 0 and eh_numero(x))
        print(f'POSITIVOS: {positivos}')
        print(io.barra_porcentagem(positivos, todos))
        print('... do valor total')
    elif escolha == 3:
        negativos = reduzir(vetor, lambda x, y : x + 1, atual = 0, regra= lambda x: x < 0 and eh_numero(x))
        print(f'NEGATIVOS: {negativos}')
        print(io.barra_porcentagem(negativos, todos))
        print('... do valor total')
        
    
def exibir_somatorio_todos_negativos_positivos(vetor):
    if obter_tamanho_vetor(vetor) == 0:
        print('Vetor sem elementos!')
        return
    todos = reduzir(vetor, lambda x, y: x + y, regra=eh_numero)
    menu = gerar_menu('Somatório de TODOS', 
                    'Somatório de POSITIVOS', 
                    'Somatório de NEGATIVOS', titulo= 'Obter..')
    
    escolha = io.obter_numero_intervalo(menu, 3, 1)
    
    if escolha == 1:
        print('A soma de todos é ', todos)
    
    elif escolha == 2:
        positivos = reduzir(vetor, lambda x, y: x + y, regra= lambda x: x > 0 if eh_numero(x) else x) 
        print('A soma de todos os positivos é ', positivos)
            
    elif escolha == 3:
        negativos = reduzir(vetor, lambda x, y: x + y, regra= lambda x: x < 0 if eh_numero(x) else x)
        print('A soma de todos os negativos é ', negativos)
        
        
def remover_texto(vetor):
    print('Removendo Não números...')
    cont = 0
    while cont < 100:
        time.sleep(0.001)
        print(io.barra_loading(cont, 100))
        io.clear_screen()
        cont += 1
    print(io.barra_loading(cont, 100))
    out = filtrar(vetor, eh_numero)
    return out


def exibir_maior_menor_numero_vetor(vetor):
    print('O maior número do vetor é: ', maior_numero_vetor(vetor))
    print('O menor número do vetor é ', menor_numero_vetor(vetor))


def sortear_positivo_e_negativo(vetor):
    numeros = filtrar(vetor, eh_numero)
    
    if reduzir(numeros, lambda x, y: x or y > 0, atual= False):
        positivo_random = escolher_item_aleatorio(vetor)
        while positivo_random < 0:
            numero_aleatorio = escolher_item_aleatorio(vetor)
            positivo_random = numero_aleatorio
        print(f'Elemento positivo aleatório: {positivo_random}')
    else:
        print('Sem elementos positivos :(')
        
    if reduzir(numeros, lambda x, y: x or y < 0, atual= False):
        negativo_random = escolher_item_aleatorio(vetor)
        while negativo_random > 0:
            numero_aleatorio = escolher_item_aleatorio(vetor)
            negativo_random = numero_aleatorio
        print(f'Elemento negativo aleatório: {negativo_random}')
    else:
        print('Sem elementos negativos :(')
        
    
def adcionar_grupos_n_grupos_t_tamanho(vetores):
    out = []
    vetor = []
    n = io.obter_inteiro('N: ', tipo="+")
    t = io.obter_inteiro('T: ', tipo="+")
    
    numero_aleatorio = gerar_numero_aleatorio_entre(1, 100)
    
    while obter_tamanho_vetor(out) < n:
        if numero_aleatorio not in vetor:
            adcionar_elemento(vetor, numero_aleatorio)
        else:
            numero_aleatorio = gerar_numero_aleatorio_entre(1,100)
        if obter_tamanho_vetor(vetor) == t:
            adcionar_elemento(out, vetor)
            vetor = []
    return out
        
        
        
        
        
    

## utils


def gerar_menu(*opcoes, titulo = '==== MENU ===='):
    menu = titulo
    for i in range(obter_tamanho_vetor(opcoes)):
        menu += f'\n{i + 1} - {opcoes[i]}'
    menu += '\n> '
    return menu

def gerar_numero_aleatorio_entre(min, max):
    return int(random() * (max - min) + min)
    

def mostrar_vetor(vetor, quantidade_max_valores = 6):
    if eh_matriz(vetor):
        print('VETOR DE VETORES')
        mostrar_matriz(matriz= vetor)
        return
    if obter_tamanho_vetor(vetor) == 0:
        print('Vetor sem itens ainda!')
    elif len(vetor) > quantidade_max_valores:
        print(f'VETOR: {vetor[0 : quantidade_max_valores - 1]}\b...({len(vetor) - quantidade_max_valores} itens)...{vetor[len(vetor) - 1]}]')
    else:
        print(vetor)
        
def mostrar_matriz(matriz):
    for item in matriz:
        print(item)
        
def tchauzinho(arquivo_incrivel_motivacional_supermassa):
    mensagens = arquivo_incrivel_motivacional_supermassa.readlines()
    print('\n' + escolher_item_aleatorio(mensagens))

    