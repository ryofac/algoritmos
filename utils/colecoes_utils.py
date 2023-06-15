def obter_tamanho(colecao):
    contador = 0
    for item in colecao:
        contador += 1
    return contador


def adcionar_elementos(colecao, *elementos):
    for elemento in elementos:
        colecao += [elemento]

def remover_elemento(colecao, elemento):
    out = []
    for i in range(obter_tamanho(colecao)):
        if colecao[i] == elemento:
            continue
        adcionar_elementos(out, colecao[i])
    colecao = [out]
    
            
        
        

if __name__ == '__main__':
    lista = [0,1,2]
    print(obter_tamanho(lista))
    adcionar_elementos(lista, 1,2,3,4)
    print(lista)
    remover_elemento(lista, 1)
    print(lista)
    