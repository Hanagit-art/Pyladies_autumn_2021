# Ukol0.py
"""Napiš funkci, která dostane jako argumenty seznam zvířat a slovo a zjistí, jestli je toto slovo v seznamu. 
„Zjistí“ znamená, že funkce vrátí True nebo False."""


# animals = ["dog", "cat", "rabbit", "snake", "kangaroo"]


# def verify(animal, animals):
        
#     if animal in animals:
#         return True
#     else:
#         return False

# while True:
#     animal = input("Zadej zvire v anglictine: ")
#     if animal == "end":
#         break
    
#     print(verify(animal, animals))
    
"""Napiš funkci, která dostane jako argument seznam domácích zvířat a vrátí seznam těch, která jsou kratší než 5 písmen."""


# def verify(animals):
#     new_animals = []   
#     for word in animals:
#         if len(word) < 5:
#             new_animals.append(word)
#     return new_animals
         
# print(verify(animals))

"""Napiš funkci, která dostane jako argument seznam domácích zvířat a vrátí seznam těch, která začínají na k."""

# def verify(animals):
#     new_animals = []   
#     for word in animals:
#         if word[0] == "k" or word[0] == "K":
#             new_animals.append(word)
#     return new_animals
         
# print(verify(animals))

"""Napiš program, který seřadí seznam domácích zvířat podle abecedy. Víš, jaký je rozdíl mezi metodou sort a funkcí sorted?"""

# animals.sort()
# print(animals)

# sorted(animals)
# print(animals)

"""Sort a sorted jsou podobne, ale sorted muze pouzit slovniky, seznamy i N-tice.
Sorted funkce se pouziva tam, kde chceme zachovat puvodni seznam. Funkce vraci seznam, 
takze je nutne vracena data priradit do nove promenne. Sort funkce updatuje puvodni seznam, 
nema zadnou navratovou hodnotu."""

# Napiš funkci, která dostane dva seznamy jmen zvířat a vrátí tři seznamy:

# animals1 = ["dog", "cat", "rabbit", "snake", "kangaroo"]
# animals2 = ["dog", "monkey", "fish", "snake", "elephant"]

# def f(animals1,animals2):
#     common = []
#     for animal in animals1:
#         if animal in animals2:
#             common.append(animal)

#     diff1 = []
#     for animal in animals1:
#         if animal not in animals2:
#             diff1.append(animal)
            
#     diff2 = []
#     for animal in animals2:
#         if animal not in animals1:
#             diff2.append(animal)
            
#     return common,diff1,diff2

# print(f(animals1,animals2))
                

"""Napiš funkci, která dostane dvojici (tzv. tuple) a vrátí její součet. 
okud funkce dostane více jak dvě čísla, tj. např. trojici, tak vypíše: "Bohužel, umím sečíst jen dvě čísla.":"""

# long verze

# def add(tuple):
            
#     if len(tuple) == 2:
#         soucet = tuple[0] + tuple[1]
#         return soucet
        
# tuple = []
# while True:
    
#     cislo = int(input('Zadej cislo: '))
#     tuple.append(cislo)
    
#     if len(tuple) == 1:
#         cislo = int(input('Zadej cislo: '))
#         tuple.append(cislo)
       
#     if len(tuple) > 2:
#         break
    
#     print(add(tuple))
        
# print("Bohužel, umím sečíst jen dvě čísla.")

# short verze

# tuple = [1,2,3]   
 
# def add(tuple):
            
#     if len(tuple) == 2:
#         soucet = tuple[0] + tuple[1]
#         return soucet
    
#     elif len(tuple) > 2:
#         return "Bohužel, umím sečíst jen dvě čísla."
        
# print(add(tuple))
        
"""Had byl pyšný na to, že je v abecedě první. Dokud nepřiletěla "andulka".

Abys hada uklidnila, vytvoř funkci, která zvířata seřadí podle abecedy, ale bude ignorovat první písmeno t.j. vrátí:

"had",
"pes",
"andulka",
"kočka",
"králík".
Postup:

Máš seznam hodnot, které chceš seřadit podle nějakého klíče. Klíč se dá z každé hodnoty vypočítat.
Vytvoř seznam dvojic (klíč, hodnota).
Seřaď tento seznam dvojic – dvojice se řadí nejdřív podle prvního prvku, pak druhého atd.
Nakonec vytvoř ze seznamu dvojic opět jen seznam hodnot.
Proč má zrovna had takovéhle výsadní postavení, zjistíš později."""

seznam = ["had","pes","andulka","kocka","kralik"]
seznam_abc = sorted(seznam)

def f(seznam_abc):
    dvojice = []
    for zvire in seznam_abc:
        dvojice.append((zvire[1], zvire))
   
    seznam_pismen = []
    for zvire in seznam_abc:
        seznam_pismen.append(zvire[1])

    dvojice = []
    for pismeno, zvire in zip(seznam_pismen, seznam_abc):
        x = pismeno,zvire
        dvojice.append(x)
    return dvojice

dvojice = f(seznam_abc)
    
# print(seznam)
# print(seznam_abc)
print(dvojice)
dvojice.sort()
print(dvojice)

for zvire in dvojice:
    print(zvire[1])

"-----------------------------------------------------------------"
    
# s pouzitim dictionaries

# dvojice = dict(dvojice)
# dvojice = dict(sorted(dvojice.items()))
# print(dvojice)

# for zvire in dvojice.values():
#     print(zvire)
"-----------------------------------------------------------------"
    
# seznam = "had","pes","andulka","kocka","kralik"

# seznam_abc = sorted(seznam)
# # print(seznam_abc)

# def f(seznam_abc):
#     novy_seznam = sorted(seznam_abc, key=lambda x: x[1])
#     return novy_seznam

# print(f(seznam_abc))

# for zvire in f(seznam_abc):
#     print(zvire)
        

    

    