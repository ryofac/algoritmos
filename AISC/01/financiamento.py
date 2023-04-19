# valor_entrada  = no min 30%
# O valor "do meio" é financiado
# valor_financiamento => no máx 30%
from time import sleep

def main():
    while True:
        fala_jose('Olá, eu sou José, estagiário do banco e vou te ajudar a financiar um veículo!')
        valor_veiculo = float(input('Qual é o valor total do veículo? \n > R$ '))
        if not(check_valor(valor_veiculo)):
            break # Final 1
        renda_comprador = float(input('Quanto você ganha por seu trabalho suado?\n > R$'))
        if not(check_renda(renda_comprador)):
            casar = str(input('...')).upper()
            if casar in "Ss":
                fala_jose('Então vamos casar!')
                game_over('BEST ENDING')
                printslow('Você casou com José e agora são felizes para sempre! :)')
                break # Final 2
        fala_jose('Qual é o tipo de serviço que você presta\n1- Público\n2- Privado\n > ')
        tipo_servico = str(input('> '))
        
def fala_jose(txt):
    printslow('JOSÉ: ' + txt)
def fala_gerente(txt):
    printslow('GERENTE: ' + txt)
    

def check_renda(renda):
    if renda > 15000:
        fala_jose('Você tá solteiro?...')
        fala_gerente('JOSÉ!')
        fala_jose('TA BEM...TA BEM...')
    elif renda > 10000:
        fala_jose('Você dá aula no ifpi?!')
    elif renda < 1000:
        fala_jose('Cara, a gente vai fazer uma promoção bem especial pra vc, a vida já te fudeu demais\n >')
    else:
        fala_jose('OK, vamos continuar...')
        
def check_valor(valor_carro):
    if valor_carro > 10000000:
        fala_jose('CARALHO')
        fala_jose('Posso nem sonhar com esse carro')
        fala_jose('Ok... vamos continuar')
        entrada = float(input(('Pois bem... você vai pagar quanto de entrada nesse carrão?\n >'))) 
        
    elif valor_carro < 10000:
        fala_gerente('Ah, esse...')
        fala_gerente('...é o carro que a gente ia despejar pro ferro velho')
        fala_jose('Esse não é o prêmio do funcionário do mês....?')
        fala_gerente('José! Você está demitido!!')
        game_over('BAD ENDING')
        printslow('José foi demitido e agora está desempregado :/')
        return False              
    else:
        fala_jose('OK, vamos proceguir então...')
        entrada = float(input('Quanto você vai querer dar de entrada?\n >'))
    return entrada

def game_over(txt):
    print('--------------------------')
    print(f'|       {txt}       |')
    print('--------------------------')

    
def printslow(texto): # função para escrever o texto lentamente
    for letra in texto: # loop for: variável letra recebe cada letra em texto
        print(letra, end='', flush=True) # end ='': não quebra a linha e não tem espaço entre as letras
        # flush: Não deixa o buffer renderizar a string toda
        sleep(0.04) # Atraso de 0.04seg entre cada letra
    print('\n')
    
# def check_tipo_servidor(tipo_servidor):
#     if tipo_servidor == 1:
        
#     elif tipo_servidor == 2:
main()