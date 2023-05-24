
def main():
    elementos = int(input('Digite quantos elemntos vc quer no vetor: '))
    vetorA = []

    for i in range(elementos):
        elemento = int(input('Digite os elementos do vetor: '))
        vetorA.append(elemento)
    
    b_vetor = inverter_colecao(vetorA)

    print(b_vetor)

def  inverter_colecao(a_vetor):
    colecao_invertida = []
    for i in range(len(a_vetor)):
        colecao_invertida.append(a_vetor[len(a_vetor) - 1 - i])
    return colecao_invertida

main()