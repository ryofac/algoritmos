from io_utils import *
def main():
    numero_n = obter_inteiro('Me diga qual o número da sequência você quer: ', tipo="+")
    cont = 0
    somador = 0
    while cont <= numero_n:
        print(f' + {1}/{cont}')
        cont += 1
        somador += 1/numero_n
    print('--------')
    print('=', 1/somador)
main()