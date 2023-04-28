from random import *
def main():
    arquivo = open("./alunos.txt")
    alunos_def = arquivo.readlines()
    shuffle(alunos_def)

    grupo1 = alunos_def[:20]
    grupo2 = alunos_def[20:40]
    grupo3 = alunos_def[40:]
    
    
    header('GRUPO 1')
    show_list(grupo1)
    header('GRUPO 2')
    show_list(grupo2)
    header('GRUPO 3')
    show_list(grupo3)

def show_list(lst):  # Função que retorna uma lista numerada
    cont = 0
    for element in lst:
        cont += 1
        print(f'({cont}) {element}', end='')

def header(txt):  # Função para formatação de texto
    print('=' * len(txt))
    print(txt.upper())
    print('=' * len(txt))

main()