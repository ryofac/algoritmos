def main():
    farinha, ovo, leite = map(int, input().split())
    bolos = quantos_bolo(farinha, ovo, leite)
    print(bolos)

def quantos_bolo(f, o, l):
    cont_bolo = 0
    while True:
        if pode_bolo(f,o,l):
            cont_bolo += 1
            f = f - 2
            o = o - 3
            l = l - 5
        else:
            break
    return cont_bolo

def pode_bolo(farinha, ovo, leite):
    return farinha >= 2 and ovo >= 3 and leite >=5
main()
