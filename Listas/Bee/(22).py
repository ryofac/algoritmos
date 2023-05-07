def main():
    # entrada
    a,b,c,d = list(map(int, input().split()))
    # processamento
    if b > c and \
        d > a and c + d > a + b \
            and c > 0 and d > 0 \
                and is_even(a):
        # saida
        print('Valores aceitos')
    else:
        # saida2
        print('Valores nao aceitos')
def is_even(number):
    return number % 2 == 0
main()