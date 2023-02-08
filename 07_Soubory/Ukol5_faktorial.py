# Ukol5_faktorial.py

from math import factorial

N = int(input("Zadej hodnotu n!: "))

print(factorial(N))

def jeprvocislo(N):
    
    for i in range(2,N-1):

        if N%i == 0:
            return False

    return True


if N <= 1:
    print("ne")
elif jeprvocislo(N) == True:  # True zde byt nemusi, je definovane funkci.      
    print("ano")
elif N == 2 or N == 3:
    print("ano")

else:
    print("ne")
            

        
       
    
