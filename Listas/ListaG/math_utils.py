import io_utils as io
from os import system


def contar_ate(num):
    contador = 0
    while contador != num:
        contador += 1
        io.printslow(f'...{contador}', speed= 0.5)
        system("clear")

def fatorial(num):
    multiplicador = 1
    contador = 0
    while contador < num:
        contador += 1
        multiplicador *= contador
    return multiplicador

def eh_multiplo(numero, candidato):
    return numero % candidato == 0


def eh_par(numero):
    return numero % 2 == 0

def eh_primo(numero):
    anterior = 1
    cont_multiplos = 0
    while anterior < numero:
        anterior += 1
        if eh_multiplo(numero, anterior):
            cont_multiplos += 1
    return cont_multiplos == 1

def fib(num): # Utilizando o conceito de recursividade
    if num == 1 or num == 2:
        return 1
    else:
        return fib(num-1) + fib(num-2)
    

if __name__ == "__main__":
    io.title('math utils', upper=True)
    io.printslow('Olá, sou o módulo extra para o facilitamento de algumas ações matemáticas!')
    io.printslow('Eu não consigo rodar sozinho, para me testar, vá em algum módulo.py em que eu esteja presente!')


