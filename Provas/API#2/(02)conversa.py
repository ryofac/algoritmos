def main():
    try:
        quantidade_testes = int(input())
        for c in range(quantidade_testes):
            linguas = []
            quantidade_linguas = input()
            for i in range(quantidade_linguas):
                lingua = input()
                linguas.append(lingua)
                
                
    except EOFError:
        return 

def tem_diferente(linguas):
    lingua_anterior = linguas[0]
    for i in range(1, len(linguas)):
        if lingua_anterior == linguas[i]:
            continue
        else:
            return 'ingles'
        

main()