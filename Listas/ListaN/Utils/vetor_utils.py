def contem_caracter(vetor: list, caracter_analisado: str, ignore_case: bool = False) -> bool:
    return contar_caractere(vetor, caracter_analisado, ignore_case ) > 0


def contar_caractere(vetor: list, caractere:str, ignore_case: bool = False) -> int:
    if len(caractere) > 1:
        return 'Caracteres somente com 1 de tamanho!'
    cont_caractere = 0
    if ignore_case:
        for char in vetor: 
            if lowercase_char(caractere) == lowercase_char(char):
                cont_caractere += 1
        return cont_caractere
    
    for char in vetor: 
        if char == caractere:
            cont_caractere += 1
    return cont_caractere

# STRING UTILS:
def lowercase_char(char: str) -> str:
    if not eh_lower_char(char):
        return chr(ord(char) + 32)
    return char


def uppercase_char(char: str) -> str:
    if not eh_upper_char(char):
        return chr(ord(char) - 32)
    return char

def eh_upper_char(char: str) -> bool:
    return 65 <= ord(char) <= 90


def eh_lower_char(char: str) -> bool:
    return 97 <= ord(char)<= 122