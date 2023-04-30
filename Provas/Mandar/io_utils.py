from time import sleep
from os import system, get_terminal_size

def obter_tamanho_tela():
    return get_terminal_size().columns


def pedir_inteiro(label= 'Me diga um número inteiro:\n> ', tipo = None):
    if not tipo:
        try:
            num = int(input(label))
        except:
            print('Não é um inteiro!')
            while not num:
                num = int(input(label))
        return num
    if tipo == '+':
        num = int(input(label))
        while not num > 0:
            print('Digite um número positivo!')
            num = int(input(label))
        return num
    if tipo == '-':
        num = int(input(label))
        while not num <= 0:
            print('Digite um número negativo!')
            num = int(input(label))
        return num

def pedir_float(label ='Me diga um número: ', tipo = None):
    if not tipo:
        try:
            num = float(input(label))
        except:
            print('Não é um número!')
            while not num:
                num = float(input(label))
        return num
    if tipo == '+':
        num = float(input(label))
        while not num > 0:
            print('Digite um número positivo!')
            num = float(input(label))
        return num
    if tipo == '-':
        num = float(input(label))
        while not num <= 0:
            print('Digite um número negativo!')
            num = float(input(label))
        return num
    

 # Escrever o texto lentamente (quando -speed, mais rápido)
def printslow(*palavras, speed = 0.04, inline = False):
    for elemento in palavras:
        for letra in elemento:
            print(letra, end='', flush=True)
            sleep(speed)
    if not inline:
        print('\n')
    
def title(txt, center = True, estrelado = False, upper=False):
    if upper:
        txt = txt.upper()
    if not center:
        print('=' * (len(txt)))
        print(txt)
        print('=' * len(txt))
    elif estrelado:
        print('*' * (len(txt) + 2))
        print(txt.center(len(txt) + 2))
        print('*' * (len(txt) + 2))
    else:
        print('=' * (len(txt) + 2))
        print(txt.center(len(txt) + 2))
        print('=' * (len(txt) + 2))

def centralize(txt):
    return txt.center(obter_tamanho_tela() - 2)

def printcenter(txt):
    print (centralize(txt))

def clear_screen():
    system('clear')


if __name__ == "__main__":
    title('io_utils', upper=True)
    printslow('Olá, sou o módulo extra para as funções de entrada e saída do Python!')
    printslow('Eu não consigo rodar sozinho, para me testar, vá em algum módulo.py em que eu esteja presente!')

        


