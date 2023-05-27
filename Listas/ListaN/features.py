from wordplay_utils import *
from Utils.vetor_utils import * 
from Utils.io_utils import *
def imprimir_todas(vetor):
    mostrar_lista_resumida(vetor)
    print(f'Tem o total de : {len(vetor)}')
    
    
def imprimir_palavras_maiores_que_N(vetor, limite):
    out = []
    for palavra in vetor:
        if len(palavra) > limite:
            out.append(palavra)
    mostrar_lista_resumida(out)
    printcenter(barra_total(len(out), len(vetor)))
    print(f'Tem {len(out)} palavras maiores que {limite} caracteres na lista')
    

def imprimir_sem_char(vetor, char):
    out = filtrar(lambda x: not(texto_tem(x, char)), vetor)
    mostrar_lista_resumida(out)
    printcenter(barra_total(len(out), len(vetor)))
    print(f'O total de palavras sem {char} é de {len(out)}')
    

def imprimir_sem_letras_proibidas(vetor, letras_proibidas):
    out = filtrar(lambda x: texto_nao_tem_nenhum(x, letras_proibidas), vetor)
    mostrar_lista_resumida(out)
    printcenter(barra_total(len(out), len(vetor)))
    print(f'O total de palavras sem letras proibidas é de: {len(out)}')
    
    
def imprimir_somente_contem_letras(vetor, letras_obrigatorias):
    out = filtrar(lambda x: usa_somente(x, letras_obrigatorias), vetor)
    mostrar_lista_resumida(out)
    printcenter(barra_total(len(out), len(vetor)))
    print(f'O total de palavras que só utilizam {letras_obrigatorias} é {len(vetor)}')
    

def imprimir_contem_letras(word_list, letras_obrigatorias):
    out = filtrar(lambda x: texto_tem_letras(x, letras_obrigatorias), word_list)
    print(out)


def imprimir_letras_max(vetor, limite):
    out = []
    for palavra in vetor:
        if len(palavra) <= limite:
            out.append(palavra)
    mostrar_lista_resumida(out)
    printcenter(barra_total(len(out), len(vetor)))
    print(f'Tem {len(out)} palavras com no máximo {limite} caracteres')
    

def imprimir_palavras_palindromas(vetor):
    out = filtrar(lambda x: eh_palindromo(x), vetor)
    listar_elementos(out)

    
