from time import time
def main():
    vetor = [1, 2, 5, 4, 3 , 2, 12313, -100]
    
    
def bubble_organizar_vetor(vetor): # Função Bubble Sort
    for i in range(len(vetor) - 1): # Percorrer os itens do vetor
        for j in range(len(vetor) - i - 1): #  -> Quantidade de vezes que irá acontecer <-
            if vetor[j] > vetor[j+1]:
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j] # "Swap", troca os elementos se o da direita for maior
                # -> Faz os valores maiores "Flutuarem"
    return vetor


def quick_organizar_vetor(vetor):
    if len(vetor) <= 1:
        return vetor
    indice_aleatorio_vetor = int(time() * 100000) % len(vetor) # Só pra gerar aleatório
    pivot = vetor[indice_aleatorio_vetor]
    equal = []
    left = []
    right = []
    for item in vetor:
        if item == pivot:
            equal.append(item)
        if item > pivot:
            right.append(item)
        if item < pivot:
            left.append(item)
    return quick_organizar_vetor(left) + equal + quick_organizar_vetor(right)
