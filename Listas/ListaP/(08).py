# Leia um vetor com N elementos, encontre e escreva o maior e o menor elemento e suas respectivas
# posições no vetor.

def main():
    vetor_a = [int(i) for i in input('Diga a sua lista: ').split()]
    
    maior, menor = qual_maior_menor(vetor_a)
    
    if maior == menor:
        print('A lista só contém elementos iguais!')
    else:
        print(f'O menor valor é {menor}')
        print(f'O maior valor é {maior}')
        
  
        
        
def qual_maior_menor(colecao: list[int]) -> tuple[int]:
    maior_valor = float('-inf')
    menor_valor = float('inf')

    for item in colecao:
        if item > maior_valor:
            maior_valor = item
        if item < menor_valor:
            menor_valor = item
    
    return maior_valor, menor_valor
    
main()