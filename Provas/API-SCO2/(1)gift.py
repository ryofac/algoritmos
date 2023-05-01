from io_utils import *
from math_utils import *
from os import get_terminal_size

screen_size = get_terminal_size().columns - 2 # Obter tamanho do terminal

# A FLAG É NOME_CLIENTE = ADMIN
def main():
    # Inicializando Contadores Globais!
    quantidade_clientes = 0
    valor_compras_total = 0
    valor_cashback_clientes = 0
    quantidade_compras_totais = 0
    maior_cash = float('-inf')
    menor_cash = float('inf')    
    
    while True:
        clear_screen()
        label = '    Loja Jalo     '
        title(label.center(screen_size, '-'), upper=True)
        printslow('Aqui a gente vende !(caro)'.center(screen_size), speed= 0.01)
        printslow('> Olá, qual é o seu nome? ')
        nome_cliente = str(input(' >> '))
        
        if nome_cliente.lower().strip()== 'admin': # Flag (Condição de Continuidade)
            clear_screen()
            title('Loja Fechada'.center(screen_size), upper=True)
            break
        
        quantidade_clientes += 1
        
        printslow(f'\n> Olá {nome_cliente}!, que !(ruim) te ver por aqui hoje!')
        num_compras = pedir_inteiro('> Digite o total de compras no carrinho\n >> ', tipo="+")
        while muita_compra(num_compras):
            printslow('> Desculpe, !(aceitamos) compras por pessoa física com mais de 10 produtos!')
            num_compras = pedir_inteiro('> Digite um número válido de compras\n >> ', tipo="+")
        
        quantidade_compras_totais += num_compras
        
        # Inicializando Contadores Locais!
        compra_atual = 0
        valor_compra_total = 0
        valor_cashback_total = 0
        
        while compra_atual < num_compras:
            clear_screen()
            compra_atual += 1
            printcenter(f'-- ({compra_atual})/({num_compras}) -- ')
            valor_compra_atual = pedir_float('> Digite o valor do seu pedido: R$', tipo='+')
            cashback = calcularCashback(valor_compra_atual)
            valor_compra_total += valor_compra_atual
            valor_cashback_total += cashback
            valor_cashback_clientes += cashback # soma os cashbacks de todos e armazena 
            valor_compras_total += valor_compra_atual # Soma a quantidade de compras totais no dia
            
        # Checagem do maior_menor:
        print(f'CASHBACK TOTAL: {valor_cashback_total}')
        if valor_cashback_total > maior_cash:
            maior_cash = valor_cashback_total
        if valor_cashback_total < menor_cash:
            menor_cash = valor_cashback_total 
            
        clear_screen()
        mostrarViaCliente(nome_cliente, num_compras, valor_compra_total, valor_cashback_total)
        input('Próximo!...<Enter>')
        clear_screen()
        
    if nome_cliente == 'admin' and quantidade_compras_totais > 0:
        # Fim do loop!
        media_cashback = calcular_media(valor_cashback_total,  num_compras)
        mostrarFaturamento(quantidade_clientes,quantidade_compras_totais, valor_compras_total, valor_cashback_clientes, media_cashback, maior_cash, menor_cash)
    else:
        printcenter('-- SEM COMPRAS COMPUTADAS --')


def calcularCashback(valor_compra_atual):
    if valor_compra_atual <= 250:
        return valor_compra_atual * porcentagem_de(5)
    elif valor_compra_atual <= 500:
        return (valor_compra_atual - 250) * porcentagem_de(7) + 250 * porcentagem_de(5)
    elif valor_compra_atual <= 750:
        return (valor_compra_atual - 500 )+ 250 * porcentagem_de(8) + 250 * porcentagem_de(5)
    else:
        return (valor_compra_atual - 750)+ 250 * porcentagem_de(8) + 250 * porcentagem_de(7) + 250 * porcentagem_de(5)
    
def mostrarViaCliente(nome, num_compras, valor_compras, valor_cashback):
    title('Via do Cliente'.center(screen_size), upper= True)
    print(f'CLIENTE: {nome}\n'.center(screen_size))
    gerar_recomendação(valor_cashback + valor_compras + num_compras + len(nome))
    print(f'QUANTIDADE TOTAL DE PEDIDOS: {num_compras}'.center(screen_size))
    print(f'VALOR PEDIDOS: R${valor_compras:.2f}'.center(screen_size))
    title(f' >> VALOR CASHBACK: R${valor_cashback:.2f}'.center(screen_size), estrelado= True)
    

def mostrarFaturamento(qnt_clientes, qnt_compras, total_de_compras, total_cashback, media_cash, maior_cash, menor_cash):
    print(f'QUANTIDADE TOTAL DE CLIENTES HOJE: {qnt_clientes}'.center(screen_size))
    print(f'QUANTIDADE TOTAL DE COMPRAS HOJE: {qnt_compras}'.center(screen_size))
    print(f'>> VALOR TOTAL DE COMPRAS: R${total_de_compras:.2f}\n'.center(screen_size))
    print(f'>> VALOR TOTAL DE CASHBACKS: R${total_cashback:.2f}\n'.center(screen_size))
    print(f'\t>> VALOR MÉDIO: R${media_cash:.2f}'.center(screen_size))
    print(f'\t>> MAIOR VALOR: R${maior_cash:.2f}'.center(screen_size))
    print(f'\t>> MENOR VALOR: R${menor_cash:.2f}'.center(screen_size))
    title(f'FATURAMENTO FINAL: R${total_de_compras:.2f} => {calcular_porcento_do_valor(total_cashback, total_de_compras):.2f}% de CASHBACK'.center(screen_size),estrelado= True )

def calcular_porcento_do_valor(valor, total):
    return (valor / total) * 100

def calcular_media(somatorio, total):
    return somatorio / total


def gerar_recomendação(randomidade):
    recomendacoes = ['Muito obrigado por comprar na nossa loja!', 
                     'Você sabia que no cartão jalo você pode !(perder) mais de 20% das compras como cashback??',
                     'Volte Sempre!', 'Obrigado pela Preferência', 'Jalo, o !(pior) para você!', 'Você é o nosso número 0!']
    printslow(recomendacoes[int(randomidade % 6)].center(screen_size), speed=0.01)
        

# Funções de checagem:
def muita_compra(compras):
    return compras > 10



    
main()