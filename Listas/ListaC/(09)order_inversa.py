
def main():
    # Entrada: 
    a = int(input('Me diga um número: ')) 
    b = int(input('Me diga outro número: '))

    print(f'Os números vistos em ordem oposta ao que vocẽ enviou são {inverter_num(a,b)}') # Saída
    
   #  num1, num2 = inverter_num(a,b) # "Desempacotamento" explicado na última aula
   #  print(f'Os números em ordem oposta a que você enviou são: {num1} e {num2}')
  
# Saída:
def inverter_num(a,b):
    return (b,a)

main()