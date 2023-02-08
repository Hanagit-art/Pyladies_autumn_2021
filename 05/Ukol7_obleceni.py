
# Napiš funkci, která pro zadanou teplotu doporučí vhodné oblečení. Využij funkci z předchozího úkolu.

# teplota = int(input("Zadej teplotu: "))
# min_limit = 0
# max_limit = 40
# def check(teplota, min_limit, max_limit):
#     if teplota > max_limit:
#         return "To neprezijes!"
#     elif teplota >= min_limit+20:
#         return "Oblec si plavky!"
#     elif teplota >= min_limit+10:
#         return "Oblec si kalhoty!"
#     elif teplota >= min_limit:
#         return "Oblec si bundu"
#     else:
#         return "Poradne se oblec, mrzne!"

    
# print(check(teplota, min_limit, max_limit)) 

"-------------------------------------------------------------------------"

teplota = int(input("Zadej teplotu a ja ti doporucim obleceni: "))
min_limit = 0
max_limit = 30

def check(teplota, min_limit, max_limit):
    if teplota >= min_limit and teplota <= max_limit:
        return True
    else:
        return False
    
def doporuc_obleceni():
    if check(teplota, min_limit, max_limit) == True and teplota < min_limit +10:
        print("Je  chladno, vem si bundu a kalhoty!")
        
    elif check(teplota, min_limit, max_limit) == True and teplota < 20:
        print("Je prijemne, staci mikina!")
    
    elif check(teplota, min_limit, max_limit) == True:
        print("Je teplo, vem si saty!")
           
    elif check(teplota, min_limit, max_limit) == False and teplota > max_limit:
        print("Teplota je mimo maximalni limit. Je opravdu horko. Vem si plavky!")
        
    else:
        print("Teplota je mimo minimalni limit. Dobre se oblec. Vem si cepici a bundu!")
    
doporuc_obleceni()
