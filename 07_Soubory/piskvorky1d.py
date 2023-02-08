# piskvorky1d.py

from random import randrange


def tah(pole, pozice, symbol):
    pole = pole[:pozice] + symbol + pole[pozice+1:]                
    return pole

"----------------------------------------------------"

def tah_hrace(pole):

    symbol = "o"
    while True:
        try:
            pozice = int(input('Zadej cislo pozice: '))
        except ValueError:    
            print("Musis zadat cislo!")
            
        else:    
            if pozice > 19 or pozice < 0:
                print('Toto cislo nelze pouzit!')
                       
            elif pole[pozice] != '-':
                print("Toto pole je jiz obsazene!")
                
            else:
                pole = tah(pole, pozice, symbol)
                return pole
            
"----------------------------------------------------"

def tah_pocitace(pole):
    
    symbol = "x"
    while True:
        
        pozice = randrange(len(pole))
        
        if pole[pozice] == "-":
            pole = tah(pole, pozice, symbol)
            return pole

"----------------------------------------------------"

def vyhodnot(pole):
    
    if "xxx" in pole:
        return "x"
    elif "ooo" in pole:
        return "o"
    elif "-" not in pole:
        return "!"
    else:
        return "-"
    
"----------------------------------------------------"   

def piskvorky1d():
    print("""1D PISKVORKY:
          
    Tvuj symbol: o
    Pocitat ma symbol: x""")

    print()
    print("Herni pole pro 1D piskvorky:")
    pole = "--------------------"
    
    while True:
        print(pole)
        print()
        pole = tah_hrace(pole)
        # print(pole)
    
        if vyhodnot(pole) != '-':
            break
        
        pole = tah_pocitace(pole)
        
        if vyhodnot(pole) != '-':
            break
        
    print(pole)
    if vyhodnot(pole) == "!":
        print("Remmiza")
    elif vyhodnot(pole) == "o":
        print("Vyhral jsi!")   
    elif vyhodnot(pole) == "x":
        print("vyhral pocitac!")
        
piskvorky1d()