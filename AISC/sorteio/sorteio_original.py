
# O código recebe uma lista e sorteia em grupos as pessoas da lista recebida
# Feito por Ryan e Lívia
from random import *
arquivo = open("/home/ryan/Algoritmos/AISC/sorteio/alunos.txt") # coloca o diretório dos dados
alunos_def = list(map(str.strip, arquivo.readlines()))

def main():
    grupos_separados = []  # Lista que recebe os grupos já separados
    alunos = alunos_def.copy()  # Copia a "base de dados"

    # Loop principal do programa:
    while True:
        print('>> SORTEADOR DE GRUPOS <<')
        if len(grupos_separados) > 0:
            header('Grupos:')
            count = 0
            for element in grupos_separados:
                count2 = 0
                count +=1 
                header(f'Grupo {count}')
                for nome in element:
                    count2 += 1
                    print(f'({count2}) {nome}')
        header('Digite a opção!')
        menu(alunos)
        question = int(input('> '))  # Abre uma sequência condicional de opções
        if question == 1:
            if len(alunos) == 0:
                print('A lista não tem mais valores!')
            else:
                integrantes = int(input('Quantos integrantes máximos você quer ter em um grupo?\n > '))
                # integrantes = integrantes + 1
                
                if len(alunos) % integrantes == 0:
                    for c in range(len(alunos) // integrantes):
                        escolhidos = escolher(alunos,
                                              integrantes)  # Integrantes assume o valor de k e define o tamanho de cada grupo
                        grupos_separados.append(escolhidos)
                else:
                    q1 = str(input('Vai ter um grupo com menos alunos... \n Quer continuar?(y/n) \n > ')).strip()
                    if q1 in 'YySs':
                        for c in range(len(alunos) // integrantes):
                            escolhidos = escolher(alunos,
                                                  integrantes)  # Integrantes assume o valor de k e define o tamanho de cada grupo
                            grupos_separados.append(escolhidos)

                        sobra = len(alunos) % integrantes  # a sobra significa os alunos que não couberam na divisão inteira
                        resto = escolher(alunos, sobra)
                        grupos_separados.append(resto)
                    else:
                        print('Retornando...')

        elif question == 2:
            alunos = alunos_def.copy()
            grupos_separados = []

        elif question == 3:
            if len(alunos) > 0:
                header('Alunos:')
                show_list(alunos)

            else:
                print('Sem dados!')
                
        elif question == 4:
            shuffle(alunos)
            print('Bagunçada!')
        else:
            break
    header('Obrigado por executar :)')


def escolher(lista, quantos):  # Essa função recebe uma lista e quantos valores vai escolher dessa lista
    nao_escolhidos = []  # Essa lista serve para controle, ela existe temporariamente dentro do programa
    escolhas = sample(lista, quantos)
    for aluno in lista:
        if aluno not in escolhas:
            nao_escolhidos.append(aluno)
    lista.clear()
    lista.extend(nao_escolhidos)

    return escolhas


def header(txt):  # Função para formatação de texto
    print('=' * len(txt))
    print(txt.upper())
    print('=' * len(txt))


def show_list(lst):  # Função que retorna uma lista numerada
    cont = 0
    for element in lst:
        cont += 1
        print(f'({cont}) {element}')


def menu(alunos):  # retorna o menu de opções
    print('1- para separar os grupos')
    print('2- para resetar valores')
    print(f'3- para ver todos os alunos disponíveis ({len(alunos)})')
    print('4- para deixar as coisas mais interessantes')
    print('5- para sair')


main()
