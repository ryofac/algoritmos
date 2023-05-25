# 17. Leia valores inteiros em duas variáveis distintas e se o resto da divisão da primeira pela segunda for 1
# escreva a soma dessas variáveis mais o resto da divisão; se for 2 escreva se o primeiro e o segundo valor
# são pares ou ímpares; se for igual a 3 multiplique a soma dos valores lidos pelo primeiro; se for igual a 4
# divida a soma dos números lidos pelo segundo, se este for diferente de zero. Em qualquer outra situação
# escreva o quadrado dos números lidos.

def main():
    num1 = int(input('Digite o valor do primeiro número: '))
    num2 = int(input('Digite o valor do segundo número: '))
    if num1 % num2 == 1:
        print(num1 + num2 + 1)
    if num1 % num2 == 2:
        print('num1 eh par') if num1 % 2 == 0 else print('num1 eh impar')
        print('num2 eh par') if num2 % 2 == 0 else print('num2 eh impar')
    if num1 % num2 == 3:
        multiplica_soma = num1 * ( num2 + num1)
        print(multiplica_soma)
    if num1 % num2 == 4:
        if num2 != 0:
            print((num1 + num2)/num2)
    else:
        print('num1 ^ 2: ', num1 ** 2)
        print('num2 ^ 2: ', num2 ** 2)
    