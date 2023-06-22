from utils.io_utils import obter_numero_intervalo
from features import *

# Carregamento de arquivos
pessoas_file = open("./data/pessoas.txt")
menu_file = open("./data/menu.txt")

# Arquivos -> Listas
options = menu_file.readlines()
pessoas = pessoas_file.readlines()
pessoas = mapear(pessoas, lambda x: x.strip())

# Arquivo de dados
data_default = {
        'pessoas' : pessoas,
        'valor_ponto': 0,
        'quantidade_premios': 0,
        'max_premios': 0,
        'taxa_adm' : 0,
        'pontos_sorteados' : [],
        'pontos_disponiveis' : obter_pontos_disponiveis(pessoas),
        'pontos_comprados' : obter_pontos_comprados(pessoas)
    }


def main():
    data = data_default.copy()
    while True:
        checar_valores_nulos(data)
        clear_screen()
        opcao = obter_numero_intervalo(menu(options), 10, 0)
        
        if opcao == 0:
            print('Tchau coração! ')
            break
        if opcao == 1:
            obter_numero_de_pontos(data)
            
        if opcao == 2:
            numero_cada_pessoa_posicao(data)
        
        if opcao == 3:
            data['valor_ponto'] = 0
        
        if opcao == 4:
            obter_visao_geral(data)
        
        if opcao == 5:
            for i in range(100):
                print('Resetando!')
                print(barra_loading(i, 100))
                sleep(0.01)
                clear_screen()
            del data
            data = data_default.copy()
            print('Resetado!')
            
        if opcao == 6:
            print('GANHADORES!!!!')
            while not data['quantidade_premios'] <= 0:
                realizar_sorteio(data)
            print('=================')
            obter_visao_geral(data)
            break
            
        input('<Enter>')
        clear_screen()
        

def menu(file):
    out = ''
    for linha in file:
        out += linha
    return out


main()