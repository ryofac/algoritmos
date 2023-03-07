#Entrada: 
numero = str(input("Digite o número que você quer saber o inverso \n >> "))

#Processamento:
def inverterNum(num):
    num = str(num)
    return num[::-1]

# Saída: 
print(f'O inverso do número {numero} é {inverterNum(numero)}')