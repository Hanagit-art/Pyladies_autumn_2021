
# Vytvoř funkci, která spočítá Body Mass Index pro kočky. Vstupem (parametry) funkce bude obvod hrudníku (cm) a délka zadní nohy od kolena ke kotníku (cm). Funkce vrátí číslo (feline body mass index, fBMI).
# Postup výpočtu fBMI: 1. Vydělit obvod hrudníku 0.7062 a odečíst délku nohy. 2. Vydělit výsledek 0.9156. 3. Od výsledku bodu 2 odečíst délku nohy.

obvod = 40
delka_nohy = 20

def BMI(obvod, delka_nohy):
    bmi = (obvod/0.7062 - delka_nohy)/0.9156
    bmi = bmi - delka_nohy
    
    return bmi

print(BMI(obvod, delka_nohy))