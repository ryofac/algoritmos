def main():
    qunt_pecas = int(input())
    
    pecas_totais = [x for x in range(1, qunt_pecas + 1)]
    
    pecas_tem = [int(x) for x in input().split()]
    peca_falta = pecas_faltando(pecas_tem, pecas_totais)

    print(peca_falta)
    
def pecas_faltando(colecao, pecas_totais):
    for peca in pecas_totais:
        if peca not in colecao:
            return peca
    return    
main()