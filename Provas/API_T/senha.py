# Proteja a sua senha:
def main():
    senha_final = []
    
    seq_letra = []
    inputs = ['A', 'B', 'C', 'D', 'E']
    
    linha1 = [ x for x in input().split()]
    
    senha = linha1[:10]
    seq = linha1[10:]
    
    
    cont = 0
    relacionando_letra = []
    for num in senha:  
        relacionando_letra.append(num)
        cont += 1
        if cont >= 2:
            seq_letra.append(relacionando_letra)
            relacionando_letra = []
            cont = 0
    
    for letra in seq:
        print(inputs.index(letra))
        senha_final.append(seq_letra[inputs.index(letra)][contar_caractere(seq, letra)-1])
    
    print(senha)
    print(seq)
    print(senha_final)
            
def contar_caractere(lista:list, caractere:str):
    cont_caractere = 0
    for char in lista:
        if caractere == char:
            cont_caractere += 1
    return cont_caractere
    
            
main()