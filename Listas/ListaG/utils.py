from time import sleep


def pedir_inteiro(label= 'Me diga um número inteiro:\n> ', tipo = None):
    if not tipo:
        try:
            num = int(input(label))
        except:
            print('Não é um número!')
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


def printslow(palavra): # Escrever o texto lentamente(
    for letra in palavra:
        print(letra, end='', flush=True)
        sleep(0.05)
    print('\n')
    
def title(txt, center = True, estrelado = False, upper=False):
    if upper:
        txt = txt.upper()
    if not center:
        print('=' * (len(txt)))
        print(txt)
        print('=' * len(txt))
    if estrelado:
        print('*' * (len(txt) + 2))
        print(txt.center(len(txt) + 2))
        print('*' * (len(txt) + 2))
    else:
        print('=' * (len(txt) + 2))
        print(txt.center(len(txt) + 2))
        print('=' * (len(txt) + 2))
        


def contar_ate(num):
    contador = 0
    while contador != num:
        contador += 1
        print(contador)