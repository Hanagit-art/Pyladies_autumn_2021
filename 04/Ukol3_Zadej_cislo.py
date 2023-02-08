
"Prvni verze, co jsem ti posilala"

number = int(input("Zadje cislo: "))
while True:
    number = int(input("Zadje cislo: "))
    number = min(number, number)
    
    print(number)   

    
    
     


#     min_number = min(number1, number2)
# print(min_number)
# -----------------------------------------------------
" Tady to funguje s nulou, ale vypisuje mi to minimum jen ze dvou cisel"
# while True:
#     number1 = int(input('Zadej cislo: '))
#     if number1 == 0:
#         break
    
#     else:
#         number2 = int(input('Zadej cislo: '))
#         if number2 == 0:
#             break
        
# if number1 != 0:
#         min_number = min(number1, number2)
               
    

# ----------------------------------------------------
"Vypisuje min cislo, ale s nulou na prvnim ci druhem miste to dava error, min_number is not defined"

# number1 = int(input('Zadej cislo: '))    
# while number1 != 0:
#     number2 = int(input('Zadej cislo: '))
#     if number2 == 0:
#         break
        
#     min_number = min(number1, number2)
   
# print(min_number)

