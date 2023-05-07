def main():
    # Entrada 
    valor_total = float(input())
    quantidade_notas= divisoes_sucessivas(100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.10, 0.05, 0.01, total= valor_total)


    # Saída

    print('NOTAS:')
    print(f'{quantidade_notas[100]} nota(s) de R$ 100.00')
    print(f'{quantidade_notas[50]} nota(s) de R$ 50.00')
    print(f'{quantidade_notas[20]} nota(s) de R$ 20.00')
    print(f'{quantidade_notas[10]} nota(s) de R$ 10.00')
    print(f'{quantidade_notas[5]} nota(s) de R$ 5.00')
    print(f'{quantidade_notas[2]} nota(s) de R$ 2.00')
    print('MOEDAS:')
    print(f'{quantidade_notas[1]} moeda(s) de R$ 1.00')
    print(f'{quantidade_notas[0.5]} moeda(s) de R$ 0.50')
    print(f'{quantidade_notas[0.25]} moeda(s) de R$ 0.25')
    print(f'{quantidade_notas[0.10]} moeda(s) de R$ 0.10')
    print(f'{quantidade_notas[0.05]} moeda(s) de R$ 0.05')
    print(f'{quantidade_notas[0.01]} moeda(s) de R$ 0.01')

    
# Funcao que calcula a quantidade de notas para cada valor dado e armazena em um dicionario
def divisoes_sucessivas(*notas, total):
    notas_quantidade = {1:1}

    for nota in notas:
        nota = round(nota, 2)
        quantidade_notas = total // nota
        notas_quantidade[nota] = int(quantidade_notas)
        total = total - (nota * quantidade_notas)
        total = round(total, 2)
    if total == 0.01:
        notas_quantidade[0.01] += 1
        
    return notas_quantidade
        
main() 