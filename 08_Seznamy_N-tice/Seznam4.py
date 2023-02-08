

stastnych_pet = [3,5,7,47,98]
potraviny = ["fazalo", "kukurice", "ryze", "kureci_maso"]
abeceda = ["a", "b", "c"]

# lepsi_abeceda = abeceda + ["n"] + ['o', 'p', 'q']

# print(lepsi_abeceda + lepsi_abeceda)

# konec_abecedy = ['x', 'y', 'z']
# abeceda.extend(konec_abecedy)

# print(abeceda)

# stastnych_pet.extend(range(10))

# print(stastnych_pet)


# mazani ze seznamu

# del potraviny[1]
# print(potraviny)

# del stastnych_pet[-3:]
# print(stastnych_pet)

# posledni_cislo = stastnych_pet.pop()
# stastnych_pet.append(posledni_cislo)

# print(posledni_cislo)
# print(stastnych_pet)

potraviny = ["fazale", "kukurice", "mleko", "ryze", "kureci maso"]

nova_potravina = "mleko"
if nova_potravina in potraviny:
    print("Uz je na seznamu")
else:
    potraviny.append(nova_potravina)
    print("Pridano", nova_potravina)
    
print(potraviny)

#  To same:
if potraviny:
    print("Bez nakoupit")
else:
    print("Nic nam nechybi")
    
# existuje shuffle a choice na michani/nahodny vyber

abeceda = "abcdefghijklmnopqrstuvxyz"
seznam_pismen = list(abeceda)

print(seznam_pismen)

suda_cisla = list(range(0, 20, 2))
print(suda_cisla)

# z_ntice = list("parek", "nuz", "pomazanka")
                
# print(z_ntice)
                