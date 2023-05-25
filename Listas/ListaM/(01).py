from str_utils import *
def main():
    frase = input('Digite a frase: ')
    frase = criptografar(frase)
    print(frase)
    
def criptografar(texto:str):
    novo_texto = ""
    for i in range(obter_tamanho(texto)):
        contagem_inversa = obter_tamanho(texto)- 1 - i
        texto_ascii = ord(texto[contagem_inversa])
        if 65 <= texto_ascii <= 90 or 65+32 <= texto_ascii <= 90 + 32:
            if not (texto_ascii == 65 or texto_ascii == 69 or texto_ascii == 73 or texto_ascii == 79 or texto_ascii == 85 or \
                texto_ascii == 65+32 or texto_ascii == 69 + 32 or texto == 73 + 32 or texto_ascii == 79 + 32 or texto_ascii == 85 + 32):
                novo_texto += '#' 
            else:
                novo_texto += texto[contagem_inversa]
        else: 
            novo_texto += texto[contagem_inversa]
            
    return novo_texto
        
main()