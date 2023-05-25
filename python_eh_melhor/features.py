from utils import gerar_vetor_aleatorio, obter_posicoes_em_vetor
import os


def gerar_vetor():
    tamanho = int(input("Quantos elementos\n> "))
    numeros = gerar_vetor_aleatorio(tamanho)
    return numeros

def localizar_posicoes(numeros): 
    numero = int(input("Número: "))
    posicoes = obter_posicoes_em_vetor(numeros, numero)

    if len(posicoes) > 0: 
        print(f"Número {numero} localizado nas posições: {posicoes}")
    else:
        print("Número não pertence aos vetores!")

def multiplicar_cada_numero_por_n(numeros): 
    vetor = [0] * len(numeros)
    n = int(input("Multiplicador: "))

    for i in range(len(numeros)):
        vetor[i] = numeros[i] * n

    return vetor

def enter_limpar_tela():
    input('<ENTER to continue...> ')
    
    os.system('clear')  

def enter_limpar_tela():
    os.system('clear')

if __name__ == '__main__':
    enter_limpar_tela()
