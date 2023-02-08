
#util.py

def tah(pole, pozice, symbol):        
    pole = pole[:pozice] + symbol + pole[pozice+1:]                
    return pole