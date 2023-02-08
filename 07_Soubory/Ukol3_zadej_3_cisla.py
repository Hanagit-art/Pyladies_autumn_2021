# Ukol3_zadej_3_cisla.py
"""Napiš program, který se zeptá na 3 čísla a zjistí, 
jestli je jejich součet větší než 10. 
Dokážeš jej vymyslet tak, aby funkce input byla v kódu zapsaná jen jednou? ;)"""



# def napis_cislo(zadej): 
      
#     while True:
            
#         cislo = int(input(zadej))
    
#         print(cislo)
        
#         # if cislo > 10:
#         #     print(cislo, 'je > 10')
            
#         # else:
#         #     print(cislo, 'je < 10')        
            
# napis_cislo("Zadej cislo: ")     
        
# from numpy import number


# i, numbers = 1, [] 
# while i < 4: 
#     try: 
#         n = float(input(f”Write {i} number:”)) 
#         numbers.append(n) 
#         i += 1 
#     except Exception as e: 
#         print(f”{n} isn’t a number, try again”) 
# a, b, c = numbers 
# print(“Result: {(a + b)*c}”) 


soucet = 0
for i in range(3):
    soucet = soucet + int(input("Zadej cislo: "))
    print(soucet)
        
if soucet > 10:
    print("Soucet je vetsi nez 10.")
        
else:
    print("Soucet je mensi nez 10.")