
# Slovniky4.py

retezec = input("Zadej cisla oddelena carkou: ")
print(retezec)
cisla = retezec.split(",")

print(cisla)
cetnosti = {}

for cislo in cisla:
    cislo = int(cislo)
    cetnosti[cislo] = cetnosti.get(cislo, 0) + 1
    
print(cetnosti)

for klic, hodnota in cetnosti.items():    
    # print(f"{klic}: vyskytuje se {hodnota}-krat")
    print('{}:vyskytuje se {}'.format(klic, hodnota))