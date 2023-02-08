#ai.py

from random import randrange
import util

def tah_pocitace(pole):
    
    # symbol = "x"
    while True:
        
        pozice = randrange(len(pole))
        symbol = "x"
        if pole[pozice] == "-":
            pole = util.tah(pole, pozice, symbol)
            return pole