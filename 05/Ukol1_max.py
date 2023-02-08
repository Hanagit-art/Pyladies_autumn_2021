# Napiš funkci, která vrátí maximální hodnotu ze tří zadaných čísel.

# num1 = int(input("Zadej cislo: "))
# num2 = int(input("Zadej cislo: "))
# num3 = int(input("Zadej cislo: "))

# max_num = max(num1, num2, num3)

# print(max_num)

"--------------------------------------------------------------------------------"

num1 = int(input("Zadej cislo: "))
num2 = int(input("Zadej cislo: "))
num3 = int(input("Zadej cislo: "))

def maximum(num1,num2,num3):
    max_num = max(num1, num2, num3)
    return max_num
    
print(maximum(num1, num2, num3))

"---------------------------------------------------------------------------------"
# list = []

# for i in range(3):
#     num = int(input("Zadej cislo: "))
#     list.append(num)
#     print()
    
# print(list)
# print(max(list))

