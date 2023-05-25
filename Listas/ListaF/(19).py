def main():
    altura = float(input('Qual a sua altura em metros? \n> '))
    peso = float(input('Qual o seu peso em quilogramas? \n> '))
    
    imc = calcular_imc(altura, peso)
    
    situacao = verificar_situacao(imc)
    
    print(f'Você tem um IMC de {imc:.2f} e sua situação é {situacao}')
    
    
    
def calcular_imc(altura, peso):
    return peso / altura ** 2

def verificar_situacao(imc):
    if imc > 30:
        return "OBESIDADE MÓRBIDA"
    elif imc < 30:
        return "OBESIDADE"
    elif imc < 25:
        return "NORMAL"
    
main()