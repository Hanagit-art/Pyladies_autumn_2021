
# import numpy as np

list = []
number = 1
while number != 0:
    number = int(input('zadej cislo: '))
    list.append(number)

  
# A = np.array(list)   
# print(A[A!=0])
# print(min(A[A!=0]))

A = list
C = [i for i in A if i != 0]

print(C)
print(min(C))
