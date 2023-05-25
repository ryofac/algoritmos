def main():
    
    data1 = input('Digite uma data no formato DD/MM/AAAA: ')
    data2 = input('Digite outra data no formato DD/MM/AAAA: ')
    
    mais_recente = qual_mais_recente(data1, data2)
    
    print(f'A data mais recente é {mais_recente}')
    
def qual_mais_recente(data1, data2):
    
    dia1 = data1[0:2]
    mes1 = data1[3:5]
    ano1 = data1[6:]
    
    dia2 = data2[0:2]
    mes2 = data2[3:5]
    ano2 = data2[6:]
    
    if ano1 > ano2:
        return data1
    if ano2 > ano1:
        return data2
    if ano1 == ano2:
        if mes1 > mes2:
            return data1
        if mes2 > mes1:
            return data2
        if mes1 == mes2:
            if dia1 > dia2:
                return dia1
            if dia2 > dia1:
                return dia2
            else:
                return "As datas são iguais!"
main()