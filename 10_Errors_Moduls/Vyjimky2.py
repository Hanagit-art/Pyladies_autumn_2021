#  Vyjimky2.py
#  Otevirani souboru

try:
    f = open("soubor.txt", "r")
except FileNotFoundError:
    f = open("soubor1.txt", "w")
    f.write("Soubor neexistoval, tak jsem ho vytvoril.")
    print("Soubor neexistoval, tak jsem ho vytvoril.")

else:   
    data = f.radline()
    print(data)

finally:
    f.close()