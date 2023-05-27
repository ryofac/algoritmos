from os import get_terminal_size, system, name

def printcenter(texto: str) -> None:
    tamanho_terminal = get_terminal_size().columns
    meio = (tamanho_terminal // 2) - len(texto)
    print(' ' * meio + texto )
    
def clear_screen() -> None:
    try:
        if name == 'posix':
            system("clear")
        else:
            system("cls")
    except:
        return 

def obter_numero_positivo(label = 'Me diga um número positivo: ', tem_limite = False, limite = None):
    numero = int(input(label))
    while numero < 0:
        numero = int(input(label))
    if tem_limite:
        if not limite:
            print('Reveja sua função limite e passe os parâmetros corretos!')
            return
        while not (numero < limite):
            print('Valor maior que o limite!')
            numero = int(input(label))
            
    return numero


def obter_texto(label:str = 'Texto: ') -> str:
    texto = input(label)
    return texto


def obter_texto_max(label:str, tamanho_max:int) -> str:
    texto = obter_texto(label)
    while len(texto) > tamanho_max:
        return obter_texto_max(f'Texto de no máx({tamanho_max}): ', tamanho_max)
    return texto


def enter_to_continue() -> None:
    input('<ENTER to continue...')
    clear_screen()
    


           
           
            
    
        
            
    
    
