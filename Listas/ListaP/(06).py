def main():
	print(' Separe por espaços! ')
	binarios = [int(x) for x in input('Digite um binário com 8 digitos: ').split()]
 
	while len(binarios) != 8:
		print('Preencha os 8espaços!')
		binarios = [int(x) for x in input('Digite um binário com 8 digitos: ').split()]
  
 
	print('Em hexadecimal > ', bin_hexa(binarios))
	print('Em decimal > ', bin_dec(binarios))
  


def bin_dec(binarios):
	resultado = 0

	for x in range(len(binarios)):
		resultado += binarios[len(binarios) -1 - x] * 2 ** x

	return resultado


def bin_hexa(binarios):
	resultado_1 = 0
	resultado_2 = 0
	hexadecimal_chars = ['A', 'B', 'C', 'D', 'E', 'F']

	for x in range(len(binarios)):
		if x < 4:
			resultado_1+= (binarios[len(binarios) -1 -x]) * 2 ** x

		else:
			resultado_2 += binarios[len(binarios) -1 -x] * 2 ** (x-4)



	return str(resultado_2 if resultado_2 < 10 else hexadecimal_chars[resultado_1 - 10]) + (str(resultado_1 if resultado_1 < 10 else hexadecimal_chars[resultado_2 - 10]))


main()