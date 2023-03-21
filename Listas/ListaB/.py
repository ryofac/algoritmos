# Arquivo que é usado como treinamento nas aulas: 
def main():
    # SEPARAR OS GRANDES PASSOS
    # MODULARIZAR OS >>"""""DETALHES"""""<<
    
    # Entrada
    peso = float(input('Qual é o seu peso(kg)\n >> '))
    reduzir = int(input('Quanto você quer perder?(%)\n >> '))
    tempo = int(input('Em quantas semanas? \n >> '))
    consumo_diario = int(input('Quanto você quer consumir por dia? \n >> '))
     
     # Processamento
    reducao_peso = calcPesoReduzir(peso, tempo, reduzir)
    gasto_diario = consumo_diario + reducao_peso
   
    # Saída
    print(f'Você deve deixar de consumir (total) {gasto_diario:.2f} kcal por dia')


def calcPesoReduzir(peso, tempo, reduzir):
    tempo_dias = tempo * 7 # Transforma o tempo em semanas
    peso_kcal = peso * 7700 # Transforma o peso(kg) para kcal
    reduzir = peso_kcal * (reduzir/100) # Calcula da quantidade em kcal, a porcentagem a ser reduxida
    return reduzir / tempo_dias # Efetivamente calcula a redução por dia em kcal

main()
