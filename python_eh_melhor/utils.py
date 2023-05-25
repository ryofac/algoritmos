import random
from datetime import date

def gerar_vetor_aleatorio(tamanho):
    vetor = [0] * tamanho

    for i in range(tamanho):
        vetor[i] = obter_numero_aleatorio()

    return vetor

def obter_numero_aleatorio(limite=100):
    return random.randint(0, limite)

def bye():
    frases_legais = ['Obrigado por usar! ', 
                     'Você é incrível, lembre- se disso!', 
                     'Quando você está parando pra pensar, você pensa parado!', 
                     'Quem ganha dinheiro deitado é testador de cama',
                     'Tchau BB! ',
                     'Não olhe para trás!',
                     'Python > JS',
                     f'Hoje são {date.today()}',
                     'Beba bastante... água!'] 

    index = random.randint(0, len(frases_legais) - 1)

    print('Lembrete diário: ' + frases_legais[index])

def obter_posicoes_em_vetor(vetor, valor):
    posicoes = []
    for i in range(len(vetor)):
        if vetor[i] == valor:
            posicoes.append(i)

    return posicoes

