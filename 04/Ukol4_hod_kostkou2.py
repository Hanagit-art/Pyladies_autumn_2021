
"""První hráč hází kostkou (t.j. vybírají se náhodná čísla od 1 do 6), dokud nepadne šestka. Potom hází další hráč, dokud nepadne šestka i jemu. Potom hází hráč třetí a nakonec čtvrtý. Vyhrává ten, kdo na hození šestky potřeboval nejvíc hodů. (V případě shody vyhraje ten, kdo házel dřív.)

Program by měl vypisovat všechny hody a nakonec napsat, kdo vyhrál."""

from random import randrange


def hod_kostkou():
    "Funkce stiuluje hru jednoho hrace."
    
    pocet_hodu = 0
    while True:
        hod = randrange(1,7)
        pocet_hodu += 1
        if hod == 6:
            break
    return pocet_hodu
    
pocet_hodu = hod_kostkou()
# print("Pocet hodu byl:", pocet_hodu)

nejvic_hodu = 0
vitez = 0

for cislo_hrace in range(1,5):
    pocet_hodu = hod_kostkou()
    print("Pocet hodu hrace c.", cislo_hrace, "byl:", pocet_hodu)
    if pocet_hodu > nejvic_hodu:
        nejvic_hodu = pocet_hodu
        vitez = cislo_hrace
        
print("Nejvetsi pocet hodu byl", nejvic_hodu)
print("Vitez je hrac c.", vitez)


        