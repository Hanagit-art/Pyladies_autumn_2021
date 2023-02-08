
#hra.py

import ai
import piskvorky as p

def piskvorky1d():
    print("""1D PISKVORKY:
          
    Tvuj symbol: o
    Pocitat ma symbol: x""")

    print()
    print("Herni pole pro 1D piskvorky:")
    pole = 20* "-"
    
    while True:
        print(pole)
        print()
        pole = p.tah_hrace(pole)
        # print(pole)
    
        if p.vyhodnot(pole) != '-':
            break
        
        pole = ai.tah_pocitace(pole)
        
        if p.vyhodnot(pole) != '-':
            break
        
    print(pole)
    if p.vyhodnot(pole) == "!":
        print("Remmiza")
    elif p.vyhodnot(pole) == "o":
        print("Vyhral jsi!")   
    elif p.vyhodnot(pole) == "x":
        print("vyhral pocitac!")
        
piskvorky1d()