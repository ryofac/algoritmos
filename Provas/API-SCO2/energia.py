from io_utils import *
from math_utils import *
    
# Exemplo: 
# Consumo 000 KWh
# Valor Faturado R$ 0,00
# Bandeira R$ 0,00 (x bandeiras)
# ICMS R$ 0,00
# PIS/CONFIS
# Taxa Iluminação R$ 0,00
# A cada 100KWh -> + R$ 8
# Até 30KWh -> isento
# Até 100KWh -> + R$0.59
# acima de 100 KWH -> + R$0.75 de cada KWh
# sobre o atrifado é aplicado 25% de ICMS e 15% de PIS/CONFIS
# Taxa de iluminação: Acima de 80KWh


def main():
    clear_screen()
    printcenter('-- EquatoriMAL energia -- '.upper())
    printcenter('Cálculo de Tarifa')
    consumo_anterior = pedir_inteiro('LEITURA ANTERIOR (KWH): \n >> ')
    consumo_atual = pedir_inteiro('LEITURA ATUAL (KWH): \n >> ')
    while consumo_anterior > consumo_atual:
        printcenter('Tente fazer a leitura novamente! (Err: Anterior maior que atual)')
        consumo_anterior = pedir_inteiro('LEITURA ANTERIOR: \n >> ')
        consumo_atual = pedir_inteiro('LEITURA ATUAL:\n >> ')
    consumo = consumo_atual - consumo_anterior
    tarifa = calcular_tarifa(consumo)
    bandeira = calcular_bandeira(consumo)
    icms = calcular_ICMS(tarifa)
    pis = calcular_PIS(tarifa)
    taxa_iluminacao = calcular_taxa_iluminacao(consumo)
    resultado(consumo, tarifa, bandeira, icms, pis, taxa_iluminacao)
    
    
    
    

def resultado(consumo, tarifa, bandeira, icms, pis, taxa_ilum):
    printcenter('=' * 30)
    printcenter('EquatoriMAL')
    printcenter('=' * 30)
    printcenter(f'Consumo: {consumo:.2f} KWh')
    printcenter(f'Valor Faturado R${tarifa:.2f}')
    printcenter(f'Bandeira R${bandeira:.2f} => R$8.00 x {consumo // 100}')
    printcenter(f'ICMS R${icms:.2f}')
    printcenter(f'PIS/CONFIS R${pis:.2f}')
    printcenter(f'Taxa Iluminação R$ {taxa_ilum:.2f}')
    printcenter('=' * 30)
    printcenter(f'VALOR TOTAL: R${tarifa + bandeira + icms + pis + taxa_ilum:.2f}')
    printcenter('=' * 30)
    printcenter(f'PAGAMENTO(PIX): 86995638334')
    printcenter('=' * 30)
    
def calcular_tarifa(consumo):
    if consumo <= 30:
        return 0
    elif consumo <= 100:
        return 0.59 * consumo
    else:
        return 0.75 * consumo

def calcular_bandeira(consumo):
    valor_bandeira = 8
    if consumo < 100:
        return 0
    return (consumo // 100) * valor_bandeira
    
    
    
def calcular_ICMS(consumo):
    return consumo * porcentagem_de(25)
    
def calcular_PIS(consumo):
    return consumo * porcentagem_de(15)
    
def calcular_taxa_iluminacao(consumo):
    if consumo <= 80:
        return 0
    return consumo * porcentagem_de(6)

main()