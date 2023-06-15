def filtrar(vetor, regra, reverso=False):
    out = []
    for item in vetor:
        if reverso:
            if not regra(item):
                adcionar_elemento(vetor, item)
        else:
            if regra(item):
                adcionar_elemento(vetor, item)
    return out


def mapear(vetor, funcao_mapear, regra_mapeamento = lambda x: x):
    out = []
    for item in vetor:
        if regra_mapeamento(item):
            adcionar_elemento(out, funcao_mapear(item))
        else:
            adcionar_elemento(out, item)
    return out


def reduzir(vetor, funcao_acumuladora, atual, acumulado, regra= lambda x: x):
    for item in vetor:
        if regra(item):
            acumulado = funcao_acumuladora(acumulado, atual)
    return acumulado
            

def adcionar_elemento(vetor, elemento):
    vetor += [elemento]
    
    
def obter_tamanho_vetor(vetor):
    contador = 0
    for _ in vetor:
        contador += 1
    return contador
    

######## RANDOM FUNCTIONS ##########
from random import random

def escolher_item_aleatorio(vetor):
    return vetor[int(random() * obter_tamanho_vetor(vetor))]

