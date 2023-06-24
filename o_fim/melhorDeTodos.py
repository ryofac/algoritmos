from features import *

def main():
    opcoes = {
        'RUNNING': True,
        'OBTER_NOME': 1,
        'VER_PESSOAS': 2,
        'ADCIONAR_ADJETIVO': 3,
        'LIMPAR_DADOS': 4,
        'SAIR': 0
    }
    # Inicializando Objetos
    adjetivos = abrir_arquivo("./data/adjetivos.txt")
    pessoas = abrir_arquivo("./data/pessoas.txt", 'pessoa')
    
    menu = gerar_menu('Digitar seu nome', 
                      'Ver nomes já presentes',
                      'Gerar novo adjetivo',
                      'Limpar dados',
                      title='Digite sua opção!', center=True)
    
    while opcoes['RUNNING']:
        clear_screen()
        
        choice = obter_numero_intervalo(menu, 10, 0)
        
        if (choice == opcoes['OBTER_NOME']):
            pessoa_gerada = obter_pessoa(adjetivos)
            if pessoa_gerada:
                pessoas.append(pessoa_gerada)
                print(f'Olá {pessoa_gerada["nome"]} !')
    
        if (choice == opcoes['VER_PESSOAS']):
             mostrar_pessoas(pessoas)
             
        if (choice == opcoes['ADCIONAR_ADJETIVO']):
            gerar_novo_adjetivo(adjetivos)
            
        if (choice == opcoes['LIMPAR_DADOS']):
            pessoas = []
           
        if choice == opcoes['SAIR']:
            opcoes['RUNNING'] = False
        enter_to_continue()
    
    # Barra de Loading
    const = obter_numero_aleatorio_entre(1, 20)
    while (const <= 100):
        printcenter(barra_porcentagem(const, 100))
        const += 1
        sleep(0.01)
        clear_screen()
        
    write_in_file(file="./data/adjetivos.txt", content=adjetivos)
    write_in_file(file="./data/pessoas.txt", content=pessoas, tipo='pessoas')
    
    bye('./data/bye.txt')
main()
