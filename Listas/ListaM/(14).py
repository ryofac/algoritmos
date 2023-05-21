import str_utils as st
from time import time
iniciais_login = ('amazing','powerful', 'cold', 'potato', 'lolzer')
def main():
    nome = str(input('Digite o seu nome, caro lindo usuário: '))
    
    iniciais = obter_iniciais(nome)
   
    
    print(f'Olá {nome}, o seu nome de usuário será: {randomize(seq = iniciais_login, randomizer= st.obter_tamanho(nome) + int(time()))}-{iniciais}')

def obter_iniciais(nome):
    nome_splited = st.quebrar_palavras(nome)
    iniciais = ''
    for c in range(len(nome_splited)):
         iniciais += st.para_caixa_baixa(nome_splited[c][0:3])
    return iniciais

def randomize(seq, randomizer):
    return seq[randomizer % len(seq)]
    
         
    

    
    
    
main()