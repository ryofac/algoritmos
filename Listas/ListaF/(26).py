def main():
    print('Considerando um triângulo retângulo!')
    lado1 = int(input('Digite o valor do primeiro lado: '))
    lado2 = int(input('Digite o valor do segundo lado: '))
    lado3 = int(input('Digite o valor do terceiro lado: '))
    
    if lado1 >= lado2 and lado1 >= lado3:
        print(f'{lado1} é a hipotenusa e os demais são seus catetos')
    elif lado2 >= lado1 and lado2 >= lado3:
        print(f'{lado2} é a hipotenusa e os demais são seus catetos')
    elif lado3 >= lado1 and lado3 >= lado2:
        print(f'{lado3} é a hipotenusa e os demais são seus catetos')
    
main()
