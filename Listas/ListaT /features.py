from utils.vetor_utils import *
from utils.io_utils import *
from utils.matrizes_utils import *
from utils.str_utils import *


def checar_valores_nulos(data):
    if not data['quantidade_premios']:
        data['quantidade_premios'] = obter_inteiro('Quantos prêmios vão ser distribuidos? \n> ', tipo ="+")
        data['max_premios'] = data['quantidade_premios']
    if not data['valor_ponto']:
        data['valor_ponto'] = obter_numero_positivo('Qual o valor do ponto na rifa? \n> R$')
    if not data['taxa_adm']:
        data['taxa_adm'] = obter_numero_positivo('Qual a taxa de adm? \n(%) > ')
        
        
def obter_numero_de_pontos(data):
    livres = data['pontos_disponiveis']
    aptos = data['pontos_comprados']
    print(f'Há {len(aptos)} pontos vendidos na rifa!')
    print(f'Ainda tem {len(livres)} para serem vendidos!')
    

def numero_cada_pessoa_posicao(data):
    pessoas = data['pessoas']
    pontos_comprados = data['pontos_comprados']
    pontos_disponiveis = data['pontos_disponiveis']
    print('COMPRADOS: ')
    for i in range(len(pessoas)):
        for j in pontos_comprados:
            if i == j:
                print(f'#{i+1} -> {pessoas[i]}')
    
    print('DISPONIVEIS: ')
    for i in range(len(pessoas)):
        for j in pontos_disponiveis:
            if i == j:
                print(f'#{i+1} -> {pessoas[i]}')
    

def sortear(pontos_comprados, ganhadores, pontos_disponiveis):
    ganhador = escolher_item_aleatorio(pontos_comprados)
    
    while ganhador in ganhadores: # Verifica se já foi sorteado!
        ganhador = escolher_item_aleatorio(len(pontos_comprados))
        
    return ganhador

def realizar_sorteio(data):
    pessoas = data['pessoas']
    ponto_ganhador = sortear(data['pontos_comprados'], data['pontos_sorteados'], data['pontos_disponiveis'])
    data['pontos_sorteados'].append(ponto_ganhador + 1)
    if data['quantidade_premios'] > 0:
        data['quantidade_premios'] -= 1
    else:
        print('Sem prêmios!')
        return
    print(pessoas[ponto_ganhador], ponto_ganhador + 1)
    data['pontos_comprados'] = filtrar(data['pontos_comprados'], lambda x: x != ponto_ganhador)
    
def obter_pontos_disponiveis(pessoas):
    out = []
    for i in range(len(pessoas)):
        if '-' in pessoas[i]:
            out.append(i)
    return out


def obter_pontos_comprados(pessoas):
    out = []
    for i in range(len(pessoas)):
        if '-' not in pessoas[i]:
            out.append(i)
    return out
    
        
def obter_visao_geral(data):
    taxa_adm = data['taxa_adm']
    premios = data['quantidade_premios']
    valor_ponto = data['valor_ponto']
    ganhadores = data['pontos_sorteados']
    total_arrecadado = (data['max_premios'] * valor_ponto)
    
    print(f'PONTOS SORTEADOS: {ganhadores}')
    print(f'PRÊMIOS DISPONÍVEIS: {premios}')
    print(f'VALOR DO PONTO ATUAL: R${valor_ponto:.2f}')
    print(f'VALOR TOTAL ARRECADADO: R${total_arrecadado}')
    print(f'TAXA DE ADM({taxa_adm:.2f}%): {total_arrecadado * taxa_adm/100}')
    
