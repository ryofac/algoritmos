# Nesse eu me empolguei um pouco e fiz duas versões:
# Uma converte decimal para binário e a outra faz o que o exercício manda 
while True:
    pergunta = int(input('Qual opção vc quer (1/2)? \n >> '))
    if pergunta == 1:
        
        # Entrada 1:
        binario = int(input('Digite o número de 4 dígitos: '))
        numeros = []

        # Processamento 1:
        while True:
            print(binario)
            numeros.append(binario % 2)
            binario = binario // 2
            if binario == 0 or binario == 1:
                numeros.append(binario % 2)
                break
            
        # Saída 1: 
        print('O binário é:')
        for c in numeros[::-1]:
            print(c, end='')
            print('')
        break
    # Todo esse trabalho foi pura vontade de sofrer, existe a função chamado int({numero}, {base=})
    
    if pergunta == 2:
        
        # Entrada 2:
        binary = (input('Digite um número de 4 dígitos binário \n >> '))
        
        # Processamento:
        # Saída:
        print(f'O número convertido em binário é {int(binary, base=2)}: ')       
    break
