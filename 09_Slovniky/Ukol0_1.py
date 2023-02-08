# Ukol1.py

# version_1

# n = int(input("Zadej range >= 1: "))

# def dictionery(n):
#     list_tuples = []
#     for i in range(1,n+1):
#         list_tuples.append((i,i**2))
#     return dict(list_tuples)

# print(dictionery(n))

# version_2

n = int(input("Zadej range >= 1: "))

def dictionery(n):
    dict = {}
    for i in range(1,n+1):
        # dict[i] = dict.setdefault(i,i**2)
        dict[i] = i ** 2
        # dict[i] = dict.get(i,i**2)
    return dict

print()   
print(dictionery(n),'\n')

dict = dictionery(n)

# for cislo, mocnina in dict.items():
#     print(f"Druha mocnina cisla {cislo} je {mocnina}")

# Ukol2

def soucet_klicu_a_hodnot(dict):    
    sum_keys = sum(dict.keys())
    sum_val = sum(dict.values())
    return sum_keys, sum_val

print(soucet_klicu_a_hodnot(dict))




