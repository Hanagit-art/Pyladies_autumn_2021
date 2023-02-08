"""Napiš funkci, která s pomocí cyklu for a příkazu if vypíše z jednotlivých 'X' a mezer následující obrazec:

X X X X X X
X         X
X         X
X         X
X         X
X X X X X X"""

def f_obrazec():
    for r in range(6):
        print("x", end=" ")

        for k in range(4):
                
            if r in range(1,5):
                print(" ", end=" ")

            else:
                print("x", end=" ")

        print("x")  
    
f_obrazec()

# for j in range(6):
#     for i in range(4):
#         print('X', end='')
#     print()

