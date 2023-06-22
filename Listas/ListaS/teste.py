def main():
    mostrar(['impar e multiplo de 3' if x % 2 and x % 3 == 0 else '' for x in [x for x in range(100)]])


def mostrar(elemento):
    print(elemento)

main()