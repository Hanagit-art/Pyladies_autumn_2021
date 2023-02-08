
# napiste for cyklus, ktery vypise katde druhe pismeno retezce
# nactete retezec od uzivatele
# velkumi pismeny!

retezec = input("Zadej retezec: ")
retezec = retezec.strip()

delka = len(retezec)
for i in range(1, delka, 2):
    print(retezec[i].upper(), end="")
print()