from str_utils import quebrar_palavras
def main():
    seu_nome = str(input('Digite qual o seu nome, senhor: '))
    
    nome_splited = quebrar_palavras(seu_nome)
    
    primeiro_nome = nome_splited[0]
    
    ultimo_nome = nome_splited[len(nome_splited) - 1]
    
    print(f'Olá {ultimo_nome}/{primeiro_nome} seu acento será o 42')
    
main()