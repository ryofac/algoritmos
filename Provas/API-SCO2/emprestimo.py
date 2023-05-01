from math_utils import *
from io_utils import *

selicAtual = porcentagem_de(13.75)
tamanho_tela = obter_tamanho_tela() - 2

def main():
    
    title(' --  Banco VestidoBank -- '.center(tamanho_tela))
    renda_mensal = pedir_float('Qual a sua renda mensal?\n > R$', tipo= "+")
    valor_emprestimo = pedir_float('Qual é o valor total do seu empréstimo? \n >> R$')
    prazo = pedir_inteiro('Me diga o prazo (em meses): \n>> ')
    taxa = calcularTaxa(prazo, selicAtual)
    montante = calcularJurosCompostos(valor_emprestimo, taxa, prazo)
    juros = montante - valor_emprestimo
    iof = calcularIOF(valor_emprestimo, meses_dias(prazo))
    valor_final = montante + iof
    
    while not quantidade_parcela_ok(prazo):
        prazo = pedir_inteiro(f'O Prazo inválido: \n>> ')
    
    # Calcular o valor da parcela
    valor_parcela = valor_final / prazo
    
    while not parcela_aprovada(valor_parcela, renda_mensal):
        print('Seu empréstimo não foi aprovado devido a sua renda! ')
        renda_mensal = pedir_inteiro('Digite novamente sua renda\n >> R$', tipo='+')
        
    gerar_relatorio_final(renda_mensal, valor_emprestimo, iof, juros, valor_final, valor_parcela, meses_dias(prazo))

    


def gerar_relatorio_final(renda, valor_pedido, rogerio_feioso, juros, valor_total, parcela_mensal, tempo_dias):
    label = 'Simulação do Empréstimo'
    title(label.center(tamanho_tela, '-'), upper= True)
    print(f'O valor do empréstimo:   R${valor_pedido:.2f}'.center(tamanho_tela))
    print(f'O valor IOF:             R${rogerio_feioso:.2f}'.center(tamanho_tela))
    print(f' >> IOF por dia:             R${rogerio_feioso/tempo_dias:.2f}'.center(tamanho_tela))
    print(f'Juros:                   R${juros:.2f}'.center(tamanho_tela))
    print()
    print(f'Valor a pagar:           R${valor_total:.2f}'.center(tamanho_tela))
    print(f'Parcela mensal:          R${parcela_mensal:.2f} x {tempo_dias//30}'.center(tamanho_tela))
    print(f'                           >> {(parcela_mensal / renda) * 100:.2f}% do salário atual'.center(tamanho_tela))

    print('=' * len(label.center(tamanho_tela)))
    
def calcularTaxa(prazo, selic):
    if prazo <= 6:
        return selic * porcentagem_de(50)
    elif prazo <= 12:
        return selic * porcentagem_de(75)
    elif prazo <= 18:
        return selic
    elif prazo > 18:
        return selic * porcentagem_de(130)

#    O IOF é calculado da seguinte forma: 0,38% sobre valor total (independente do prazo) + 
#    0,0082% por cada dia do prazo do empréstimo.

def calcularIOF(valor_total, prazo_dias):
    valor_fixo = porcentagem_de(0.38) * valor_total
    valor_por_dia = porcentagem_de(0.0082) * valor_total
    return valor_fixo + (valor_por_dia * prazo_dias)

# Check Functions:
def quantidade_parcela_ok(prazo):
    return 2 <= prazo <= 24

def emprestimo_aprovado(emprestimo, renda_mensal):
    return emprestimo == renda_mensal

def parcela_aprovada(valor_parcela, renda_mensal): 
    return valor_parcela <= porcentagem_de(40) * renda_mensal



main()