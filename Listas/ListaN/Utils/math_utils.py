from random import random
from math import floor
def escolher_aleatorio(vetor: list):
    return vetor[floor(numero_aleatorio_entre(0, len(vetor)))]

def numero_aleatorio_entre(limite_min:float , limite_max: float) -> float:
    return random() * (limite_max - limite_min) + limite_min