from utils.vetor_utils import *
from utils.str_utils import eh_numero
import utils.io_utils as io
import time

def gerar_valores_padrao(vetores):
    posicoes = io.obter_inteiro('Quantas posições? \n> ', tipo= "+")
    valor_padrao = input('Qual o valor padrão? \n> ')
    vetores = gerar_n_posicoes(posicoes, valor_padrao)
    mostrar_vetor(vetores, 10)
    return vetores
    
def gerar_n_posicoes(posicoes, valor_padrao = None):
    out = [None] * posicoes
    out = mapear(out, lambda x: valor_padrao, lambda x: x == None)
    out = mapear(out, lambda x: float(x), eh_numero)
    return out

def preencher_vetor_intervalo(vetores):
    minimo = io.obter_inteiro('Digite o valor mínimo: ')
    maximo = io.obter_inteiro('Digite o valor máximo: ')
    vetores = preencher_automaticamente_vetor(maximo, minimo)
    mostrar_vetor(vetores, 10)
    return vetores


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
        
        
def pedir_novo_vetor_e_verificar_se_esta_no_vetor(vetores):
    vetor_novo = []
    tamanho = io.obter_inteiro('Digite o tamanho do vetor: ', tipo='+')
    
    for i in range(tamanho):
        elemento = io.obter_numero(f'Digite o elemento ({i+1}): ')
        adcionar_elemento(vetor_novo, elemento)
        
    # Checando elementos:
    for item in vetor_novo:
        if item not in vetores:
            print('Nem todos os elementos estão no vetor!')
            return
        
    valores_presentes = filtrar(vetores, lambda x: x in vetor_novo)
    
    
    print('Filtro:', valores_presentes)
    print('Vetor criado:', vetor_novo)
    
    if valores_presentes == vetor_novo:
        print('Deu tudo certo grazadeus :)')
    else:
        print('Vem algo especial por aí')
        

def top_n_maiores(vetores):
    if obter_tamanho_vetor(vetores)== 0:
        print('Vetor nulo!')
        return
    n = io.obter_inteiro('N: ', tipo= '+')
    while n > obter_tamanho_vetor(vetores):
        print(f'{n} é maior que vetor (tamanho = {obter_tamanho_vetor(vetores)})!')
        n = io.obter_inteiro('N: ', tipo= '+')
    vetor_ordenado = quicksort(vetores)
    print(f'Os {n} maiores são: ', my_slice(vetor_ordenado, obter_tamanho_vetor(vetores) - n , obter_tamanho_vetor(vetores)))
    
def top_n_menores(vetores):
    if obter_tamanho_vetor(vetores)== 0:
        print('Vetor nulo!')
        return
    n = io.obter_inteiro('N: ', tipo= '+')
    while n > obter_tamanho_vetor(vetores):
        print(f'{n} é maior que vetor (tamanho = {obter_tamanho_vetor(vetores)})!')
        n = io.obter_inteiro('N: ', tipo= '+')
    vetor_ordenado = quicksort(vetores)
    print(f'Os {n} menores são: ', my_slice(vetor_ordenado, 0, n))
    

def analise_media(vetores):
    media = calcular_media_vetor(vetores)
    maiores_que_media = filtrar(vetores, lambda x: x > media)
    menores_que_media = filtrar(vetores, lambda x: x < media)
    exatamente_iguais = filtrar(vetores, lambda x: x == media)
    
    print(f'{menores_que_media} <= MÉDIA:{exatamente_iguais if obter_tamanho_vetor(exatamente_iguais) > 0 else media} <= {maiores_que_media}')
    
    
    
        
def mostrar_questao_grande(vetores):
    # 
    numeros_pares_pos = filtrar(vetores, lambda x: x % 2 == 0 and x > 0)
    if obter_tamanho_vetor(numeros_pares_pos) > 0:
        media_pares_pos = calcular_media_vetor(numeros_pares_pos)
    else:
        print('Sem pares positivos!')
        media_pares_pos = 0
    
    numeros_pares_neg =  filtrar(vetores, lambda x: x % 2 == 0 and x < 0)
    if obter_tamanho_vetor(numeros_pares_neg) > 0 and numeros_pares_neg[0] != 1:
        produto_numeros_neg = reduzir(numeros_pares_neg, lambda x, y: x * y , atual= 1)
    else:
        print('Sem pares negativos!')
        produto_numeros_neg = 0
    
    produto_numeros_neg /= 2
       
    
    print('Média positivos: ', media_pares_pos)
    print('Produto negativos: ', produto_numeros_neg)
    print(f'O resultado é {media_pares_pos + produto_numeros_neg}')
    
def ordem_crescente(vetores):
    geral = quicksort(vetores)
    
    menu = gerar_menu("TODOS",
                      "PARES",
                      "ÍMPARES",
                      "POSITIVOS",
                      "NEGATIVOS",
                      "MULTIPLOS DE N",
                      titulo= 'Escolha...')
    
    opcao = io.obter_numero_intervalo(menu, 6, 1)
    
    if opcao == 1:
        print(f'TODOS ORDENADOS: {geral}')
    
    elif opcao == 2:
        print(f'PARES: {filtrar(geral, lambda x: x % 2 == 0)}')
    
    elif opcao == 3:
        print(f'IMPARES: {filtrar(geral, lambda x: x % 2)}')
        
    elif opcao == 4:
        print(f'POSITIVOS: {filtrar(geral, lambda x: x > 0)}')
    
    elif opcao == 5:
        print(f'NEGATIVOS: {filtrar(geral, lambda x: x < 0)}')
    
    elif opcao == 6:
        n = io.obter_numero_positivo('N: ')
        multiplos_n = filtrar(geral, lambda x: x % n == 0)
        print(f'MULTIPLOS DE N: {multiplos_n}') if multiplos_n else print('Sem múltiplos de N')


def ordem_decrescente(vetores):
    geral = my_slice(quicksort(vetores), obter_tamanho_vetor(vetores) - 1, 0)
    
    menu = gerar_menu("TODOS",
                      "PARES",
                      "ÍMPARES",
                      "POSITIVOS",
                      "NEGATIVOS",
                      "MULTIPLOS DE N",
                      titulo= 'Escolha...')
    
    opcao = io.obter_numero_intervalo(menu, 6, 1)
    
    if opcao == 1:
        print(f'TODOS ORDENADOS: {geral}')
    
    elif opcao == 2:
        print(f'PARES: {filtrar(geral, lambda x: x % 2 == 0)}')
    
    elif opcao == 3:
        print(f'IMPARES: {filtrar(geral, lambda x: x % 2)}')
        
    elif opcao == 4:
        print(f'POSITIVOS: {filtrar(geral, lambda x: x > 0)}')
    
    elif opcao == 5:
        print(f'NEGATIVOS: {filtrar(geral, lambda x: x < 0)}')
    
    elif opcao == 6:
        n = io.obter_numero_positivo('N: ')
        multiplos_n = filtrar(geral, lambda x: x % n == 0)
        print(f'MULTIPLOS DE N: {multiplos_n}') if multiplos_n else print('Sem múltiplos de N')
        
def obter_e_apagar_numero_multiplo_N_M(vetores):
    n = io.obter_inteiro('N: ')
    m = io.obter_inteiro('M: ')
    multiplo_N_M = filtrar(vetores, lambda x: x % n == 0 and x % m == 0)
    if obter_tamanho_vetor(vetores) > 1:
        out = filtrar(vetores, lambda x: x not in multiplo_N_M)
        return out
    out = filtrar(vetores, lambda x: x != multiplo_N_M )
    print(f'Multiplo de n e m é {multiplo_N_M}') if obter_tamanho_vetor(multiplo_N_M) > 0 else print('Não há esse número!')
    return out

    
    
    

# Math utils

def calcular_media_vetor(vetor):
    quantidade = 0
    somatorio = 0
    for item in vetor:
        quantidade += 1
        somatorio += item
    return somatorio / quantidade

        
        
    
###### Menu_utils #####
def gerar_menu(*opcoes, titulo = '==== MENU ===='):
    menu = titulo
    for i in range(obter_tamanho_vetor(opcoes)):
        menu += f'\n{i + 1} - {opcoes[i]}'
    menu += '\n> '
    return menu

def gerar_numero_aleatorio_entre(min, max):
    return int(random() * (max - min) + min)
    

def mostrar_vetor(vetor, quantidade_max_valores = 6, center = False):
    if eh_matriz(vetor):
        print('VETOR DE VETORES')
        mostrar_matriz(matriz= vetor)
        return
    if obter_tamanho_vetor(vetor) == 0:
        if center:
            io.printcenter('Vetor sem itens ainda!')
        else:
            print('Vetor sem itens ainda!')
    elif len(vetor) > quantidade_max_valores:
        if center:
            io.printcenter(f'VETOR: {vetor[0 : quantidade_max_valores - 1]}\b...({len(vetor) - quantidade_max_valores} itens)...{vetor[len(vetor) - 1]}]')
        else:
            print(f'VETOR: {vetor[0 : quantidade_max_valores - 1]}\b...({len(vetor) - quantidade_max_valores} itens)...{vetor[len(vetor) - 1]}]')
    else:
        if not center:
            print(vetor)
            return
        io.printcenter(vetor)
        
def mostrar_matriz(matriz):
    for item in matriz:
        print(item)
        
def tchauzinho(arquivo_incrivel_motivacional_supermassa):
    mensagens = arquivo_incrivel_motivacional_supermassa.readlines()
    print('\n' + escolher_item_aleatorio(mensagens))

