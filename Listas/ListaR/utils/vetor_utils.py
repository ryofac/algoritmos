from str_utils import eh_numero


def filtrar(vetor, regra, reverso=False, matriz_como_vetor = False):
    out = []
    if not eh_matriz(vetor) or matriz_como_vetor:
        for item in vetor:
            if reverso:
                if not regra(item):
                    adcionar_elemento(out, item)
            else:
                if regra(item):
                    adcionar_elemento(out, item)
    else:
        for item in vetor:
            parte_matriz = []
            for valor in item:
                if reverso:
                    if not regra(valor):
                        adcionar_elemento(parte_matriz, valor)
                else:
                    if regra(valor):
                        adcionar_elemento(parte_matriz, valor)
            adcionar_elemento(out, parte_matriz)
    return out


def mapear(vetor, funcao_mapear, regra_mapeamento = lambda x: x, matriz_como_vetor = False):
    out = []
    if not eh_matriz(vetor) or matriz_como_vetor:
        for item in vetor:
            if regra_mapeamento(item):
                adcionar_elemento(out, funcao_mapear(item))
            else:
                adcionar_elemento(out, item)
    else:
        for item in vetor:
            parte_matriz = []
            for valor in item:
                if regra_mapeamento(valor):
                    adcionar_elemento(parte_matriz, funcao_mapear(valor))
                else:
                    adcionar_elemento(parte_matriz, valor)
            adcionar_elemento(out, parte_matriz)
    return out


def reduzir(vetor, funcao_acumuladora, atual = None, regra= lambda x: x, matriz_como_vetor = False):
    
    if not eh_matriz(vetor) or matriz_como_vetor:
        if atual == None and regra(vetor[0]):
            acumulado = vetor[0]
        else: 
            acumulado = atual       
        for i in range(obter_tamanho_vetor(vetor)):
            if regra(vetor[i]):
                # print(acumulado, vetor[i])
                acumulado = funcao_acumuladora(acumulado, vetor[i])
        return acumulado if acumulado != None else 0
    
    else:
        if atual == None and regra(vetor[0][0]):
            acumulado = vetor[0][0]
        else:
            acumulado = atual
            
        for i in range(obter_tamanho_vetor(vetor)):
            for j in range(obter_tamanho_vetor(vetor[i])):
                if regra(vetor[i][j]):
                    # print(acumulado, vetor[i][j])
                    acumulado = funcao_acumuladora(acumulado, vetor[i][j])  
        return acumulado if acumulado != None else 0
        
### Ordenar ###

def quicksort(vetor , reverso= False):
    if obter_tamanho_vetor(vetor) <= 1:
        return vetor
    pivot = escolher_item_aleatorio(vetor)
    igual = filtrar(vetor, lambda x: x == pivot)
    right = filtrar(vetor, lambda x: x > pivot)
    left = filtrar(vetor, lambda x: x < pivot)
    if reverso:
        return quicksort(right, reverso= True) + igual + quicksort(left, reverso= True)
    return quicksort(left) + igual + quicksort(right)
    
            

def adcionar_elemento(vetor, elemento):
    vetor += [elemento]
    
def vetor_sem_elemento(vetor, elemento):
    out = []
    for item in vetor:
        if not item == elemento:
            adcionar_elemento(out, item)
    return out

def my_slice(vetor, inicio, final):
    out = []
    
    while inicio < final:
        adcionar_elemento(out, vetor[inicio])
        inicio += 1
        
    while inicio > final:
        adcionar_elemento(out, vetor[inicio])
        inicio -= 1
        
    return out
        

def maior_numero_vetor(vetor):
    maior_numero = reduzir(vetor, lambda x, y: x if x > y else y, regra= eh_numero)
    return maior_numero

def menor_numero_vetor(vetor):
    menor_numero = reduzir(vetor, lambda x, y: x if x < y else y, regra= eh_numero)
    return menor_numero
    
    
def obter_tamanho_vetor(vetor):
    contador = 0
    for _ in vetor:
        contador += 1
    return contador

def eh_matriz(vetor):
    for item in vetor:
        if type(item) == list:
            return True
    return False

######## RANDOM FUNCTIONS ##########
from random import random

def escolher_item_aleatorio(vetor):
    if eh_matriz(vetor):
        lista_unica = []
        for item in vetor:
            for valor in item:
                adcionar_elemento(lista_unica, valor)
        return lista_unica[int(random() * obter_tamanho_vetor(lista_unica))]
    
    return vetor[int(random() * obter_tamanho_vetor(vetor))]



