from utils.vetor_utils import *
from utils.io_utils import *
from colorama import Fore

def abrir_arquivo(file, tipo = None):
    file = open(file)
    file_vetor = mapear(file.readlines(), lambda x: x.strip()) # remover espaços
    if tipo == 'pessoa':
        pessoas = []
        for lines in file_vetor:
            lines = str(lines)
            lines = lines.split('#')
            print(lines)
            pessoa = new_pessoa(nome=lines[0], sexo=lines[1])
            pessoas.append(pessoa)
        return pessoas
        
    return file_vetor

def gerar_menu(*options, title, center=False):
    menu = title if not center else centralize(title)
    for i in range(len(options)):
        if center:
            menu += centralize(f'\n{i + 1} - {options[i]}')
        else:
            menu += f'\n{i + 1} - {options[i]}'
    menu += '\n > '
    return menu


def obter_pessoa(adjetivos):
    tem_pessoa = False
    nome = obter_texto('Digite seu nome: ')
    for adjetivo in adjetivos:   
        if nome[0] in adjetivo[0]:
            tem_pessoa = True
    if not tem_pessoa:
        print('Seu nome não se relaciona com nenhum adjetivo cadastrado')
        print('Mas não se preoucupe, você pode sempre <ADCIONAR> um no menu principal!')
        return
    disclaimer = Fore.LIGHTBLACK_EX + '(Determinado somente pela letra final do nome)' + Fore.RESET
    eh_automatico = obter_texto(f'Tentar fazer a correspondência de gênero automática? (Y/n) \n {disclaimer} \n > ').strip().upper()
    print()
    automatico = True if(eh_automatico == 'Y' or eh_automatico == '') else False    

    nomes_escolhidos = []
    for adjetivo in adjetivos:
        if adjetivo[0] == nome[0]:
            nomes_escolhidos.append(adjetivo)
    apelido = escolher_item_aleatorio(nomes_escolhidos)
    
    # Checagens de gênero
    if automatico:
        genero = 'F' if nome[-1] == 'a' else  'M'
        if nome[-1] == 'a' and apelido[-1] == 'o':
            new_apelido = ''
            for i in range(len(apelido) - 1):
                new_apelido += apelido[i]
            new_apelido += 'a'
            apelido = new_apelido
            
        if nome[-1] == 'a' and apelido[-1] == 'r':
            new_apelido = ''
            for i in range(len(apelido)):
                new_apelido += apelido[i]
            new_apelido += 'a'
            apelido = new_apelido
    else:
        obter_genero = obter_texto('Digite seu gênero: \n(1/M) - Masculino\n(2/F)- Feminino\n(3/N) - Não declarar \n > ').strip().upper()
        # Verificacoes de genero
        if obter_genero == '1' or obter_genero == 'M': genero = 'M'
        if obter_genero == '2' or obter_genero == 'F': genero = 'F'
        if obter_genero == '3' or obter_genero == 'N': genero = 'N'
        if genero == 'F' and apelido[-1] == 'o':
            new_apelido = ''
            for i in range(len(apelido) - 1):
                new_apelido += apelido[i]
            new_apelido += 'a'
            apelido = new_apelido
        if genero == 'F' and apelido[-1] == 'r': 
            new_apelido = ''
            for i in range(len(apelido)):
                new_apelido += apelido[i]
            new_apelido += 'a'
            apelido = new_apelido
        
    out = f' {nome} {apelido}'
    pessoa = new_pessoa(out, genero)   
    return pessoa
    
def gerar_novo_adjetivo(adjetivos):
    novo = obter_texto('Digite o novo adjetivo a ser adcionado: ')
    adjetivos.append(novo)
    print(f'{novo} Adcionado com sucesso!') if novo in adjetivos else print('Algo deu errado!')
    

def write_in_file(file, content, tipo=None):
    stream = open(file, 'w')
    lines = ''
    for item in content:
        if(not item): continue
        if tipo == 'pessoas':
             lines += str(item["nome"]) + '#' + str(item["sexo"]) + '\n'
        else:
            lines += f'{item}\n'
    stream.writelines(lines)
    sleep(0.3)
    print(Fore.GREEN + centralize(f'Arquivo {file} salvo com sucesso!')+ Fore.RESET)
    
    
def new_pessoa(nome, sexo):
    pessoa = {
        'nome': nome,
        'sexo': sexo
    }
    return pessoa

def mostrar_pessoas(pessoas):
    clear_screen()
    for pessoa in pessoas:
        sexo = pessoa['sexo']
        if sexo == 'M': genero = Fore.BLUE + 'Masculino' + Fore.RESET
        if sexo == 'F': genero = Fore.RED + 'Feminino' + Fore.RESET
        if sexo == 'N': genero = Fore.GREEN + 'Não declarado' + Fore.RESET
        printcenter('======================')
        printcenter('NOME: ' + pessoa['nome'])
        printcenter('GÊNERO: ' + genero)
        printcenter('======================')
    enter_to_continue()

def bye(file):
    cores = [Fore.YELLOW, Fore.BLUE, Fore.CYAN, Fore.MAGENTA]
    stream = open(file)
    frases_nostalgicas_para_despedidas = mapear(stream.readlines(), lambda x: x.strip())
    frase_para_lembrar_da_turma_maravilhosa_de_ads_2023 = '<LOG> ' + escolher_item_aleatorio(frases_nostalgicas_para_despedidas)
    print(escolher_item_aleatorio(cores) + centralize(frase_para_lembrar_da_turma_maravilhosa_de_ads_2023)+ Fore.RESET)