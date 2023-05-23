def main():
    a,b,c = map(int, input().split()) # conteiner
    x,y,z = map(int, input().split()) # navio
    
    largura_max = z // c
    comprimento_max = y // b
    altura_max = x // a
    
    volume_max = altura_max *  comprimento_max * largura_max
    
    print(volume_max)
 
main()