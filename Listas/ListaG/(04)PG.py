from utils import *
def main():
    title('Formador de Progração Geométrica')
    a0 = pedir_inteiro("Me diga o número inicial da PG:\n> ")

    limite = pedir_inteiro("Quantos termos você quer para essa PG: ", tipo="+")
    razao = pedir_inteiro('Diga a razão:  ')
    contador = 0

    while contador != limite:
        print(f'({contador + 1}) -> {a0}')
        contador += 1
        a0 *= razao
        
    printslow('Essa foi sua PG!')

main()