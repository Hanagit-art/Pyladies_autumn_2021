
"Pomocí cyklů for a parametru end pro print napiš program, který postupně z jednotlivých 'X' vypíše:"
# X X X X X
# X X X X X
# X X X X X
# X X X X X
# X X X X X
"Z jednotlivých 'X'“ znamená, že nepoužiješ např. print('X X X X X'), ani násobení řetězců, t. j. např. 5 * 'X'."

"Jak pojmenuješ proměnnou cyklu? A tu druhou?"

# for j in range(5):
#     for i in range(4):
#         print('x', end='')
#     print("x")
    
for j in range(5):
    for i in range(5):
        print('x', end='')
        
    print()
    


    