# Vytvoř funkci nakresli_n_uhelnik, která vykreslí pro zadaný počet stran n-úhelník. Pomocí této funkce vykresli následující obrázek:

# mnohoúhelníky

# Vnitřní úhel pravidelného n-úhelníka má 180 × (1-2/n) stupňů.

# Aby byly tvary zhruba stejně veliké, použij pro n-úhelník délku strany např. 200/n

                
from turtle import forward, left, pendown, penup, exitonclick

"verze 1"

# n = int(input('Zadej pocet uhlu: '))

# def nakresli_n_uhelnik(n):

#     for i in range(n):
#         forward(200)
#         left(180-180*(1-2/n))
    
#     exitonclick()
    
# nakresli_n_uhelnik(n)

"------------------------------------------------------------------------------"
"verze 2"

# n = 4
# for n in range(n+1,9):
    
#     def nakresli_n_uhelnik():

#         for obrazek in range(n):       
#             forward(200/n)
#             left(180-180*(1-2/n))

#         return obrazek

#     nakresli_n_uhelnik()
#     penup()
#     forward(80)
#     pendown() 
# exitonclick()

"-------------------------------------------------------------------------------"
"verze 3"

# def nakresli_n_uhelnik():
#     n = 4
#     for n in range(n+1,9):        

#         for obrazek in range(n):       
#             forward(200/n)
#             left(180-180*(1-2/n))
#         penup()
#         forward(80)
#         pendown() 
           
#     return obrazek           

# nakresli_n_uhelnik()

# exitonclick()


"---------------------------------------------------------------------------------"
"verze 4"
    
def nakresli_n_uhelnik():

    for obrazek in range(n):       
        forward(200/n)
        left(180-180*(1-2/n))
    return obrazek

n = 4    
for n in range(n+1,9):

    nakresli_n_uhelnik()
    
    penup()
    forward(80)
    pendown() 
    
exitonclick()