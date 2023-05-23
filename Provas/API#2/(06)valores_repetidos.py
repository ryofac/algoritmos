def main():
    cod_alunos = []
    total = int(input())
    for i in range(total):
        valores = int(input())
        cod_alunos.append(valores)
    sem_repeticao = lista_corrigida(cod_alunos)
    print(sem_repeticao)

def lista_corrigida(lista):
    lista_retorno = []
    for i in lista:
        if not i in lista_retorno:
            lista_retorno.append(i)     
    return len(lista_retorno)
        
        
main()