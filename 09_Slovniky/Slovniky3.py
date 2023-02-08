Opakovani3.py

osoba = {
    "jmeno": "Jana",
    "prijmeni": "Nova",
    "narozeni": "7.1.1995",
    "miry": [10, 20, 10],
    1: 2
}

osoba2 = {
    "jmeno": "Petra",
    "prijmeni": "Nova"
}

osoba3 = {
    "jmeno": "Pet",
    "prijmeni": "Novak"
}

seznam_osob = {
    1: osoba,
    2: osoba2,
    3: osoba3
}

for klic, hodnota in seznam_osob.items():
    #dokoncit