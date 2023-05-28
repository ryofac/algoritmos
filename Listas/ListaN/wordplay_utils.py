from Utils.vetor_utils import contem_caracter, lowercase_char, uppercase_char, inverter_palavra
from Utils.math_utils import escolher_aleatorio


def texto_tem(palavra: str, char:str) -> bool:
    return contem_caracter(palavra, lowercase_char(char)) or contem_caracter(palavra, uppercase_char(char))


def texto_nao_tem_nenhum(palavra: str, chars: list[str]):
    for char in chars:
        char = str(char)
        if contem_caracter(palavra, lowercase_char(char)) or contem_caracter(palavra, uppercase_char(char)):
            return False
    return True


def retirar_espacos(vetor) -> list:
    return mapear(lambda x: x.strip(), vetor)


def mapear(func, vetor: list) -> list:
    out = []
    for item in vetor:
        out.append(func(item))
    return out


def filtrar(func: bool, vetor: list) -> list:
    out = []
    for item in vetor:
        if func(item):
            out.append(item)
    return out


def usa_somente(palavra: str, letras: list[str]):
    for letra in palavra:
        if not texto_tem(letras, letra):
            return False
    else:
        return True
            
    
def barra_total(valor_obtido:float, valor_total:float):
    porcentagem = valor_obtido / valor_total * 100
    multiplicador = int(porcentagem // 10)
    total = ' ' * 10
    progresso = '#' * multiplicador
    quanto_falta = ' ' * (len(total) - len(progresso))
    return f'[{progresso}{quanto_falta}] (≃ {porcentagem:.3f}%) do total!'


def mostrar_lista_resumida(lista):
    if len(lista) > 6:
        print(f' {lista[0:5]}\b...({(len(lista) - 1) - 5} itens)...{lista[len(lista) - 1]}]')
    else:
        print(lista)
        

def texto_tem_letras(palavra, letras_obrigatorias):
    for letra in letras_obrigatorias:   
        if not texto_tem(palavra, letra):
            return False
    return True


def eh_palindromo(palavra):
    palavra_invertida = inverter_palavra(palavra)
    return palavra == palavra_invertida

    
def listar_elementos(lista):
    for elemento in lista:
        print('> ' + elemento)
        
    
def encerrar_programa(arquivo_despedida):
    despedidas = arquivo_despedida.readlines()
    if despedidas:
        print('(LOG)')
        print(escolher_aleatorio(despedidas))
    else:
        print('Arquivo de despedidas não setado!')
