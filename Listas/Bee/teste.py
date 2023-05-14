def main():
    n1, n2, n3, n4 = map(float, input().split())
    
    media = calcular_media_ponderada(n1,n2,n3,n4, pesos = (2,3,4,1))
    resultado_aluno = checar_situacao(media)
    
    if not resultado_aluno == 'Aluno em exame.':
        print(f'Media: {media:.1f}')
        print(resultado_aluno)
        return
    
    exame = float(input())
    print(f'Media: {media}')
    print(resultado_aluno)
    media_exame = media + exame / 2 
    print(f'Media Final: {media_exame:.1f}')
    print(checar_situacao_exame(media_exame))
        

def calcular_media_ponderada(*valores, pesos):
    quociente = 0
    soma_pesos = 0
    for c in range(len(valores)):
        quociente += valores[c] * pesos[c]
          
    for valor in pesos:
        soma_pesos += valor
    
    return quociente / soma_pesos


def checar_situacao(media):
    if media <= 5.0:
        return 'Aluno reprovado.'
    elif media <= 6.9:
        return 'Aluno em exame.'
    else:
        return 'Aluno aprovado.'
    
def checar_situacao_exame(media):
    if media >= 5.0:
        return 'Aluno aprovado.'
    else:
        return 'Aluno reprovado.'
main()
