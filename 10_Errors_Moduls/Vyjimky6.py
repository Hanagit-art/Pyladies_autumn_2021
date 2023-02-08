# def nacti_cislo():
#     while True:
#         odpoved = input('Zadej číslo: ')
#         try:
#             return int(odpoved)
#         except ValueError:
#             print('To nebylo číslo! Zkus to znovu.')
            
# print(nacti_cislo())
            
def nacti_cislo():
    odpoved = input('Zadej číslo: ')
    try:
        cislo = int(odpoved)
    except ValueError:
        print('To nebylo číslo! Pokračuji s nulou.')
        cislo = 0
    return cislo

print(nacti_cislo())