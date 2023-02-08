
"""Napiš program, který se ptá uživatele na čísla do té doby, než zadá 0. Poté vypíše nejmenší ze zadaných čísel. (Pozor: nula se mezi porovnávaná čísla nepočítá.)

Nápověda: průběžně stačí ukládat jen údaj, které číslo je aktuálně to nejmenší."""

    
# number = 10**10
# while True:       
#     number = min(int(input('zadej cislo: ')), number)              
#     if number == 0:
#         break
#     print(number)

"----------------------------------------------------------------"
    
number = int(input('zadej cislo: '))
while True:
    if number == 0:
        break   
    zadej = int(input('zadej cislo: '))
    if zadej == 0:
        break
    number = min(zadej, number)
    
print(number)
    
"-----------------------------------------------------------------"

# def min_number(number):
    
#     number = 10**10
#     while True:
#         zadej = int(input('zadej cislo: '))
#         if zadej == 0 or number == 0:
#             break
#         number = min(zadej, number)
#     return number
    
# number = min_number()
# print(number)