from str_utils import *
def main():
    verbo_er = str(input('Digite um verbo na segunda conjugação (er): '))
    conjugar(verbo_er)
    
    

def conjugar(verbo) -> None:
    radical = ''
    pessoas = ('Eu', 'Tu', 'Ele/Ela', 'Nós', 'Vós', 'Eles/Elas')
    terminacoes = ('o', 'es', 'e', 'emos', 'eis', 'em')
    for i in range(obter_tamanho(verbo) - 2):
       radical += verbo[i]
    
    for i in range(len(pessoas)):
        print(f'{pessoas[i]}: {radical + terminacoes[i]}')
       

    
    

        
   
main()