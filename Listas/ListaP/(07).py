def main():
    vetor_a = [int(i) for i in input('Diga a sua lista(A): ').split()]
    vetor_b = [0 if item % 2 == 0 else 1 for item in vetor_a]
    print(vetor_b)
    
main()