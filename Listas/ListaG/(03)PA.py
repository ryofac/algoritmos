# Leia as variáveis A0, Limite e R e escreva os valores menores que Limite gerados pela Progressão
# Aritmética que tem por valor inicial A0 e razão R.
from utils import *
def main():
    title('Formador de Progressão Aritmética')
    a0 = pedir_inteiro("Me diga o número inicial da PA:\n> ")

    limite = pedir_inteiro("Quantos termos você quer para essa PA? ", tipo="+")
    razao = pedir_inteiro('Diga a razão:  ')
    contador = 0

    while contador != limite:
        print(f'({contador + 1}) -> {a0}')
        contador += 1
        a0 += razao
        
    printslow('Essa foi sua PA!')

main()