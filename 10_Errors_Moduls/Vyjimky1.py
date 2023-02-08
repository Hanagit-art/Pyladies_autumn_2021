# Vyjimky1.py

# def vnejsi_funkce():
#     return vnitrni_funkce(0)

# def vnitrni_funkce(delitel):
#     return 1 / delitel

# delitel = int(input("Zadej delitel: "))

# print(vnitrni_funkce(delitel))

"----------------------------------------------------------"

# def vnejsi_funkce():
#     return vnitrni_funkce(0)

def vnitrni_funkce(delitel):
    return 1 / delitel

while True:   
    try:
        cislo = int(input("Zadej delitel: "))
        print(vnitrni_funkce(cislo))
        
    except ValueError:
        print("Zadejte cislo.")
    except ZeroDivisionError:
        print("Cislo nesmi byt nula.")
    else:
        print("Dekujeme za vyuziti")
        break

"----------------------------------------------------------"
    
# def nacti_cislo():
#     while True:
#         odpoved = input('Zadej číslo: ')
#         try:
#             return int(odpoved)
#         except ValueError:
#             print('To nebylo číslo! Zkus to znovu.')
            
# nacti_cislo()

# "----------------------------------------------------------"
# VELIKOST_POLE = 20

# def over_cislo(cislo):
#     if 0 <= cislo < VELIKOST_POLE:
#         print('OK!')
#     else:
#         raise ValueError('Čislo {n} není v poli!'.format(n=cislo))
    
#     over_cislo()