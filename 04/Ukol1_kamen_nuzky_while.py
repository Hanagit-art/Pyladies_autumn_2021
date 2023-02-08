
import random

while True:

    tahy = ['kamen', 'nuzky', 'papir']
    tah_pocitace = random.choice(tahy)
    tah_cloveka = input('Zadej kamen, nuzky nebo papir: ')
    
    print(tah_pocitace)
    
    if tah_cloveka == 'konec':
        break    

    elif tah_cloveka == tah_pocitace:
        print('remiza')
    
    elif ((tah_cloveka == 'kamen') and (tah_pocitace == 'nuzky')) or ((tah_cloveka == 'nuzky') and (tah_pocitace == 'papir')) or ((tah_cloveka == 'papir') and (tah_pocitace == 'kamen')):
        print('Vyhral jsi ty')

    else:
        print('prohra')
    




