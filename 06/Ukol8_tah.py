
# Napiš funkci tah, která dostane řetězec s herním polem, číslo políčka (0-19), a symbol (x nebo o) a vrátí herní pole (t.j. řetězec) s daným symbolem umístěným na danou pozici.

# Hlavička funkce by tedy měla vypadat nějak takhle:

# def tah(pole, cislo_policka, symbol):
#     "Vrátí herní pole s daným symbolem umístěným na danou pozici"
#     ...
# Můžeš využít nějakou funkci, kterou jsme napsaly už na sraze?


   
def tah(pole, cislo_policka, symbol): 
    "viz Retezce_string2 zamen"
    return pole[:cislo_policka] + symbol + pole[cislo_policka+1:]
    
print(tah("--------------------", 4, "x"))