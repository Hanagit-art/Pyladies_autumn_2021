# Slovniky5.py
# Ukol 1:
# napiste program, ktry nacte textovy soubor
# a vypise jej radek po radku

# with open("text.txt", "r") as soubor:
#     for radek in soubor:
#         print(radek.strip())
                

# Ukol 2:
# Upravte ukol 1 tak, ze na zacatku kazde radky vypisu bude cislo radku

# with open("text.txt", "r") as soubor:
#     for i, radek in enumerate(soubor):
#         print(i, ":", radek.strip())
        
# Ukol 3:
# Predpokladejte, ze soubor na kazdem radku obsahuje prave dve slova (jmeno, prijmei).
# Napiste program, ktery vypise pouze krestni jmena.

with open("text.txt", "r") as soubor:
    for i, radek in enumerate(soubor):
        jmeno, prijmeni = radek.split()
        print(radek.split())
        # jmeno = radek.split()
        print(i, ":", radek.split()[0])

# Ukol 4:
# Predpokladejte, ze soubor na kazdem radku obsahuje prave slova (jmeno, prijmeni).
# Napiste program, ktery zjisti cetnosti krestnich jmen v souboru.
# Vysledkem bude slovnik, kde klice jsou jmena a hodnoty jejich cetnosti

cetnosti = dict()

with open("text.txt", "r") as soubor:
    for i, radek in enumerate(soubor):
        jmena = radek.split()
        krestni_jmeno = jmena[0]
        print(krestni_jmeno)
        cetnosti[krestni_jmeno] = cetnosti.get(krestni_jmeno, 0) + 1
        print("vyskytlo se ", cetnosti[krestni_jmeno], "krat")

    print(cetnosti)
for krestni_jmeno, cetnost in cetnosti.items():
    print(krestni_jmeno, ":", cetnosti)
    
del cetnosti["Petr"]
print(cetnosti)

prazdny_slovnik = {}
if prazdny_slovnik:
    print("Slovnik neni prazdny")
    
else:
    print("Ve slovniku nic neni.")
    
    
"""Tereza Vaňková
Zuzana Pokorná
Veronika Sarkányová
Lucka Říhová
Radka Planková
Eliška Doktorová
Zuzana Kašáková
Michaela Kroužková
Jana Slouková
Petr Messner
Petra Vidnerová
Vojtěch Růžička
Vašek Chalupníček
Oskar Hollmann
Mirek Brabenec
Petr Lessner
Petr Matuška
Miro Hrončok
Naďa Jašíková"""

