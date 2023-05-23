from io_utils import *
somador = 0
def main():
    numero_n = obter_inteiro('Me diga qual o número da sequência você quer: ', tipo="+")
    somador = 0
    for c in range(1, numero_n + 1):
        somador += 1/numero_n
        print(f' + {1}/{c}')
    print('--------')
    print('=', somador)
main()
