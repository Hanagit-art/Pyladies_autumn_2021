
# Napiš funkci, která ověří, že zadaná teplota je v daném intervalu. Funkce bude mít tři parametry (teplota, dolní mez, horní mez) a bude vracet True/False.

teplota = int(input("Zadej teplotu: "))
min_limit = 0
max_limit = 40
def check(teplota, min_limit, max_limit):
    if teplota >= min_limit and teplota <= max_limit:
        return True
    else:
        return False
    
print(check(teplota, min_limit, max_limit))  
