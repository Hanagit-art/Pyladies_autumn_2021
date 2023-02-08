


o1 = input('Jmeno: ')

print(o1[0].upper())

retezec = "cokolada"

print(retezec[2:6])
print(retezec[1:-1])

print(retezec[2:])
print(retezec[:3])

print("*" +retezec[1:])

def zamen(retezec, pozice, znak):
   return retezec[:pozice] + znak + retezec[pozice+1:]
   
print("cokolada", zamen("cokolada", 2, "L"))

# vstup = input("Neco zadej")

# print(vstup.lstrip())

# retezec =  "cokolada"
# print("Retezec", retezec, "obsahuje ", 
#       retezec.count("o"), "krat pismeno \"o\"")

# delka = len(retezec)
# print("Retezec ", retezec, "ma ", delka, "znaku.")

# if "oko" in "cokolada" :
#     print("oko je v cokolade")
    
# if "koko" in rezetec