from Utils.vetor_utils import * 
def imprimir_palavras_maiores_20_caracteres(vetor):
    out = []
    for palavra in vetor:
        if len(palavra) > 20:
            out.append(palavra)
    print(f'> {out}')

def imprimir_palavras_com_e(vetor):
    print(filtrar(tem_e, vetor))
    
def tem_e(palavra):
    return contem_caracter(palavra, 'e')