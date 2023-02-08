# Ukol3.py
   
input = [(0,0),(1,0),(2, 2),(4,3),(8,9),(8,9)]

def f(input): 
    dots = 10 * "."
    
    list_list = []
    for i in range(10):
        list_list.append(list(dots))
        
    for raw, col in input:
        list_list[raw][col] = "X"   
    return list_list

list_list = f(input)    
# print(list_list)

for list in list_list:
    for item in list:
        print(item, end=' ')
        
# res = [item for list in list_list for item in list]
# print(res, end=' ')
    
    print()
    
