# Leia as variáveis A0, Limite e R e escreva os valores menores que Limite gerados pela Progressão
# Aritmética que tem por valor inicial A0 e razão R.
from io_utils import *
def main():
    clear_screen()
    # Entrada
    title('Formador de Progressão Aritmética')
    a0 = pedir_inteiro("Me diga o número inicial da PA:\n> ")
    # Processamento
    limite = pedir_inteiro("Quantos termos você quer para essa PA? ", tipo="+")
    razao = pedir_inteiro('Diga a razão:  ')
    
    for c in range(limite): # For 'numérico
        print(f'({c + 1}) -> {a0}')
        a0 += razao
    
    # Saída
    printslow('Essa foi sua PA!')

main()