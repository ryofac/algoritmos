from str_utils import *
from getpass import getpass

def main():
    SENHA_CORRETA = 'rogerio4ever'
    
    obter_senha = getpass("Digite a senha: ")
    
    while not obter_senha == SENHA_CORRETA:
        print('Tente novamente!')
        obter_senha = getpass("Digite a senha: ")
    
    print('Bem vindo ao computador de Rogério da Silva! ')
        
    
    
    
    
main()