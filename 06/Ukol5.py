"Napiš funkci, která se zeptá na 3 čísla a zjistí, jestli je jejich součet větší než 10"

cislo = int(input("Zadej cislo: "))
cislo = int(input("Zadej cislo: "))
cislo = int(input("Zadej cislo: "))

cislo = cislo + cislo + cislo

def f(cislo):
  
    if cislo > 10:
        return 'je > 10'
    
    else:
        return 'je < 10'

print(cislo, f(cislo))

"----------------------------------------------------------------------------"
       

# def napis_cislo(zadej):
#     cislo = int(input(zadej))
#     cislo = int(input(zadej))+cislo
#     cislo = int(input(zadej))+cislo
    
#     if cislo > 10:
#         print(cislo, 'je > 10')
        
#     else:
#         print(cislo, 'je < 10')        
            
# napis_cislo("Zadej cislo: ") 

"-------------------------------------------------------------------------------"


