def main():
    cont_teste = 0
    while True:
        cont_teste += 1
    
        tamanho = int(input())
        if tamanho == 0:
            break
        
        soma_beto = 0
        soma_aldo = 0
        
        for c in range(tamanho):
            aldo, beto = [int(x) for x in input().split()]
            soma_beto += beto
            soma_aldo += aldo
        ganhador = definir_ganhador(soma_aldo, soma_beto)
        print(f'Teste {cont_teste}\n{ganhador}\n')
        
        
def definir_ganhador(pontoA, pontoB):
    return ('Aldo') if pontoA > pontoB else ('Beto')
        
    
    
main()