def main():
    n1, n2, n3, n4 = map(float, input().split())
    
    # pesos = 2, 3, 4 e 1
    media = calcular_media_ponderada(valores = [n1, n2, n3, n4], pesos = [2,3,4,1])
    if media >= 7:
        print('Aluno aprovado.')
        print(f'Media: {media:.1f}')

    elif media >= 5:
        nota_exame = float(input())
        media_exame = calcular_media(nota_exame, media)
        print('Aluno em exame.')
        print(f'Media: {media:.1f}')
        if media_exame >= 5:
            media 
            print('Aluno aprovado.')
            print(f'Media final: {media_exame:.1f}')
            return
        print('Aluno reprovado.')
        print(f'Media final: {media_exame:.1f}')
        return
    else:
        print('Aluno reprovado.')
        print(f'Media: {media:.1f}')
      
def calcular_media(*valores : list[float]) -> float:
    soma = 0
    quantidade = 0
    for item in valores:
        soma += item
        quantidade += 1
    return soma / quantidade


def calcular_media_ponderada(valores: list[float], pesos: list[int]) -> float:
    quociente = 0
    soma_pesos = 0
    for valor in valores:
        for peso in pesos:
            quociente += peso * valor
            soma_pesos += peso
    return quociente / soma_pesos
    
main()