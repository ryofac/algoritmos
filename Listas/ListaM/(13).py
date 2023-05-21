from str_utils import quebrar_palavras
def main():
    seu_nome = str(input('Qual o nome que você quer colocar no artigo (qualquer um se o seu for feio): '))
    
    nome_splited = quebrar_palavras(seu_nome)
    
    # letras_primeiro_nome = [letra for letra in nome_splited[0]]
    # letras_segundo_nome = [letra for letra in nome_splited[1]]
    
    # primeira_inicial = letras_primeiro_nome[0]
    # segunda_inicial = letras_segundo_nome[0]
    
    primeira_inicial = nome_splited[0][0]
    segunda_inicial = nome_splited[1][0]
    ultimo_nome = nome_splited[len(nome_splited) - 1]
    
    print(f'Então será: {ultimo_nome}. {primeira_inicial}. {segunda_inicial}')

    
main()