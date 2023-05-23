def main():
    while True:
        try:
            a,b,c,d = map(int, input().split())
            valor_mmc = mmc(b,d)
            
            soma = f'{a *  (valor_mmc // b) +  c * (valor_mmc // d)} / {valor_mmc}'
        except EOFError:
            print(soma)
    

def mmc(num1, num2) -> int | None:
    if num1 == 0 or num2 == 0:
        return
    maior = max((num1, num2))
    valor_minimo = num1 + num2 - maior
    cont = valor_minimo
    while cont <= maior:
        if cont % num1 == 0 and num2 % cont == 0:
            return cont
        cont += 1
    return maior * valor_minimo
main()

