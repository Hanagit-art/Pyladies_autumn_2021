

# Ukol:
# Dostaneme seznam cisel
# Vratit trikatr vetsi seznam
# [2, 3, 5] -> [6, 9, 15]

seznam = [2, 3, 5] 

novy_seznam = []
for cislo in seznam:
    vetsi_cislo = cislo * 3
    novy_seznam.append(vetsi_cislo)
    
print(novy_seznam)