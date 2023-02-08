        
zvirata = ["had",
           "pes",
           "andulka",
           "kocka",
           "kralik"
           ]

def vytvor_dvojice(seznam):
    dvojice = []
    for prvek in seznam:
        klic = prvek[1:]
        cele_jmeno = prvek
        dvojice.append((klic, cele_jmeno))
    return dvojice

seznam_dvojic = vytvor_dvojice(zvirata)
print(seznam_dvojic)

print()
seznam_dvojic.sort()
print(seznam_dvojic)

vysledny_seznam = []
for klic, zvire in seznam_svojic:
    vysledny_seznam.append(zvire)
    
print()
print(vysledny_seznam)


"-------------------------------------------------------------------------"
seznam = ["kralik", "kocka", "pes", "morce"]

print(seznam[1])
print(seznam[::2])
print(seznam[-1])
druhy_seznam = seznam #.copy()

print(seznam, "\n", druhy_seznam)
# del seznam[-1]
#print(seznam, "\n", druhy_seznam)

print(seznam is druhy_seznam)
print(seznam == druhy_seznam)

"----------------------------------------------------------------------"



def dej_prvni_pismena(seznam):
    prvni_pismena = []
    for prvek in seznam:
        prvni_pismena.append(prvek[0])
    return prvni_pismena

# print(dej_prvni_pismena(seznam))
# print(dej_prvni_pismena(["ahoj", "nazdar"]))
# print(dej_prvni_pismena(["ahoj", "nazdar"]))

def seber_hlavu_a_ocas(seznam):
    del seznam[0]
    del seznam[-1]
    return seznam
    
print(seber_hlavu_a_ocas(seznam))
print(seznam)

def seznam_bez_hlavy_a_ocasu(seznam):
    novy = seznam.copy()
    del novy[0]
    del novy[-1]
    return novy

print(seznam_bez_hlavy_a_ocasu(seznam))
print(seznam)

print("Ahoj Pyladies! Jak se mate?".split())
slova = "Ahoj Pyladies! Jak se mate?"
print(slova)
print(", ".join(slova))

