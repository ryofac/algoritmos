def main():
    senha_default = '1234'
    senha = input('Digite sua senha: ')
    if senha == senha_default:
        print('Senha certa!')
        return
    print('Senha errada!')
    
main()