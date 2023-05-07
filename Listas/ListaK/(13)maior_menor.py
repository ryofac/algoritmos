from io_utils import *
from random import choice

frases_legais_para_pedir_inteiro = ['Ok, me diga outro: ', 'Passe mais um número: ', 
                                    'Digite mais um: ', 'Digite outro: ']

def main():
    clear_screen()
    title('Check Maior ou Menor', upper=True)
    # Entrada
    quantidade_n = pedir_inteiro('Quantos termos você quer na lista?: ')
    numero_atual = pedir_inteiro('Ok, me diga o primeiro número da lista: ')
    
    # Processamento
    menor_numero = maior_numero = numero_atual
    
    for c in range(0, quantidade_n): # For numérico
        novo_numero = pedir_inteiro(choice(frases_legais_para_pedir_inteiro))
        if novo_numero > maior_numero:
            maior_numero = novo_numero
        if novo_numero < menor_numero:
            menor_numero = novo_numero
    # Saída
    title(f'Maior: {maior_numero}')
    title(f'Menor: {menor_numero}')

main()