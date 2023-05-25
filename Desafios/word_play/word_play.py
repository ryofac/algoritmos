from utils.io_utils import *
from utils.math_utils import *
from utils.str_utils import *
import sys

def main():
    while True:
        arquivo = open("/home/ryan/Algoritmos/Desafios/word_play/words.txt")
        print('Arquivo carregado!')
        menu()
        printslow('O que deseja fazer? ')
        escolha = obter_inteiro('> ', tipo='+')
        
        if escolha == 1:
            contador_palavras = 0
            for linha in arquivo:
                print(linha)
                contador_palavras +=1
            print(f'A quantidade de palavras total é de {contador_palavras}')
        
        if escolha == 2:
            tamanho_n = obter_inteiro('Qual o tamanho máximo que você quer obter? \n> ')
            
            for palavra in arquivo:
                palavra = remover_caracter(palavra, ' ')
                if obter_tamanho(palavra) <= tamanho_n + 1:
                    print(palavra)
        
        if escolha == 3:
            caracter_analisado = obter_char("Qual o caractere a ser analisado?")
            for palavra in arquivo:
                if not contem_caracter(palavra, caracter_analisado):
                    print(palavra)

        
def menu():
    opcoes = ['1 - Listar todas as palavras', 
              '2 - Mostrar palavras com no mínimo N caracteres', 
              '3 - Palavras que não contém letras',
              '4 - Palavras contém todas as letras']
    for opcao in opcoes:
        print(opcao)
main()