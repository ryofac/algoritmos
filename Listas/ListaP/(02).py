
def main():
    tamanho = int(input('Qual o tamanho dos arrays: '))
    print('Digite os elementos de A: ')
    vetor_a = [int(input('> ')) for c in range(tamanho)]
    print('Digite os elementos de B: ')
    vetor_b = [int(input('> ')) for c in range(tamanho)]

    # conj = inter(vetor_a, vetor_b)
    # uni = uniao(vetor_a, vetor_b)
    # print('Conjunto A inter B: ', conj)
    # print('Conjunto A união B: ', uni)

    tem_igual(vetor_a, vetor_b)

def tem_igual(a, b):
    vector_c = a + b
    intersecao = []
    uniao = []
    print(vector_c)
    verificados = []
    for item in vector_c:
        if item in verificados:
            if not item in intersecao:
                intersecao.append(item)
        else:
            verificados.append(item)
            uniao.append(item)
    
    print(intersecao)
    print(uniao)

# def uniao(vetorA, vetorB):
#     uniao_repetido = vetorA + vetorB
#     verificados = []
#     for item in uniao_repetido:
#         verificados.append(item)
#         if item in verificados:
#             uniao_repetido.pop(item)

#     return uniao_repetido

# def inter(colA, colB):
#     inter = []
#     for c in colA:
#         if c in colB:
#             inter.append(c)
#     return inter

# def tem_igual(colecao: list) -> bool:
#     verificados = []
#     iguais = []
#     for item in colecao:
#         if item in verificados:
#             iguais.append(item)
#         else:
#             verificados.append(item)
#     return iguais
    

main()