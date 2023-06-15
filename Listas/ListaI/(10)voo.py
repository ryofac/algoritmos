def main():
    
    quantidade_combustivel = obter_inteiro('Digite a quantidade de combustivel da aeronave:')
    
    while quantidade_combustivel < 1000:
        print('A aeronave não pode decolar com menos de 1000l')
        quantidade_combustivel = obter_inteiro('Quanto de combustível é ')

    quantidade_conteiners = obter_inteiro('Digite a quantidade de conteiners: ', tipo = '+')    
    peso_conteiners_total = 0
    contador = 0
    
    while quantidade_conteiners >= 0:
        contador += 1
        peso_conteiner = obter_inteiro(f'Qual é o peso do conteiner {contador}: ', tipo="+")
        quantidade_conteiners -= 1
        peso_conteiners_total += peso_conteiner
    
    
    total_passageiros = 0
    total_bagagens = 0
    
    print('BEM VINDOS AO VOO PASSAGEIROS!')
    while True:
        tiket = obter_inteiro('Qual é o número do seu tiket?: ')
        if tiket == 0: break
        bagagens = obter_inteiro('Quantas bagagens o senhor(a) está carregando?: ')
        total_bagagens += bagagens
        total_passageiros += 1
    
    peso_combustivel = calcular_peso_combustivel(quantidade_combustivel)
    peso_passageiro = calcular_peso_passageiro(total_bagagens, total_passageiros)
    peso_carga = peso_conteiners_total
    
    peso_decolagem = peso_combustivel + peso_passageiro + peso_carga
    
    if peso_decolagem > 500000:
        print('Aeronave não pode decolar!')
        return
    
    print('Aeronave pode decolar!')
    
    print(f'PESO TOTAL AERONAVE: {peso_decolagem}')
      
    
    
    
    
    
def calcular_peso_combustivel(qnt_combustivel):
    return qnt_combustivel * 1.5


def calcular_peso_passageiro(qnt_carga, qnt_pessoas):
    return (qnt_pessoas * 70)  +  (qnt_carga * 10)

    
def obter_inteiro(label= 'Me diga um número inteiro:\n> ', tipo:str = None) -> int:
    if not tipo:
        try:
            num = int(input(label))
        except:
            print('Não é um inteiro!')
            while not num:
                num = int(input(label))
        return num
    if tipo == '+':
        num = int(input(label))
        while not num > 0:
            print('Digite um número positivo!')
            num = int(input(label))
        return num
    if tipo == '-':
        num = int(input(label))
        while not num <= 0:
            print('Digite um número negativo!')
            num = int(input(label))
        return num

    
main()