def main():
    alcool_preco, gasolina_preco, rendimento_alcool, rendimento_gasolina = [float(x) for x in input().split()]

    rodando_gasolina_preco = calcular_desempenho(gasolina_preco, rendimento_gasolina)
    rodando_alcool_preco = calcular_desempenho(alcool_preco, rendimento_alcool)
    
    if rodando_alcool_preco == rodando_gasolina_preco:
        print('G')
        return
    print('G') if rodando_gasolina_preco < rodando_alcool_preco else print('A')

def calcular_desempenho(combs, redm_combs):
    return combs / redm_combs
main()