def main():
    tamanho_a = int(input('Qual é o tamanho da lista A? \n> '))
    vetor_a = [input('> ') for c in range(tamanho_a)]
    tamanho_b = int(input('Qual é o tamanho da lista B? \n> '))
    vetor_b = [input('> ') for c in range(tamanho_b)]

    vetor_c = juntar_arrays(vetor_a, vetor_b)

    print(vetor_c)

def juntar_arrays(vetorA, vetorB):
    vetorResultante = []
    while len(vetorA) + len(vetorB) != 0:
        if len(vetorA) > 0:
            vetorResultante.append(vetorA.pop())
        if len(vetorB) > 0:
            vetorResultante.append(vetorB.pop())
    return vetorResultante
        
        
main()