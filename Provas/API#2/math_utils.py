import io_utils as io

# ===== Matematica financeira ====
def calcular_Juros(emprestimo: float, taxa: float, prazo: float):
    return emprestimo * porcentagem_de(taxa) * prazo if 0 > taxa > 100 else emprestimo * taxa * prazo


def calcularMontanteJurosCompostos(emprestimo:float, taxa:float, prazo:float):
    contador_meses = 0
    capital = emprestimo
    while contador_meses < prazo:
        juros = capital * taxa
        capital += juros 
        contador_meses += 1
    return capital


def calcularJurosCompostos(emprestimo:float, taxa:float, prazo:float):
    montante = calcularMontanteJurosCompostos(emprestimo, taxa, prazo)
    return montante - emprestimo


# ===== Geometria =====
def calcular_area_circulo(raio:float, pi = 3.14):
    return 2 * pi * raio 


def calcular_area_triangulo(base: float, altura: float):
    return (base * altura) / 2


def calcular_area_trapezio(base_maior:float, base_menor:float, altura:float):
    return (base_maior + base_menor) * altura / 2


def calcular_area_quadrado(lado:float):
    return lado **2


def distancia_entre_pontos(x1: float, y1: float, x2:float, y2:float):
    cateto1 = x2 - x1
    cateto2 = y2 - y1
    return raiz_quadrada_de(cateto1 ** 2 + cateto2 ** 2)


# === Utilidades ===

def calcular_media(*valores : list[float]) -> float:
    soma = 0
    quantidade = 0
    for item in valores:
        soma += item
        quantidade += 1
    return soma / quantidade
        
def fib(termo:int): # Fibonnaci recursivo
    if termo == 1 or termo == 2:
        return 1
    else:
        return fib(termo-1) + fib(termo-2)


def contar_ate(num: int):
    contador = 0
    while contador != num:
        contador += 1
        io.printslow(f'...{contador}', speed= 0.2, inline= True)
        if contador % 10 == 0:
            print()


def fatorial(num: int):
    multiplicador = 1
    contador = 0
    while contador < num:
        contador += 1
        multiplicador *= contador
    return multiplicador


def porcentagem_de(num: float):
    return num / 100


def raiz(num:float, indice:int):
    return num ** (1/indice)



def raiz_quadrada_de(num: float):
    return num ** (1/2)


def raiz_cubica_de(num: float):
    return num ** (1/3)

def mmc(num1, num2) -> int | None:
    if num1 == 0 or num2 == 0:
        print('Valores de MMC INVÁLIDOS')
        return
    maior = valor_maximo_de(num1, num2)
    valor_minimo = num1 + num2 - maior
    cont = valor_minimo
    while True:
        if eh_multiplo(num1, cont) and eh_multiplo(num2, cont):
            return cont
        cont += 1

# ==== Check Functions ====
def eh_numero_perfeito(num: int):
    soma_divisores = 0
    for c in range(1, num):
        if eh_divisor(num, c):
            soma_divisores += c
        print(soma_divisores)
    return soma_divisores == num
                    
    
def eh_divisor(numero, candidato):
    return numero % candidato == 0

def eh_multiplo(numero, candidato):
    return candidato % numero == 0


def eh_par(numero):
    return numero % 2 == 0


def eh_primo(numero):
    anterior = 1
    cont_multiplos = 0
    while anterior < numero:
        anterior += 1
        if eh_multiplo(numero, anterior):
            cont_multiplos += 1
    return cont_multiplos == 1

# def eh_ano_bissexto():
    

# === Conversão ===
def anos_meses(anos):
    return anos * 12

def meses_dias(meses):
    return meses * 30



 # === Intervalos ===
 
def valor_maximo_de(*valores: int):
    valor_grandao = float('-inf')
    for values in valores:
        if values > valor_grandao:
            valor_grandao = values
    return valor_grandao
      
        
def valor_minimo_de(*valores: int):
    valor_menorzinho = float('inf')
    for values in valores:
        if values < valor_menorzinho:
            valor_menorzinho = values
    return valor_menorzinho



    



if __name__ == "__main__":
    io.title('MATH UTILS')
    io.printslow('Olá, sou o módulo extra para o facilitamento de algumas ações matemáticas!')
    io.printslow('Eu não consigo rodar sozinho, para me testar, vá em algum módulo.py em que eu esteja presente!')


