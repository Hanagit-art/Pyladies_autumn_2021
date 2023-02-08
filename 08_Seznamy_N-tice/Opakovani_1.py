# Napiste funkci, ktera jako prvni arguent bere retezec
# Funkce spocita, kolk je v retezci velky "X"

# Navod:
# postupne vypiste vsechna pismenka retezce

"--------------------------------------------------------"

# retezec = "hafXhafXX"

# def pocet_X(retezec):
#     vypis = retezec.count("X")
#     return vypis
# print(pocet_X(retezec))

"--------------------------------------------------------"
# def pocet_X(retezec):
#     for pismenko in retezec:
#         print(pismenko)
        
# pocet_X(retezec)

"--------------------------------------------------------"

# def pocet_X(retezec):
#     pocet = 0    
#     for pismenko in retezec:
#         if pismenko == 'X':
#             pocet = pocet + 1
#     return pocet
    
# print(pocet_X(retezec))

"--------------------------------------------------------"
# retezec = "hafXhafXX"
# i = 0
# while i < len(retezec):
#     if retezec[i] == "X":
#         pocet = i + 1

# print(pocet)

"------------------------------------------------------------------------------"
 
 # Zvetsi "o jednu cislici na treti pozici
 
#"hn3456" to "hn4456"
 
# retezec = "hn3456"
 
# def zamen(retezec, pozice, cislo):
#     vysledek = retezec[:pozice] + cislo + retezec[pozice + 1:]
#     print(vysledek)
    
# zamen(retezec, 2, "4")

"------------------------------------------------------------------------------"

# def zvetsi_od_tretiho(retezec):
#     prvni_pulka = retezec[:2]
#     druha_pulka = retezec[2:]
    
#     zvetsena_druha_pulka = ""
#     for i in range(len(druha_pulka)):
#         zvetsena_druha_pulka = zvetsena_druha_pulka + chr(ord(druha_pulka[i]) + 1)
        
#     return prvni_pulka + zvetsena_druha_pulka

# print(zvetsi_od_tretiho("111111111"))


"----------------------------------------------------------------------------------"
# Napiste funkci, ktera pomlcku na treti pozici v retezci
# Zmen na "X"  

"Reseni A"
# retezec = "-------------"
 
# def zamen(retezec, pozice, cislo):
#     vysledek = retezec[:pozice] + cislo + retezec[pozice + 1:]
#     print(vysledek)
    
# zamen(retezec, 4, "X")

"----------------------------------------------------------------------------------"
"Reseni B"
# def treti_X(retezec):
#     treti_znak = retezec[2]
#     prvni_pulka = retezec[:2]
#     druha_pulka = retezec[3:]
    
#     zmeneny_treti = "X"
    
#     return prvni_pulka + zmeneny_treti + druha_pulka

# print(treti_X("-----------"))

"----------------------------------------------------------------------------------"

# Funkce bere retezec a index
# Index: 4, retezec:"-------"
# Vrati: "---X---"

# retezec = "-------"
 
# def zamen(retezec, pozice, znak):
#     vysledek = retezec[:pozice] + znak + retezec[pozice + 1:]
#     print(vysledek)
    
# zamen(retezec, 3, "x")

"-----------------------------------------------------------------------------------"

def tahni(retezec, index):
    prvni_pulka = retezec[:index]
    druha_pulka = retezec[index+1:]
    
    return prvni_pulka + "X" + druha_pulka

print(tahni("--------------------", 5))

