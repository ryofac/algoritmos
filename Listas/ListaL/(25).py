
def main():
    eleitores = int(input('Digite o código de voto: '))

    candidato1 = 0
    candidato2 = 0
    candidato3 = 0
    nulo = 0
    branco = 0

    for i in range(eleitores):
        pedir_votos = int(input('Digite seu voto: '))
        if pedir_votos == 1: 
            candidato1 += 1
        if pedir_votos == 2:
            candidato2 += 1
        if pedir_votos == 3:
            candidato3 += 1
        if pedir_votos == 9:
            nulo += 1
        if pedir_votos == 0:
            branco += 1

        ganhador_eleicao = verificar_ganhador(candidato1, candidato2, candidato3)

    mostrar_resultado(candidato1, candidato2, candidato3, nulo, branco)
    print(ganhador_eleicao)

def mostrar_resultado(candi1, candi2, candi3, nulo, branco):
    print()
    print('VOTOS PARA CADA CANDIDATO')
    print(f'Candidato 1: {candi1}')
    print(f'Candidato 2: {candi2}')
    print(f'Candidato 3: {candi3}')
    print()
    print('SEM VOTOS')
    print(f'Nulo: {nulo}')
    print(f'Branco: {branco}')
    print()

def verificar_ganhador(candi1, candi2, candi3):
    if candi1 > candi2 and candi3:
        return f'Ganhador: Candidato 1'
    if candi2 > candi1 and candi3:
        return f'Ganhador: Candidato 2'
    if candi3 > candi1 and candi2:
        return f'Ganhador: Ganhador 3'
    if candi1 == candi2 == candi3:
        return 'EMPATE'
main()