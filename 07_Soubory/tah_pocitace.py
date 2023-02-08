# tah_pocitace.py

from random import randrange

pole = 19 * "-"
symbol = "x"

def tah(pole, pozice, symbol):
    return pole[:pozice] + symbol + pole[pozice + 1:]

def tah_pocitace(pole):
    while True:
        
        pozice = randrange(len(pole))
        
        if pole[pozice] == "-":
            pole = tah(pole, pozice, symbol)
            return pole

print(tah_pocitace(pole))