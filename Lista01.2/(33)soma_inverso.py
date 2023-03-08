#Entrada: 
numero = str(input("Digite o número e vou retornar a soma dele com seu inverso \n >> "))

#Processamento:
def inverterNum(num):
    num = str(num)
    return num[::-1]


inverso = inverterNum(numero)
sum = int(numero) + int(inverso)

# Saída: 
print(f'O resultado: {numero} + {inverso} = {sum}')