# n-tice se nemeni "pod rukama", nemeni se datove struktury, mohou byt rychlejsi

# zaci = ("Aneta", "Bara", "Cecisl", "Dana")
# ovoce = "Jablko", "Merunka", "kvetak", "Angrest", "Rybiz"

# print(zaci)
# print(ovoce)

# mix = 3.24, "Nuz", True, 42

# for zak in zaci:
#     print(zak)
    
# print(zaci[2])

# print(zaci[1:])

# ovoce[2] = "citron"

# print(ovoce)

# divmod v pythonu
def podil_a_zbytek(a, b):
    return a // b, a % b

podil, zbytek = podil_a_zbytek(13, 5)

print(podil)
print(zbytek)

osoby = "mama", "teta", "babicka", "vrah"
vlastnosti = "hodna", "mila", "laskava", "zaludny"

for osoba, vlastnost in zip(osoby, vlastnosti):
    print(osoba, "je", vlastnost)

# toto dela funkce zip 
("mama", "hodna")
("teta", "mila")
("babicka", "laskava")
("vrah", "zaludny")

prazdna_ntice = ()
jednprvkova_ntice = "kastan"

print(jednprvkova_ntice)



