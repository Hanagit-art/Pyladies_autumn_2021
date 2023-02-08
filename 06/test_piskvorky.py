pole = "0------------------"
def tah(pole, pozice, symbol):
    """Vrátí herní pole s daným symbolem
       umístěným na danou pozici."""
    return pole[:pozice] + symbol + pole[pozice + 1:]

def tah_hrace(pole):
    """Ptá se hráče na kterou pozici chce hrát a vrací
       herní pole se zaznamenaným tahem"""
    while True:
        pozice = int(input("Na kterou pozici chceš hrát? "))
        if pozice >= 0 and pozice < len(pole) and pole[pozice] == "-":
            return tah(pole, pozice, "x")
        else:
            print("Špatná pozice, zkus to znovu. ")
            
print(tah_hrace(pole))