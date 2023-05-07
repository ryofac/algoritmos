from io_utils import *
def main():
    title('Formador de Progressão Geométrica')
    a0 = pedir_inteiro("Me diga o número inicial da PG:\n> ")

    limite = pedir_inteiro("Quantos termos você quer para essa PG: ", tipo="+")
    razao = pedir_inteiro('Diga a razão:  ')

    for c in range(limite):
        print(f'({c + 1}) -> {a0}')
        a0 *= razao
        
    printslow('Essa foi sua PG!')

main()