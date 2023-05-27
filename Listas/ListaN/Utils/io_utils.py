from os import get_terminal_size, system, name

def printcenter(texto: str) -> None:
    tamanho_terminal = get_terminal_size().columns
    meio = (tamanho_terminal // 2) - len(texto)
    print(' ' * meio + texto )
    
def clear_screen():
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

def enter_to_continue():
    input('<ENTER to continue...')
    clear_screen()

           
           
            
    
        
            
    
    
