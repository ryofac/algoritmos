import math
from time import sleep
def main():
    numero = 0.05
    while True:
        amplitude = math.cos(numero) * 10
        numero += 1
        print('a' * (int(amplitude) + 10), flush = True)
            
main()
