
# Zadej libovolny pocet cisel cisel, oddelenych carkou: 5,6,5,8,24

retezec = input("Zadej cisla oddelena carkou: ")

cisla = retezec.split(",")

print(cisla)

soucet = 0
for cislo in cisla:
    soucet += int(cislo)
    
print(soucet)

"--------------------------------------------------------------------------------"

osoba = {
    "jmeno": "Jana",
    "prijmeni": "Nova",
    "narozeni": "7.1.1995"
}

print(osoba["jmeno"])
#print(osoba["bydliste"]) # <// Key Error

osoba["bydliste"] = "Praha"
print(osoba)

# klic = input("Co chces vedet o Jane?")
# print(osoba[klic])

del osoba["jmeno"]
# print(osoba)
osoba['jmeno'] = 'Hana'

print(osoba.get("jmeno"))
print(osoba.get("jmeno", "Nezname"))
print(osoba.get(1, "Nezname"))
print()

for klic in osoba:
    print(klic)
    
print()
for klic in osoba.keys():
    print(klic)
    
print()
for hodnota in osoba.values():
    print(hodnota)
print()
for klic, hodnota in osoba.items():
    print(klic, ":", hodnota)
    
barvy = {
    "jablko": "cervena",
    "hruska": "zluta",
    "meloun": "zelena"
}

barvy["jablko"] = "velke"

print(barvy)

zelenina = {
    "mrkev": "cervena",
    "zeli": "zelenina"
}

barvy.update(zelenina)
print()
print(barvy)

zelenina2 = dict(mrkev=2, zeli=5)
print(zelenina2)

    
    