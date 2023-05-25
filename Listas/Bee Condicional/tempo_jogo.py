def main():
    # entrada
    hora_inicio, hora_final = map(int, input().split())
    # processamento
    if hora_inicio > hora_final:
        hora_final = hora_final + 24
    resultado = hora_final - hora_inicio
    # saida
    print(f'O resultado é {resultado}')
main()