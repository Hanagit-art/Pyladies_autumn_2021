# Vyjimky4.py
# Nutno doupravit
def tah(pole, cislo_policka, symbol):
    return pole[:cislo_policka] + symbol + pole[cislo_policka+1:]

def tah_hrace(pole):
    while True:
        try:
            pozice = int(input("Kam chces hrat? "))
        except ValueError:
            print("Musis zadat cislo!")
        else:
            if pozice < 0 or pozice >= len(pole):
                print("Nemuses hrat mimo pole!") 
            
            elif pole[pozice] != '-':
                print("Misto je jiz obsazene.")
            else:
                break
            
    pole = pole[:pozice] + 'o' + pole[pozice+1:]
    return pole

print(tah_hrace("-x-------------------"))
    