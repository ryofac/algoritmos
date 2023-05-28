def main():
    cont_loop = 0
    while True:
        cont_loop += 1
        partidas = int(input())
        if partidas == 0:
            break
        print('Teste', cont_loop)
        jogador1 = input()
        jogador2 = input()
        
        for _ in range(partidas):
            escolha_a, escolha_b = [int(x) for x in input().split()]
            if (escolha_a + escolha_b)% 2 == 0:
                print(jogador1)
            else:
                print(jogador2)
        print()
            
            
main()