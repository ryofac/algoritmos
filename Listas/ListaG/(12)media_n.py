from io_utils import *
import os

frases_legais_para_pedir_inteiro = ['Ok, me diga outro número: ', 'Passe mais um número: ',
                                    'Diga um número inteiro positivo: ', 'Diga outro: ']

def main():
    clear_screen()
    title('Calcular Média Aritmética', upper=True)   
   
    # Pedir N que será o tamanho da lista:
    tamanho = pedir_inteiro('Qual o tamanho da lista?: ')
    
    # Definir tamanho inicial:
    inicio = 0
    
    # Soma dos números inputados (Assume como o primeiro valor o primeiro numero inputado):
    soma_dos_numeros = pedir_inteiro('Me diga o número que lhe darei a média: ', tipo="+")
    
    while inicio < tamanho - 1:
        
        title(f'({inicio + 1})/({tamanho})')
        print()
        numeros = pedir_inteiro(choice(frases_legais_para_pedir_inteiro), tipo="+")
        os.system('clear')
        inicio += 1 # Convergência de dados
        soma_dos_numeros += numeros
        
    title('Resultado da média:')
    printslow(f"O Resultado da média dos {tamanho} números que você digitou foi: {media(soma_dos_numeros, tamanho)}")
    
def media(soma, quantidade):
    return soma / quantidade

main()