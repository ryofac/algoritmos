
def main():
    tamanho = int(input('Digite o tamanho: '))
    vetor_a = [int(input(f'Digite o elemento: ({i + 1}) / ({tamanho}) ')) for i in range(tamanho)]
    print(tem_igual(vetor_a))

def tem_igual(colecao: list) -> bool:
    verificados = []
    for item in colecao:
        if item in verificados:
            return True
        else:
            verificados.append(item)
    return False 
    
main()
