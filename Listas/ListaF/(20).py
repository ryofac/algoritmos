def main():
    angulo = int(input('Me dê o valor do ângulo ( entre 0 e 360 graus ): '))
    quadrante = verificar_quadrante(angulo)
    
    print(f'O quadrante que esse ângulo está é o {quadrante}º quadrante')
    
def verificar_quadrante(angulo):
    if angulo <= 90:
        return 1
    elif angulo <= 180:
        return 2
    elif angulo <= 270:
        return 3
    elif angulo <= 360:
        return 4
main()