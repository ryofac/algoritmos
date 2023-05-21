from str_utils import contar_palavras

def main():
    texto = str(input('Digite o seu texto aqui: '))
    
    print(f'O total de palavras do texto é {contar_palavras(texto)}')
    
main()