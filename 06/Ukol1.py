"Napiš funkci, která dostane jako argument identifikační číslo (např. rodné číslo, číslo platební karty, číslo OP) a "
"která vrátí řetězec, kde jsou všechna čísla mimo posledních čtyř nahrazena symbolem X."

"např. pro 1234567 funkce vrátí XXX4567"

Cislo = input("Zadej cislo OP: ")

# convert = str(Cislo)
# print(type(convert))
# print("xxxxx"+convert[-4:])

def function(Cislo):
    num = len(Cislo[:-4])
    # print(num)
    # print(Cislo[:-4])
    return num*"x"+Cislo[-4:]

print(function(Cislo))


   
