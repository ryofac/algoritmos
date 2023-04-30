from io_utils import pedir_inteiro, printslow, title
def main():
    #Entrada
    print('='*10, 'simulador de cashback'.upper(), '='*10)
    
    # Variáveis globais
    cont_clientes = 0
    valor_total_compras = 0
    valor_total_cashback = 0
    valor_maior = float('-inf')
    valor_menor = float('inf')
    
    num_cliente = pedir_inteiro('Digite o número de clientes de hoje:', tipo="+")
    while cont_clientes < num_cliente:
        cont_clientes += 1
        nome_cliente = input('Digite seu nome: ')
        numero_compras = float(input('Digite o número de compras: '))
        while numero_compras > 10:
            printslow('Valor inválido!')
            numero_compras = float(input('Digite o número de compras: '))
        
        # Variáveis para cada cliente
        total_cashback = 0
        contador_compra = 0
    
        
        while contador_compra < numero_compras:
            
            contador_compra += 1
            valor_compras = float(input('Digite o valor das suas compras: '))
            calculo_cashback = calcular_cashback(valor_compras)
            
            total_cashback += calculo_cashback 
            valor_total_compras += valor_compras
            
        valor_total_cashback += total_cashback
        
        if total_cashback > valor_maior:
                valor_maior = total_cashback
        if total_cashback < valor_menor:
            valor_menor = total_cashback
    
    
        #Saída
        label = f'CLIENTE: {nome_cliente}'
        print('=' * len(label))
        print(label)
        print('>', total_cashback, 'de cashback')
        print('=' * len(label))
    
    media_cashback = calcular_media(valor_total_cashback, num_cliente)
    mostrarFaturamento(valor_total_compras, valor_total_cashback, valor_maior, valor_menor, media_cashback)
    

def calcular_media(somatorio, quantidade):
    return somatorio / quantidade
    
def calcular_cashback(valor):
    if valor <= 250:
        return (valor * 5/100)
    elif valor <= 500:
        return (valor * 7/100)
    elif valor <= 750:
        return (valor * 8/100)
    else:
        return ((valor - 750) * 0.25 + 750 *0.08)

def mostrarFaturamento(valor_compras, valor_cashback, maior, menor, media_cash):
    print(f'O Valor total de compras hoje foi de: R${valor_compras:.2f}')
    print(f'O maior valor de cashback por compra hoje foi: R${maior} ')
    print(f'O menor valor de cashback por compra hoje foi: R${menor}')
    print(f'A média de cashbacks foi de R${media_cash:.2f}')
    print(f'O total de cashbacks concedidos foi de R${valor_cashback:.2f} ')
    print(f'O valor perecentual dos cashbacks sobre o faturamento é de {(valor_cashback / valor_compras) * 100:.2f}')
    title(f'O faturamento total foi de : R${valor_compras:.2f}')

    
main()