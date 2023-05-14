def main():
    classe = str(input()).lower()
    filo = str(input()).lower()
    alimentacao = str(input()).lower()
    animal = qual_animal(classe, filo, alimentacao)
    print(animal)
  
def qual_animal(classe, filo, alimentacao):
    if classe == 'vertebrado':
        if filo == 'ave':
            if alimentacao == 'carnivoro':
                return 'aguia'
            
            if alimentacao == 'onivoro':
                return 'pomba'
            
        if filo == 'mamifero':
            if alimentacao == 'onivoro':
                return 'homem'
            if alimentacao == 'herbivoro':
                return 'vaca'  


    if classe == 'invertebrado':
        if filo == 'inseto':
            if alimentacao == 'hematofogo':
                return 'pulga'
            if alimentacao == 'herbivoro':
                return 'lagarta'
            
        if filo == 'anelideo':
            if alimentacao == 'hematofago':
                return 'sanguessuga'
            if alimentacao == 'onivoro':
                return 'minhoca'
            
            
    
main()