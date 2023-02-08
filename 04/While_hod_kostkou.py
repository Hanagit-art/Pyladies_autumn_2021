
import numpy as np

from random import randrange


for hrac in range(1, 5):

    list = []
    hod = 1
    while hod != 6:
        hod = randrange(1,7)
        list.append(hod)

    A = list

    print('hrac', hrac, A)
    #max_len = len(max(A, key=len))
    print(len(A))
    # list2 = []
    # list2.append(len(A))

    # list2 = []
#     B = len(A)
    
# list2.append(B)
    # print(list2)
    # x = max(list2)
    # print(x)

