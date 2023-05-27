from wordplay_utils import *
from Utils.vetor_utils import * 
from Utils.io_utils import *
def imprimir_palavras_maiores_20_caracteres(vetor):
    out = []
    for palavra in vetor:
        if len(palavra) > 20:
            out.append(palavra)
    mostrar_lista_resumida(out)
    print(f'Tem {len(out)} elementos na lista')

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
    
def imprimir_somente_letras_obrigatorias(vetor, letras_obrigatorias):
    out = filtrar(lambda x: usa_somente(x, letras_obrigatorias), vetor)
    mostrar_lista_resumida(out)
    printcenter(barra_total(len(out), len(vetor)))
    print(f'O total de palavras que só utilizam {letras_obrigatorias} é {len(vetor)}')
    

    
