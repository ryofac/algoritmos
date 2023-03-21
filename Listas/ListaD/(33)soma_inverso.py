#Entrada: 
numero = str(input("Digite o número e vou retornar a soma dele com seu inverso \n >> "))

#Processamento:
def inverterNum(num):
    num = str(num)
    return num[::-1] # Não consegui pensar de outra forma sem utilizar fatiamento de string em python


inverso = inverterNum(numero)
sum = int(numero) + int(inverso)

# Saída: 
print(f'O resultado: {numero} + {inverso} = {sum}')