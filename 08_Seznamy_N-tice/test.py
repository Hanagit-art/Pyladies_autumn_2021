# for j in range(1,6):
#     for i in range(j):
#         print('x', end='')
#     print()
    
# number = int(input('zadej cislo: '))
# while True:
#     if number == 0:
#         break
#     zadej = int(input('zadej cislo: '))
#     if zadej == 0:
#         break
#     number = min(zadej, number)
   
# print(number)

def podil_a_zbytek(a, b):
    return a // b, a % b

podil, zbytek = podil_a_zbytek(12, 5)

print(podil,",",zbytek)