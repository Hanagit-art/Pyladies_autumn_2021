# Ukol_chybne_zaznamy.py

seznam = ['pepa novák','Jiří Sládek','Ivo navrátil','jan Poledník']
# for zaznam in seznam:
#     jmeno_a_prijmeni = zaznam.split(' ')
#     print(jmeno_a_prijmeni)

def vyber_chybne(seznam):
    vysledek = []
    for zaznam in seznam:
        jmeno_a_prijmeni = zaznam.split(' ')
        jmeno = jmeno_a_prijmeni[0]
        prijmeni = jmeno_a_prijmeni[1]
        if jmeno[0].islower() or prijmeni[0].islower():
            vysledek.append(zaznam)
    return vysledek

print(vyber_chybne(seznam))

def vyber_spravne(seznam):
    vysledek = []
    for zaznam in seznam:
        jmeno_a_prijmeni = zaznam.split(' ')
        jmeno = jmeno_a_prijmeni[0]
        prijmeni = jmeno_a_prijmeni[1]
        if not jmeno[0].islower() and not prijmeni[0].islower():
            vysledek.append(zaznam)
    return vysledek

print(vyber_spravne(seznam))

def oprav_zaznamy(seznam):
    vysledek = []
    for zaznam in seznam:
        jmeno_a_prijmeni = zaznam.split(' ')
        jmeno = jmeno_a_prijmeni[0].capitalize()
        prijmeni = jmeno_a_prijmeni[1].capitalize()
        vysledek.append(jmeno + ' ' + prijmeni)
    return vysledek

print(oprav_zaznamy(seznam))