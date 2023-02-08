
from random import randrange

while True:
    
    tah_cloveka = input('Zadej kamen, nuzky nebo papir: ')
        
    tah = randrange(0, 3)
    
    def tah_pocitace(tah):
        if tah == 0:
            return 'kamen'
        elif tah == 1:
            return 'nuzky'
        else:
            return 'papir'
        
    print(tah_pocitace(tah))   

    if tah_cloveka == tah_pocitace(tah):
        print('remiza')


    elif ((tah_cloveka == 'kamen') and (tah_pocitace(tah) == 'nuzky')) or ((tah_cloveka == 'nuzky') and (tah_pocitace(tah) == 'papir')) or ((tah_cloveka == 'papir') and (tah_pocitace(tah) == 'kamen')):
        print('Vyhral jsi ty')

    else:
        print('prohra')


