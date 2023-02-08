# Vyjimky3.py

def vnitrni_funkce(delitel):
    return 1 / delitel

while True:
    try:
        cislo = int(input("Zadej delitel (musi byt vetsi nez nula): "))
        if cislo < 0:
            raise ValueError("Cislo {n} je mensi nez nula!".format(n=cislo))
        print(vnitrni_funkce(cislo))
        
    # except ValueError: 
    except ValueError as ve:
        print(ve)
    # except Exception:
    #     print("Vsechny ostatni vyjimky")
    else:
        print("Dekujeme za vyuziti")
        break
    finally:
        print("--- Probehla iterace. ---")
