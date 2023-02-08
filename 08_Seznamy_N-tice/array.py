# array.py

array1 = [1,2,3,4]
array2 = [2,3,4,5]

# array = array1 + array2
# print(array)

# array = []
# array.append(array1)
# array.append(array2)
# print(array)

def f(pozice_array,prvek,cislo):
    array = []
    array.append(array1)
    array.append(array2)
    array[pozice_array][prvek] = cislo
    for i in range(2):   
        return array
    
print(f(1,0,9,))
     
# pozice_array = int(input("Zadej cislo pozice array:"))
# prvek = int(input("Zadej cislo prvku:"))
# cislo = int(input("Zadej cislo:"))

# array[pozice_array][prvek] = cislo

# # print(array)

# def f(array):
#     for i in range(2):   
#         return array
    
# print(f(array))



   
