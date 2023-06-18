from io_utils import *
def main():
    n = obter_inteiro('Digite a quantidade de números da sequência de fib que você quer obter: ', tipo="+")
    print('SEQUÊNCIA: ', gerar_vetor_fib(n),'\b\b...]')
    

def gerar_vetor_fib(n_elementos):
    out = []
    for i in range(n_elementos):
        if i <= 1:
            out.append(1)
        else:
            out.append(out[i-1] + out[i-2])
    return out

main()