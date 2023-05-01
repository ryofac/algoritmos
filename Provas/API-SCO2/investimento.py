# Mariana decidiu investir:
# o valor não pode ser mais de 30% do seu salário
# Taxa de juros 0.01 - 1 % ao mês ( juros compostos )
# Preciso de um objetivo!
# Pedir a porcentagem do salário ( melhorar essa função )
# Retornar em anos e meses ( caso meses > 12 )

from io_utils import * 
from math_utils import *
from random import choice


def main():
    
    clear_screen()
    title(centralize('Meu porquinho'), upper= True)
    
    printcenter('Qual é o seu nome?')
    nome = str(input(('\t\t>> ')))
    
    printcenter(randomize_nome())
    
    printcenter('Quanto você costuma ganhar por mês? ')
    salario = pedir_float('\t\t>> R$', tipo="+")
    
    printcenter('Qual a porcentagem que você quer investir do seu salário? ')
    printcenter('(máximo de 30%)')
    investimento_percentual = pedir_float('\t\t>> ', tipo="+")
    
    while not faixa_normal_parcela(investimento_percentual):
        printcenter('Valor Inválido!')
        investimento_percentual = pedir_float('\t\t>> ', tipo="+")
        
    printcenter('A qual taxa??')
    printcenter('(min de 0.1, máx de 1%)')
    taxa = pedir_float('\t\t>> ') / 100
    
    while not faixa_normal_taxa(taxa):
        printcenter('Valor Inválido!')
        taxa = pedir_float('\t\t>> ') / 100
    
        
    valor_investido = porcentagem_de(investimento_percentual) * salario
    valor_inicial = valor_investido
    printcenter(f'Então você escolheu investir R${valor_investido}, lhe sobrando R${salario - valor_investido} por mês')
    clear_screen()
    printcenter('O que você quer fazer com esse investimento? ')
    objetivo = str(input('\t\t>> '))
    printcenter('Quanto você precisa para realizar esse investimento, Mariana?')
    dinheiro_alvo = pedir_inteiro('\t\t>> ', tipo="+")
    contador_meses = 0
    
    tempo = 'agora mesmo!' # Default
    
    
    while valor_investido <= dinheiro_alvo:
        clear_screen()
        printcenter(f'------ {objetivo} ------'.upper())
        printcenter(f'VALOR INICIAL: R${valor_inicial}')
        printcenter(f'OBJETIVO: R${dinheiro_alvo}')
        printcenter(f'TAXA: {taxa * 100} % a.m\r')
        printcenter(f' Dinheiro rendendo: R${valor_investido:.2f}\r ')
        printcenter(barra_loading(valor_investido, dinheiro_alvo))
        tempo = mostrar_tempo(contador_meses)
        printcenter(tempo)
        juros = valor_investido * taxa
        printcenter(f'JUROS: R${juros:.2f}')
        valor_investido = valor_investido + juros
        contador_meses += 1
        sleep(0.05)
    clear_screen()
    resultados(nome, valor_inicial, valor_investido, contador_meses, objetivo, dinheiro_alvo)
    
    

def resultados(nome_cliente, valor_inicial, dinheiro_final, contador_meses, objetivo, valor_objetivo):
    tempo = mostrar_tempo(contador_meses)
    title(centralize('Resultados:'))
    printcenter(f'Cliente: {nome_cliente[:2]}... ops Mariana!')
    printcenter(f'Valor investido inicial: R${valor_inicial:.2f}')
    printcenter(f'Você teria R${dinheiro_final:.2f} ao final, restando R${dinheiro_final - valor_objetivo:.2f}')
    printcenter(f'Você conseguiria {objetivo} em {tempo}')
    
def mostrar_tempo(meses):
    if meses < 12:
        return f'{meses} meses'
    else:
        anos = meses // 12
        meses = meses % 12
        return f'{anos} anos e {meses} meses'
    
def randomize_nome():
    frases = ['Ah lembrei, seu nome é Mariana ', 'Ok então é Mariana, certo?', 'Olá de novo, Mariana!']
    return choice(frases)

# Check Functions:
def faixa_normal_taxa(percentual):
    return 0.001 <= percentual <= 0.01
def faixa_normal_parcela(porcentagem_parcela):
    return 1 <= porcentagem_parcela <= 30
    


main()