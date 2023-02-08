# Napiš funkci tah_hrace, která dostane řetězec s herním polem, zeptá se hráče, na kterou pozici chce hrát, a vrátí herní pole se zaznamenaným tahem hráče. 
# Funkce by měla odmítnout záporná nebo příliš velká čísla a tahy na obsazená políčka. Pokud uživatel zadá špatný vstup, funkce mu vynadá a zeptá se znova.

# Nezapomeň, že už máš funkci tah z předešlého úkolu.



# pozice = int(input('Zadej cislo policka: '))
pole = "o------------------"
symbol = "o" 

def tah(pole, pozice, symbol):
    pole = pole[:pozice] + symbol + pole[pozice+1:]                
    return pole

# def tah_hrace(pole):

#     while True:
        
#         pozice = int(input('Zadej cislo pozice: '))
#         if pozice > 19 or pozice < 0:
#             print('Toto cislo nelze pouzit!')
            
#         elif pozice != int(pozice):
#             print("Musis zadat cislo!")
            
#         elif pole[pozice] != '-':
#             print("Toto pole je jiz obsazene!")
            
#         else:
#             break
#     pole = tah(pole, pozice, symbol)
#     return pole

# print(tah_hrace(pole))
        
    
def tah_hrace(pole, symbol):

    while True:
        try:
            pozice = int(input('Zadej cislo pozice: '))
        except ValueError:    
            print("Musis zadat cislo!")
            
        else:    
            if pozice > 19 or pozice < 0:
                print('Toto cislo nelze pouzit!')
                       
            elif pole[pozice] != '-':
                print("Toto pole je jiz obsazene!")
                
            else:
                pole = tah(pole, pozice, symbol)
                return pole
            
    # pole = tah(pole, pozice, symbol)
    # return pole

print(tah_hrace(pole, symbol))   
      

        

    
    
     
    
    

