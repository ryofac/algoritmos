from io_utils import *
def main():
    while True:
        clear_screen()
        maior_pontuacao = float('-inf')
        soma_clube_a = 0
        soma_clube_b = 0
        
        printcenter('>- COMPETIÇÃO NOVA -<')
        numProva = obter_inteiro("Qual é o número da prova? \n> ")
        numCompetidores = obter_inteiro("Digite a quantidade de competidores: \n> ")
        
        if numProva == 0 and numCompetidores == 0:
            break
        
        competidorAtual = 1
        while competidorAtual <= numCompetidores:
            clear_screen()
            printcenter(f'--({competidorAtual}) / ({numCompetidores})--')
            compedidor = obter_texto('Qual o nome do competidor? \n> ')
            clube = obter_texto_max('Qual é o clube que você participa? (A OU B) \n > ', 1).strip().lower()
            classificacao = obter_inteiro('Qual sua classificação? \n> ')
            
            
            # Somando clubes
            if clube == 'a':
                soma_clube_a +=1
            if clube == 'b':
                soma_clube_b += 1
            
            competidorAtual += 1
           
    
        if soma_clube_a > maior_pontuacao:  
            maior_pontuacao == soma_clube_a
        
        printcenter('\t--CLASSIFICAÇÃO PARCIAL--')
        printcenter(f'Clube A:  {soma_clube_a}' + '*' if soma_clube_a > soma_clube_b else '')
        printcenter(f'Clube B:  {soma_clube_a}' + '*' if soma_clube_b > soma_clube_a else '')
        input('<Enter>...')
    
           
    print('--> O clube que ganhou foi o:', 'A' if soma_clube_a > soma_clube_b else 'B', '<--')
    

        
main()