# Leia um vetor A com 20 elementos, calcule e escreva o valor de S.
# S = (A[1] - A[20])2 + (A[2] - A[19])2 + ... + (A[9] - A[12])2 + (A[10] - A[11])2

def main():
    print('Digite 20 elementos!')
    vetor_a = [int(input(f'Digite o elemento ({c})')) for c in range(21)]
    
    soma = somatorio_S(vetor_a)
    
    print('O somatorio S é', soma)
    
def somatorio_S(colecao):
    somatorio = 0
    for i in range(len(colecao)):
        somatorio += (colecao[i] - colecao[20 - i]) ** 2
        
    return somatorio
        

        
        
main()