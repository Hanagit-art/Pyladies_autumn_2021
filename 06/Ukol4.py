"Napiš funkci, která načte číslo a zjistí, jestli je sudé"

cislo = int(input("Zadej cislo: "))

def f(cislo):
    if cislo%2 == 0:
        return "sude cislo"
    else:
        return "liche cislo"
    
print(f(cislo))


"or"

# def napis_cislo(zadej):
#     cislo = int(input(zadej))

#     if cislo%2 == 0:
#         print("sude cislo")
#     else:
#         print("liche cislo")       
            
# napis_cislo("Zadej cislo: ") 
    