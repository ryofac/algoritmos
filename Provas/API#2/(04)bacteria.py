def main():
    while True:
        try:
            dna = input()
            sequencia = input()
            if sequencia in dna:
                print('Resistente')
            else:
                print('Nao resistente')
        except EOFError:
            return 
    
        
main()