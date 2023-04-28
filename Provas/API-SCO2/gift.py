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
    
    
    while True:
        clear_screen()
        label = '    Loja Jalo     '
        title(label.center(screen_size, '-'), upper=True)
        printslow('Aqui a gente vende !(caro)'.center(screen_size), speed= 0.01)
        printslow('> Olá, qual é o seu nome? ')
        nome_cliente = str(input(' >> '))
        
        if nome_cliente == 'admin': # Flag (Condição de Continuidade)
            clear_screen()
            title('Loja Fechada'.center(screen_size), upper=True)
            break
        
        quantidade_clientes += 1
        
        printslow(f'\n> Olá {nome_cliente}!, que !(ruim) te ver por aqui hoje!')
        num_compras = pedir_inteiro('> Digite o total de compras no carrinho\n >> ', tipo="+")
        
        while muita_compra(num_compras):
            printslow('> Desculpe, !(aceitamos) compras por pessoa física com mais de 10 produtos!')
            num_compras = pedir_inteiro('> Digite um número válido  de compras\n >> ', tipo="+")
        
        # Inicializando Contadores Locais!
        compra_atual = 0
        valor_compra_total = 0
        valor_cashback_total = 0
        
        while compra_atual < num_compras:
            clear_screen()
            compra_atual += 1
            title(f'({compra_atual})/({num_compras})')
            valor_compra_atual = pedir_float('> Digite o valor do seu pedido: R$', tipo='+')
            cashback = calcularCashback(valor_compra_atual)
            valor_compra_total += valor_compra_atual
            valor_cashback_total += cashback
            valor_cashback_clientes += cashback # soma os cashbacks de todos e armazena 
            valor_compras_total += valor_compra_atual # Soma a quantidade de compras totais no dia
            
    
        clear_screen()
        mostrarViaCliente(nome_cliente, num_compras, valor_compra_total, valor_cashback_total)
        input('Próximo!...<Enter>')
        clear_screen()
    
    # Fim do loop!
    mostrarFaturamento(quantidade_clientes, valor_compras_total, valor_cashback_clientes)


def calcularCashback(valor_compra_atual):
    if valor_compra_atual <= 250:
        return valor_compra_atual * porcentagem_de(5)
    elif valor_compra_atual <= 500:
        return valor_compra_atual * porcentagem_de(7)
    elif valor_compra_atual <= 750:
        return valor_compra_atual * porcentagem_de(8)
    else:
        valor_excedente = valor_compra_atual - 750
        return (valor_compra_atual * porcentagem_de(8)) + (valor_excedente * porcentagem_de(25))
    
    
def mostrarViaCliente(nome, num_compras, valor_compras, valor_cashback):
    title('Via do Cliente'.center(screen_size), upper= True)
    print(f'CLIENTE: {nome}\n'.center(screen_size))
    gerar_recomendação(valor_cashback + valor_compras + num_compras + len(nome))
    print(f'QUANTIDADE TOTAL DE PEDIDOS: {num_compras}'.center(screen_size))
    print(f'VALOR PEDIDOS: R${valor_compras:.2f}'.center(screen_size))
    print(f' >> VALOR CASHBACK: R${valor_cashback:.2f}'.center(screen_size))
    title(f'VALOR TOTAL (com "descontos" ): R${valor_compras - valor_cashback:.2f}'.center(screen_size), estrelado= True)
    

def mostrarFaturamento(qnt_clientes, total_de_compras, total_cashback):
    print(f'QUANTIDADE TOTAL DE CLIENTES HOJE: {qnt_clientes}'.center(screen_size))
    print(f'>> VALOR TOTAL DE COMPRAS: R${total_de_compras:.2f}'.center(screen_size))
    print(f'>> VALOR TOTAL DE CASHBACKS: R${total_cashback:.2f}'.center(screen_size))
    title(f'FATURAMENTO FINAL: R${total_de_compras - total_cashback:.2f}'.center(screen_size),estrelado= True )


def gerar_recomendação(randomidade):
    recomendacoes = ['Muito obrigado por comprar na nossa loja!', 
                     'Você sabia que no cartão jalo você pode !(perder) mais de 20% das compras como cashback??',
                     'Volte Sempre!', 'Obrigado pela Preferência', 'Jalo, o !(pior) para você!', 'Você é o nosso número 0!']
    printslow(recomendacoes[int(randomidade % 6)].center(screen_size), speed=0.01)
        

# Funções de checagem:
def muita_compra(compras):
    return compras > 10



    
main()