
def podil(citatel,jmenovatel):
    return citatel/jmenovatel

while True:
    try:
        citatel = int(input("Zadej citatele: "))
        jmenovatel = int(input("Zadej jmenovatele: "))
        print("Vysledek:", (podil(citatel,jmenovatel)))
        
    except ValueError:
        print("Zadejte cislo.")
    except ZeroDivisionError:
        print("Jmenovatel nesmi byt nula.")
    else:
        print("Konec vypoctu.")
        break