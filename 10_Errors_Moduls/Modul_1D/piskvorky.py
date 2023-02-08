#piskvorky.py

import util

def tah_hrace(pole):

    symbol = "o"
    while True:
        try:
            pozice = int(input('Zadej cislo pozice: '))
        except ValueError:    
            print("Musis zadat cislo!")
            
        else:    
            if pozice > 19 or pozice < 0: # zde jsem upravila len(pole) na 19
                print('Toto cislo nelze pouzit!')
                       
            elif pole[pozice] != '-':
                print("Toto pole je jiz obsazene!")
                
            else:
                pole = util.tah(pole, pozice, symbol)
                return pole
            
def vyhodnot(pole):
    
    if "xxx" in pole:
        return "x"
    elif "ooo" in pole:
        return "o"
    elif "-" not in pole:
        return "!"
    else:
        return "-"