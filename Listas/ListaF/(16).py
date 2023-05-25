def main():
    nota1 = int(input('Digite sua primeira nota: '))
    nota2 = int(input('Digite sua segunda nota: '))
    
    media = calcular_media(nota1, nota2)
    
    if media >= 7:
        print('Aprovado!')
    else:
        print('Prova final!')
        nota_exame_final = int(input('Digite a nota final do seu exame: '))
        media_final = calcular_media(media, nota_exame_final)
        if media_final <= 5:
            print('Reprovado!')
        else:
            print('Aprovado!')
    
def calcular_media(num1,num2):
    return (num1 + num2) / 2
main()