def main():
    casos_de_teste = int(input())
    
    for _ in range(casos_de_teste):
        tamanho = int(input())
        conversa_padrao = ''
        for i in range(tamanho):
            conversa = input()
            if i == 0:
                conversa_padrao = conversa
            elif conversa != conversa_padrao or conversa == '':
                conversa_padrao = 'ingles'
            
    print(conversa_padrao)
        
main()