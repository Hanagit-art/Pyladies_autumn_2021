
stastnych_pet = [3,5,7,47,98]
potraviny = ["fazalo", "kukurice", "ryze", "kureci_maso"]
bordel = [3, "fazaole", True, 4.2, None]

# potraviny[1] = "parek"

# print(potraviny)

# print(potraviny[1:3])

# print(len(potraviny))

# potraviny.append("zmrlina")

# print(potraviny)

# for index in range(len(potraviny)):
#     print(potraviny[index])
    
# for index in potraviny:
#     print(potraviny)    

"---------------------------------------------------"
# append

# prvocisla = [2, 3, 5, 7, 11, 13, 17]
# print(prvocisla)
# prvocisla.append(19)
# print(prvocisla)

# dalsi_prvocisla = [23, 29, 31]
# prvocisla.extend(dalsi_prvocisla)
# print(prvocisla)

"----------------------------------------------------"
# extend

# seznam = []
# seznam.extend('abcdef')
# seznam.extend(range(10))
# print(seznam)

"----------------------------------------------------"
# Meneni prvku

# cisla = [1, 0, 3, 4]
# cisla[1] = 2
# print(cisla)

# cisla[1:-1] = [6, 5]
# print(cisla)

"----------------------------------------------------"
# Mazani prvku

# cisla = [1, 2, 3, 4]
# cisla[1:-1] = [0, 0, 0, 0, 0, 0]
# print(cisla)
# cisla[1:-1] = []
# print(cisla)

"----------------------------------------------------"

# cisla = [1, 2, 3, 4, 5, 6]
# del cisla[-1]
# print(cisla)
# del cisla[3:5]
# print(cisla)
# del cisla
# print(cisla)

"----------------------------------------------------"

# pop, remove, clear

# cisla = [1, 2, 3, 'abc', 4, 5, 6, 12]
# posledni = cisla.pop()
# print(posledni)
# print(cisla)

# cisla.remove('abc')
# print(cisla)

# cisla.clear()
# print(cisla)

"----------------------------------------------------"

#  Razeni

# x = sorted([4, 7, 8, 3, 5, 2, 4, 8, 5])
# print(x)

# # seznam = [4, 7, 8, 3, 5, 2, 4, 8, 5]
# # seznam.sort()
# # print(seznam)

# seznam = [4, 7, 8, 3, 5, 2, 4, 8, 5]
# seznam.sort(reverse=True)
# print(seznam)

"----------------------------------------------------"

# Známé operace se seznamy

# melodie = ['C', 'E', 'G'] * 2 + ['E', 'E', 'D', 'E', 'F', 'D'] * 2 + ['E', 'D', 'C']
# print(melodie)

# print(len(melodie))         # Délka seznamu
# print(melodie.count('D'))   # Počet 'D' v seznamu
# print(melodie.index('D'))   # Číslo prvního 'D'
# print('D' in melodie)       # Je 'D' v seznamu?

# "Toto uz nefunguje!"

# print('DE' in melodie)
# print(melodie.count('DE'))
# print(melodie.index('DE'))

"----------------------------------------------------"
# Seznam jako podmínka

# seznam = [4, 7, 8, 3, 5, 2, 4, 8, 5]
# if seznam:
#     print('V seznamu něco je!')
# else:
#     print('Seznam je prázdný!')
    
"----------------------------------------------------"
# Tvoreni seznamu - funkce list - vytovri z retezce seznam znaku

# abeceda = list('abcdefghijklmnopqrstuvwxyz')
# cisla = list(range(100))
# print(abeceda)
# print(cisla)# abeceda = list('abcdefghijklmnopqrstuvwxyz')
# cisla = list(range(100))
# print(abeceda)
# print(cisla)

"Muzeme udelat i list ze seznamu - vytovri se novy seznam nezavisly na tom starem."
# a = [1, 2, 3]
# b = list(a)

# print(b)
# a.append(4)
# print(b)

"----------------------------------------------------"

# mocniny_dvou = []
# for cislo in range(10):
#     mocniny_dvou.append(2 ** cislo)
# print(mocniny_dvou)

"----------------------------------------------------"

# balicek = []
# for barva in '♠', '♥', '♦', '♣':  # (Na Windows použij textová jména)
#     for hodnota in list(range(2, 11)) + ['J', 'Q', 'K', 'A']:
#         balicek.append(str(hodnota) + barva)
# print(balicek)

"----------------------------------------------------"
# Funkce split - vytvori z retezce seznam slov

slova = 'Tato věta je složitá, rozdělme ji na slova!'.split()
print(slova)

zaznamy = '3A,8B,2E,9D'.split(',')
print(zaznamy)

veta = ' '.join(slova)
print(veta)

"----------------------------------------------------"
#  Seznamy a náhoda

import random

# balicek = []
# for barva in '♠', '♥', '♦', '♣':
#     for hodnota in list(range(2, 11)) + ['J', 'Q', 'K', 'A']:
#         balicek.append(str(hodnota) + barva)
# print(balicek)

# random.shuffle(balicek)
# print(balicek)


# while True:
#     mozne_tahy = ['kámen', 'nůžky', 'papír']
#     tah_pocitace = random.choice(mozne_tahy)
    
#     print("pokracuj")
    
#     if tah_pocitace == 'kámen':
#         break
    
"----------------------------------------------------"

#  Vnořené seznamy

# seznam_seznamu = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# prvni_seznam = seznam_seznamu[0]
# print(prvni_seznam)

# druhy_seznam = seznam_seznamu[1]
# prvni_prvek_druheho_seznamu = druhy_seznam[0]
# print(prvni_prvek_druheho_seznamu)
# prvni_prvek_druheho_seznamu = (seznam_seznamu[1])[0]
# print(prvni_prvek_druheho_seznamu)

"----------------------------------------------------"

# Tabulka

# def vytvor_tabulku(velikost=11):
#     seznam_radku = []
#     for a in range(velikost):
#         radek = []
#         for b in range(velikost):
#             radek.append(a * b)
#         seznam_radku.append(radek)
#     return seznam_radku

# nasobilka = vytvor_tabulku()

# print(nasobilka[2][3])  # dva krát tři
# print(nasobilka[5][2])  # pět krát dva
# print(nasobilka[8][7])  # osm krát sedm

# # Vypsání celé tabulky
# for radek in nasobilka:
#     for cislo in radek:
#         print(cislo, end=' ')
#     print()   